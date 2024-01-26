# Generated by Django 4.2 on 2024-01-20 20:44

from django.db import migrations, models
import django.db.models.deletion
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0023_answertoproperty_registertime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('Code', models.IntegerField(default=index.models.randIntAnything, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AccessCharacter',
            fields=[
                ('Code', models.IntegerField(default=index.models.randIntAnything, primary_key=True, serialize=False)),
                ('Character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.character')),
                ('Section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.section')),
            ],
        ),
    ]
