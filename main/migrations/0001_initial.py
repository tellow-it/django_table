# Generated by Django 4.0.4 on 2022-04-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('numbers', models.PositiveIntegerField(default=0)),
                ('distance', models.PositiveIntegerField(default=0)),
                ('data', models.DateTimeField()),
            ],
        ),
    ]
