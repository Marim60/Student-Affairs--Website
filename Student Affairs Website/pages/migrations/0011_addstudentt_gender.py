# Generated by Django 4.0.4 on 2022-05-24 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_addstudentt_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudentt',
            name='Gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=50, null=True),
        ),
    ]