# Generated by Django 3.0.4 on 2020-05-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=850)),
                ('image', models.CharField(max_length=3000)),
                ('film_id', models.CharField(max_length=12)),
            ],
        ),
    ]