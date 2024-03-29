# Generated by Django 2.1.5 on 2019-08-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
