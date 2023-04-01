# Generated by Django 3.2.16 on 2023-03-31 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('global_entity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('subject_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('subject_name', models.CharField(max_length=512)),
                ('subject_code', models.CharField(max_length=512)),
                ('subject_grade', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='global_entity.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('lecture_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('semester', models.CharField(max_length=512)),
                ('classroom', models.CharField(max_length=512)),
                ('professor_name', models.CharField(max_length=512)),
                ('lecture_time', models.CharField(max_length=512)),
                ('score', models.FloatField()),
                ('listener', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='timetable.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
