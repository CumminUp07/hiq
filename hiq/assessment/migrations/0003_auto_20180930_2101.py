# Generated by Django 2.0.8 on 2018-09-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_auto_20180930_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlequestion',
            name='correct_ans',
            field=models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')], max_length=2),
        ),
    ]
