from django.contrib import admin
from core.models import Treina_Facil,Assinar
#Treino_dificil,Treino_Forca,Treino_Forca_Resistencia,Treino_normal
# Register your models here.
class Facil(admin.ModelAdmin):
    list_display = ('id','Nome_do_treinamento','Exerc_1','Exerc_2','Exerc_3')

class Asir(admin.ModelAdmin):
    list_display = ('id','Nome','Treino','Cpf')
# class Normal(admin.ModelAdmin):
#     list_display = ('id','Nome_do_treinameto','Exerc_1','Exerc_2','Exerc_3','Exerc_4')
#
# class Dificil(admin.ModelAdmin):
#     list_display = ('id','Nome_do_treinamento','Exerc_1','Exerc_2','Exerc_3','Exerc_4','Exerc_5')
#
# class Forca(admin.ModelAdmin):
#     list_display = ('id','Nome_do_treinamento','Exerc_1','Exerc_2','Exerc_3')
#
# class Forca_resistencia(admin.ModelAdmin):
#     list_display = ('id','Nome_do_treinamento','Exerc_1','Exerc_2','Exerc_3')


admin.site.register(Treina_Facil,Facil)
admin.site.register(Assinar,Asir)
# admin.site.register(Treino_normal,Normal)
# admin.site.register(Treino_dificil,Dificil)
# admin.site.register(Treino_Forca,Forca)
# admin.site.register(Treino_Forca_Resistencia,Forca_resistencia)
