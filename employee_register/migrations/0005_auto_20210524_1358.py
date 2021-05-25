# Generated by Django 3.1.2 on 2021-05-24 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0004_auto_20210524_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='created',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='fullname',
            new_name='lattitude',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emp_code',
            new_name='longtitude',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='title',
            new_name='plate',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='ex',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mobile',
        ),
    ]
