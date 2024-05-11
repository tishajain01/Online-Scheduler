# Generated by Django 4.2.7 on 2024-05-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_instructor_department_instructor_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.URLField()),
            ],
        ),
    ]