# Generated by Django 2.0.8 on 2018-09-30 17:26

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_assessmentpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentpage',
            name='content',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]