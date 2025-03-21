# Generated by Django 3.2.16 on 2023-03-31 04:47

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
            name='Board',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('board_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('board_name', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='global_entity.university')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('comment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('content', models.CharField(max_length=512)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_anon', models.BooleanField(default=False)),
                ('ancestor_comment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('post_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=512)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_anon', models.BooleanField(default=False)),
                ('is_question', models.BooleanField(default=False)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.board')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScrapPost',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('scrap_post_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.post')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'scrap_post',
            },
        ),
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('like_post_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.post')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'like_post',
            },
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('like_post_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.comment')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'like_comment',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BlackPost',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('black_post_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.post')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'black_post',
            },
        ),
        migrations.CreateModel(
            name='BlackComment',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('black_comment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='primary key')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.comment')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'black_comment',
            },
        ),
    ]
