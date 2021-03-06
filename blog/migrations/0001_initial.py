# Generated by Django 3.1.1 on 2020-09-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тэг')),
                ('slug', models.CharField(max_length=50, unique=True, verbose_name='Слаг')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True, verbose_name='Слаг')),
                ('body', models.TextField(blank=True, db_index=True, verbose_name='Текст поста')),
                ('date_pub', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('draft', models.BooleanField(verbose_name='Черновик')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Статья блога',
                'verbose_name_plural': 'Статьи блога',
            },
        ),
    ]
