# Generated by Django 5.0.6 on 2024-06-24 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_comentario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-created'], 'verbose_name': 'Comentatrio', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='comnet',
            new_name='coment',
        ),
    ]
