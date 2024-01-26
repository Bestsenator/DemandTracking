# Generated by Django 4.2 on 2024-01-06 15:37

from django.db import migrations, models
import django_jalali.db.models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_character_alter_bigcity_code_alter_bigvillage_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIKEY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApiKey', models.TextField(default=index.models.sesProduction)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
            ],
        ),
        migrations.AlterField(
            model_name='bigcity',
            name='Code',
            field=models.IntegerField(default=5974889, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bigvillage',
            name='Code',
            field=models.IntegerField(default=7506114, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='Code',
            field=models.IntegerField(default=7302236, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='city',
            name='Code',
            field=models.IntegerField(default=5945152, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='citypart',
            name='Code',
            field=models.IntegerField(default=7898158, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='manager',
            name='Code',
            field=models.IntegerField(default=7188363, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='peoplebelonglocation',
            name='Code',
            field=models.IntegerField(default=2947408, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='village',
            name='Code',
            field=models.IntegerField(default=2734904, primary_key=True, serialize=False),
        ),
    ]
