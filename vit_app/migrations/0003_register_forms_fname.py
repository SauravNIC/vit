# Generated by Django 3.2.7 on 2021-09-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vit_app', '0002_rename_register_form_register_forms'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_forms',
            name='Fname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
