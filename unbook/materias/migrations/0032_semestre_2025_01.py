# Generated by Django 5.0.7 on 2024-08-06 14:47

from django.db import migrations
import os 


def add_2024_2(apps, schema_editor):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    Turma = apps.get_model('materias', 'Turma')
    Materia = apps.get_model('materias', "Materia")
    Professor = apps.get_model('materias',"Professor")
    Info = apps.get_model('materias', "Info_semestre")

    #adiciona materias novas
    with open('arquivos_txt/2025_01/materias_2025_01.txt', 'r', encoding='utf-8') as fp: 
        linha = fp.readline().split('$')
        while len(linha)>1:
            print(linha)
            if not Materia.objects.filter(codigo=linha[0]).exists():
                print(f'criei matéria: {linha[0]}/{linha[1][1:-1]}')
                Materia.objects.create(codigo=linha[0], nome=linha[1][1:-1])
            linha = fp.readline().split('$')
    print('-='*25)
    
    # adiciona professores novos  
    with open('arquivos_txt/2025_01/professor_2025_01.txt', 'r', encoding='utf-8') as fp:
        linha = fp.readline().split('$')
        while len(linha)>1:
            if not Professor.objects.filter(nome=linha[0]).exists():
                print(f'criei professor: {linha[0]}')
                Professor.objects.create(nome=linha[0], foto=linha[1])
            linha = fp.readline().split('$')
    print('-='*25)
    

class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0031_rename_texto_feedback_texto_and_more'),
    ]

    operations = [
        migrations.RunPython(add_2024_2)
    ]
