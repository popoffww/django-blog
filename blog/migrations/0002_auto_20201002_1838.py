# Generated by Django 3.1.1 on 2020-10-02 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub'], 'verbose_name': 'Статья блога', 'verbose_name_plural': 'Статьи блога'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title']},
        ),
    ]