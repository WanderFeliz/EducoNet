# Generated by Django 3.2 on 2021-06-25 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20210625_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='TYPE',
            new_name='blog_type',
        ),
    ]