# Generated by Django 3.2.16 on 2023-03-30 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='global.basemodel')),
                ('univ_name', models.CharField(max_length=100)),
            ],
            bases=('global.basemodel',),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='global.basemodel')),
                ('dept_name', models.CharField(max_length=100)),
                ('univ', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='global.university')),
            ],
            bases=('global.basemodel',),
        ),
    ]
