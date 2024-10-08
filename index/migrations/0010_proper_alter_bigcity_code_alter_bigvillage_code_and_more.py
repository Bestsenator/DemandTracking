# Generated by Django 4.2 on 2023-12-12 04:39

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_alter_bigcity_code_alter_bigvillage_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proper',
            fields=[
                ('Code', models.IntegerField(default=2432321, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
            ],
        ),
        migrations.AlterField(
            model_name='bigcity',
            name='Code',
            field=models.IntegerField(default=5905971, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bigvillage',
            name='Code',
            field=models.IntegerField(default=2925599, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='city',
            name='Code',
            field=models.IntegerField(default=5927346, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='citypart',
            name='Code',
            field=models.IntegerField(default=8173039, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='manager',
            name='Code',
            field=models.IntegerField(default=5216731, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='peoplebelongvillage',
            name='Code',
            field=models.IntegerField(default=2907534, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='village',
            name='Code',
            field=models.IntegerField(default=2981539, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='AnswerToProperty',
            fields=[
                ('Code', models.IntegerField(default=index.models.randIntAnything, primary_key=True, serialize=False)),
                ('Content', models.TextField(max_length=2000)),
                ('File', models.FileField(blank=True, null=True, upload_to=0)),
                ('Manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.manager')),
                ('PropertyBelongPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.propertybelongplace')),
            ],
        ),
        migrations.AlterField(
            model_name='peoplebelongvillage',
            name='Proper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.proper'),
        ),
    ]
