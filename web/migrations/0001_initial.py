# Generated by Django 5.0.6 on 2024-06-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
