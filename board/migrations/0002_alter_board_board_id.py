# Generated by Django 3.2.16 on 2023-03-31 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='primary key'),
        ),
    ]
