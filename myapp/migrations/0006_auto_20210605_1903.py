# Generated by Django 3.2.3 on 2021-06-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_registeredcustomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcustomer',
            name='contact',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='fname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='lname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='password1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
