# Generated by Django 5.0.4 on 2024-06-07 18:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0018_comentario_deletado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='denuncia',
            field=models.ManyToManyField(related_name='denuncia_comentario', to=settings.AUTH_USER_MODEL),
        ),
    ]
