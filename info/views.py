from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required
from info.forms import AddStudentForm
from info.models import StudentAcademics, StudentInfo
from bs4 import BeautifulSoup
import requests

# Create your views here.


@login_required
def create_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data['roll_no']
            name = form.cleaned_data['name']
            classname = form.cleaned_data['class_name']
            school = form.cleaned_data['school']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            maths = form.cleaned_data['maths']
            physics = form.cleaned_data['physics']
            chemistry = form.cleaned_data['chemistry']
            biology = form.cleaned_data['biology']
            english = form.cleaned_data['english']

            try:
                studentobj = StudentInfo.objects.create(roll_no=roll_no, name=name, class_name=classname, school=school,
                                                        mobile=mobile, address=address)
                StudentAcademics.objects.create(roll_no=studentobj, maths=maths, physics=physics, chemistry=chemistry,
                                                biology=biology, english=english)

                messages.success(
                    request, "Successfully Added Student Record In Database")
                return HttpResponseRedirect(reverse('create_student'))
            except:
                messages.error(
                    request, "Failed to Add Student Record In Database")
                return HttpResponseRedirect(reverse('create_student'))

        else:

            form = AddStudentForm(request.POST)
            return render(request, 'add_student.html', {'form': form})
    else:
        form = AddStudentForm()
        return render(request, 'create_student.html', {'form': form})


def show_student(request):
    student_list = StudentInfo.objects.all()
    return render(request, 'show_student.html', {'student_list': student_list})

@login_required
def academics_details(request, id):
    student_academics = StudentAcademics.objects.get(roll_no=id)
    return render(request, 'academics_data.html', {'student_academics': student_academics})


@login_required
def update_student(request, id):
    if request.method == "POST":
        form = AddStudentForm(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data['roll_no']
            name = form.cleaned_data['name']
            classname = form.cleaned_data['class_name']
            school = form.cleaned_data['school']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            maths = form.cleaned_data['maths']
            physics = form.cleaned_data['physics']
            chemistry = form.cleaned_data['chemistry']
            biology = form.cleaned_data['biology']
            english = form.cleaned_data['english']

            try:
                studentobj = StudentInfo.objects.get(roll_no=roll_no)

                studentobj.roll_no = roll_no
                studentobj.name = name
                studentobj.class_name = classname
                studentobj.school = school
                studentobj.mobile = mobile
                studentobj.address = address
                studentobj.save()
                markobj = StudentAcademics.objects.get(roll_no=roll_no)
                markobj.maths = maths
                markobj.physics = physics
                markobj.chemistry = chemistry
                markobj.biology = biology
                markobj.english = english
                markobj.roll_no = studentobj
                markobj.save()

                messages.success(request, "Successfully Edited Student")
                return HttpResponseRedirect(reverse('show_student'))
            except:
                messages.error(request, "Failed to Edit Student")
                return HttpResponseRedirect(reverse('show_student'))

        else:

            form = AddStudentForm(request.POST)
            return render(request, 'edit_student.html', {'form': form})

    else:

        student = StudentInfo.objects.get(roll_no=id)
        try:
            marks = StudentAcademics.objects.get(roll_no=student)
        except:
            return HttpResponse('Marks Not Available ')
        form = AddStudentForm()

        form.fields['roll_no'].initial = student.roll_no
        form.fields['name'].initial = student.name
        form.fields['class_name'].initial = student.class_name
        form.fields['school'].initial = student.school
        form.fields['mobile'].initial = student.mobile
        form.fields['address'].initial = student.address
        form.fields['maths'].initial = marks.maths
        form.fields['physics'].initial = marks.physics
        form.fields['chemistry'].initial = marks.chemistry
        form.fields['biology'].initial = marks.biology
        form.fields['english'].initial = marks.english

        return render(request, 'edit_student.html', {'form': form, 'student': student})


@login_required
def delete_student(request, id):
    studentobj = StudentInfo.objects.get(roll_no=id)
    studentobj.delete()
    messages.error(request, "Successfully Deleted Student")
    return HttpResponseRedirect(reverse('show_student'))


def url_search(request):
    if request.method == "POST":
        website_url = request.POST.get("website_url")
        if not website_url.startswith('http://'):
            response = requests.get('http://'+website_url)
        else:
            response = requests.get(website_url)

        beautifulobj = BeautifulSoup(response.content, 'html.parser')
        url_list = []
        for element in beautifulobj.find_all('a'):
            url = element.get('href')
            url_list.append(url)
        length = len(url_list)
        context = {'url_list': url_list, 'length': length}
    else:
        context = {}

    return render(request, 'url_search.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")