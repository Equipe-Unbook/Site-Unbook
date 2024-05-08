from django.db import models

# Create your models here.

class ProfessorManager(models.Manager):
    def pesquisa(self, termo_busca):
        encontrado = []
        for obj in super().get_queryset():
            lista_nome = obj.nome.split()
            for nome in lista_nome:
                index =obj.nome.index(nome)
                if obj.nome[index:index+len(termo_busca)] == termo_busca:
                    encontrado.append(obj)
                    break
            
        return encontrado

class Professor(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    foto = models.URLField()
    objects = ProfessorManager()
                    
    def __str__(self):
        return self.nome




class Materia(models.Model):
    codigo = models.CharField(max_length=9, primary_key=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=10)
    objects = MateriaManager()
    def __str__(self):
        return self.codigo + " " + self.nome
    


class Comentario(models.Model):
    autor_nick = models.CharField(max_length=100)
    autor_email = models.EmailField()
    hora_publicacao = models.TimeField()
    texto = models.CharField(max_length=250)
    curtidas = models.IntegerField()

class Turma(models.Model):
    professor = models.ForeignKey("Professor", on_delete=models.CASCADE)
    materia = models.ForeignKey("Materia", on_delete=models.CASCADE)
    # comentario = models.ForeignKey(Comentario)
    avaliação_1 = models.FloatField()
    avaliação_2 = models.FloatField()
    avaliação_3 = models.FloatField()
    def __str__(self):
        return self.materia.codigo + "/" + self.professor.nome



