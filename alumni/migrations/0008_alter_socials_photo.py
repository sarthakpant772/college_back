# Generated by Django 3.2.5 on 2021-10-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0007_alter_socials_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socials',
            name='photo',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]