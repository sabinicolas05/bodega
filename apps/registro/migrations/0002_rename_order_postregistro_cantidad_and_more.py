# Generated by Django 5.1 on 2024-09-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postregistro',
            old_name='order',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='postregistro',
            old_name='descriptions',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='postregistro',
            old_name='created_at',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='postregistro',
            old_name='title',
            new_name='nombre',
        ),
    ]
