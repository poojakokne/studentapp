from django import forms
from django.forms.widgets import HiddenInput


class AddStudentForm(forms.Form):
    
    roll_no=forms.IntegerField(label='Roll No',widget=forms.NumberInput(attrs={'class':'form-control'}))
    name=forms.CharField(label='Full Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    class_name=forms.CharField(label='Class Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    school=forms.CharField(label='School Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile=forms.IntegerField(label='Mobile No',widget=forms.NumberInput(attrs={'class':'form-control'}))
    address=forms.CharField(label='Address',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    maths=forms.IntegerField(label='Math Marks',widget=forms.NumberInput(attrs={'class':'form-control'}))
    physics=forms.IntegerField(label='Physics Marks',widget=forms.NumberInput(attrs={'class':'form-control'}))
    chemistry=forms.IntegerField(label='Chemistry Marks',widget=forms.NumberInput(attrs={'class':'form-control'}))
    biology=forms.IntegerField(label='Biology Marks',widget=forms.NumberInput(attrs={'class':'form-control'}))
    english=forms.IntegerField(label='English Marks',widget=forms.NumberInput(attrs={'class':'form-control'}))
