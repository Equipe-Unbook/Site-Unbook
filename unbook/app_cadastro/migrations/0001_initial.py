<<<<<<< HEAD
# Generated by Django 5.0.4 on 2024-05-06 14:44
=======
# Generated by Django 5.0.4 on 2024-05-04 20:18
>>>>>>> 098859d47ef34f5d02a0d1fbb6c0a66ccd05f8c4

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=22)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
    ]
