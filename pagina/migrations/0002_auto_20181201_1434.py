# Generated by Django 2.0.9 on 2018-12-01 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='banco',
            new_name='Apellido_materno',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='comuna',
            new_name='Apellido_paterno',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='Banco',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombreusuario',
            new_name='Comuna_trabajo',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='papellido',
            new_name='Contraseña',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='direccion',
            new_name='Direccion',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='pnombre',
            new_name='Nombreusuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='rut',
            new_name='Rut',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='sapellido',
            new_name='Segundo_nombre',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='telefono',
            new_name='Telefono',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='snombre',
            new_name='primer_nombre',
        ),
    ]