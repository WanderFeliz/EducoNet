# Generated by Django 3.2 on 2021-06-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='TYPE',
            field=models.CharField(choices=[('other', 'Variado'), ('products', 'Oferta educativa'), ('library', 'Biblioteca'), ('institute', 'Institución'), ('community', 'Comunidad')], default='other', max_length=20, null=True, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('draft', 'Nuevo'), ('available', 'Disponible'), ('cancel', 'Deshabilitado')], default='draft', max_length=20, verbose_name='Estado'),
        ),
    ]
