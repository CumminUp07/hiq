# Generated by Django 2.0.8 on 2018-09-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180927_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sub_heading',
            field=models.TextField(default=''),
        ),
    ]