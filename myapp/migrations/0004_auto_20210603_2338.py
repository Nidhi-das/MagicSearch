# Generated by Django 3.2.3 on 2021-06-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_newcustomer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcustomer',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registeredcustomer',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
