# Generated by Django 4.2 on 2024-01-20 08:19

from django.db import migrations, models
import django_jalali.db.models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_alter_bigcity_code_alter_bigvillage_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answertoproperty',
            name='RegisterTime',
            field=django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime),
        ),
        migrations.AlterField(
            model_name='answertoproperty',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to=index.models.uploadToAnswerProperty),
        ),
    ]
