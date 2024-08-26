# Generated by Django 5.1 on 2024-08-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cooking_time', models.IntegerField()),
                ('ingredients', models.TextField()),
                ('difficulty', models.IntegerField(default=None)),
            ],
        ),
    ]
