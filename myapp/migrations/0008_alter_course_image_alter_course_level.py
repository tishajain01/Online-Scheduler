# Generated by Django 4.2.7 on 2024-05-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course_images/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('ADVANCED', 'Advanced')], max_length=20),
        ),
    ]
