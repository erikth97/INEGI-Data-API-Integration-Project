# Generated by Django 5.1.2 on 2024-10-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_inegi', '0003_alter_asentamiento_options_alter_localidad_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asentamiento',
            name='cve_asen',
            field=models.CharField(db_index=True, default='0000', max_length=4),
        ),
        migrations.AlterField(
            model_name='estado',
            name='cve_ent',
            field=models.CharField(db_index=True, default='00', max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='cve_loc',
            field=models.CharField(db_index=True, default='0000', max_length=4),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='cve_mun',
            field=models.CharField(db_index=True, default='0000', max_length=4),
        ),
    ]