# Generated by Django 3.2.5 on 2021-07-25 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socials',
            name='pass_out_year',
            field=models.IntegerField(help_text='Your passout year', null=True),
        ),
    ]
