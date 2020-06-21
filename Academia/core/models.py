from django.db import models


# Create your models here.

class Treina_Facil(models.Model):
    Nome_do_treinamento = models.CharField(max_length=50)
    Exerc_1 = models.CharField(max_length=50)
    Exerc_2 = models.CharField(max_length=50)
    Exerc_3 = models.CharField(max_length=50)

    class Meta:
        db_table= 'treinamento facil'
    def __repr__(self):
        return self.Nome_do_treinamento

class Assinar(models.Model):
    Nome = models.CharField(max_length=100)
    Treino = models.CharField(max_length=250)
    Quant = models.IntegerField()
    Cpf = models.IntegerField()
    Preco= models.IntegerField()

    class Meta():
        db_table = 'Assinar'
    def __repr__(self):
        return self.Nome

# class Treino_normal(models.Model):
#     Nome_do_treinameto= models.CharField(max_length=50)
#     Exerc_1 = models.CharField(max_length=50)
#     Exerc_2 = models.CharField(max_length=50)
#     Exerc_3 = models.CharField(max_length=50)
#     Exerc_4 = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'Treinamento normal'
#     def __repr__(self):
#         return self.Nome_do_treinameto
#
# class Treino_dificil(models.Model):
#     Nome_do_treinamento = models.CharField(max_length=50)
#     Exerc_1 = models.CharField(max_length=50)
#     Exerc_2 = models.CharField(max_length=50)
#     Exerc_3= models.CharField(max_length=50)
#     Exerc_4= models.CharField(max_length=50)
#     Exerc_5= models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'treinamento dificil'
#
#     def __repr__(self):
#         return self.Nome_do_treinamento
#
# class Treino_Forca(models.Model):
#     Nome_do_treinamento = models.CharField(max_length=100)
#     Exerc_1 = models.CharField(max_length=50)
#     Exerc_2 = models.CharField(max_length=50)
#     Exerc_3 = models.CharField(max_length=50)
#     Exerc_4 = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'treinamento de força'
#
#     def __repr__(self):
#         return self.Nome_do_treinamento
#
#
# class Treino_Forca_Resistencia(models.Model):
#     Nome_do_treinamento = models.CharField(max_length=100)
#     Exerc_1 = models.CharField(max_length=50)
#     Exerc_2 = models.CharField(max_length=50)
#     Exerc_3 = models.CharField(max_length=50)
#     Exerc_4 = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'treinamento de força e resistencia'
#
#     def __repr__(self):
#         return self.Nome_do_treinamento