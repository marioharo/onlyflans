# Generated by Django 5.0.6 on 2024-07-02 19:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_flan_title_flan_flan_uuid_flan_is_private_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_form_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('customen_email', models.EmailField(max_length=254)),
                ('customer_name', models.CharField(max_length=64)),
                ('customer_lastname', models.CharField(max_length=64)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Formcontacto',
        ),
        migrations.AlterField(
            model_name='flan',
            name='flan_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='flan',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='flan',
            name='nombre',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
