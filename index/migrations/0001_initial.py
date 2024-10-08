# Generated by Django 4.2 on 2023-11-18 13:33

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import index.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigCity',
            fields=[
                ('Code', models.IntegerField(default=5904665, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('nPopulation', models.IntegerField(default=0)),
                ('nHousehold', models.IntegerField(default=0)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('Code', models.IntegerField(default=5454346, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('nPopulation', models.IntegerField(default=0)),
                ('nHousehold', models.IntegerField(default=0)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
                ('BigCity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.bigcity')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('Code', models.IntegerField(default=3807039, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Family', models.CharField(max_length=100)),
                ('SirName', models.CharField(max_length=100)),
                ('NaCode', models.CharField(blank=True, max_length=10, null=True)),
                ('Phone', models.CharField(max_length=11)),
                ('Character', models.ImageField(choices=[(1, 'Main Admin'), (2, 'Trustee'), (3, 'Responsible')], default=1, upload_to='')),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('Code', models.IntegerField(default=index.models.randIntAnything, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('Code', models.IntegerField(default=2483452, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('isEconomic', models.BooleanField(default=False)),
                ('nHousehold', models.IntegerField(default=0)),
                ('Description', models.TextField(max_length=2000)),
                ('CityCode', models.IntegerField(default=0)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
            ],
        ),
        migrations.CreateModel(
            name='SubProperty',
            fields=[
                ('Code', models.IntegerField(default=index.models.randIntAnything, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
                ('Property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyBelongPlace',
            fields=[
                ('Code', models.IntegerField(default=index.models.randIntAnything, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=2000)),
                ('Image', models.ImageField(blank=True, null=True, upload_to=index.models.uploadToPropertyBelongPlace)),
                ('PlaceCode', models.IntegerField(default=0)),
                ('SubProperty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.subproperty')),
            ],
        ),
        migrations.CreateModel(
            name='PeopleBelongVillage',
            fields=[
                ('Code', models.IntegerField(default=2740245, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('Family', models.CharField(max_length=150)),
                ('Proper', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=1500)),
                ('Village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.village')),
            ],
        ),
        migrations.CreateModel(
            name='CityPart',
            fields=[
                ('Code', models.IntegerField(default=8037019, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.city')),
            ],
        ),
        migrations.CreateModel(
            name='BigVillage',
            fields=[
                ('Code', models.IntegerField(default=4748165, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('RegisterTime', django_jalali.db.models.jDateTimeField(default=index.models.currentDateTime)),
                ('CityPart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.citypart')),
            ],
        ),
    ]
