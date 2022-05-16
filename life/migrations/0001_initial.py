# Generated by Django 3.2.4 on 2022-02-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('date_time', models.DateTimeField()),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]