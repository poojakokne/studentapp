# Generated by Django 4.0.1 on 2022-01-12 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('class_name', models.CharField(max_length=256)),
                ('school', models.CharField(max_length=256)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAcademics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maths', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField()),
                ('biology', models.IntegerField()),
                ('english', models.IntegerField()),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.studentinfo')),
            ],
        ),
    ]