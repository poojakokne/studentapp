from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    class_name = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    mobile = models.IntegerField()
    address = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)


class StudentAcademics(models.Model):
    roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    biology = models.IntegerField()
    english = models.IntegerField()

    def __str__(self):
        return str(self.roll_no)
