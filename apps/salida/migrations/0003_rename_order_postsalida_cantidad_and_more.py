# Generated by Django 5.1 on 2024-09-20 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salida', '0002_alter_postsalida_descriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postsalida',
            old_name='order',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='postsalida',
            old_name='descriptions',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='postsalida',
            old_name='created_at',
            new_name='fecha_salida',
        ),
        migrations.RenameField(
            model_name='postsalida',
            old_name='title',
            new_name='nombre',
        ),
    ]
