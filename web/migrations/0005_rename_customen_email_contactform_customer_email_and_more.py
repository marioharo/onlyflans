# Generated by Django 5.0.6 on 2024-07-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_contactform_delete_formcontacto_alter_flan_flan_uuid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='customen_email',
            new_name='customer_email',
        ),
        migrations.AlterField(
            model_name='flan',
            name='flan_uuid',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='flan',
            name='is_private',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='flan',
            name='nombre',
            field=models.CharField(default='nombre', max_length=64),
        ),
    ]
