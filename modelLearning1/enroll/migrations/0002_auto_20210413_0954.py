# Generated by Django 3.1.1 on 2021-04-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stuemail',
            field=models.EmailField(default='example@gmail.com', max_length=70),
        ),
        migrations.AddField(
            model_name='student',
            name='stupass',
            field=models.CharField(default='password', max_length=70),
        ),
    ]
