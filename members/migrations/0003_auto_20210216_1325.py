# Generated by Django 2.2.5 on 2021-02-16 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20210216_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='prof_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='프로필 사진'),
        ),
    ]
