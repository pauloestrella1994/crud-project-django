# Generated by Django 2.2.12 on 2020-04-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('edition', models.PositiveIntegerField()),
                ('publication_year', models.DateField()),
                ('authors', models.CharField(max_length=100)),
            ],
        ),
    ]
