# Generated by Django 2.2.5 on 2019-09-09 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tb_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('contact', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
            ],
        ),
    ]
