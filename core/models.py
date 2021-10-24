from django.db import models
from datetime import date

class PeopleManager(models.Manager):
    def alphabetical(self):
        return self.model.objects.order_by('nome')

    def younger(self, n):
        return self.model.objects.order_by('-data_nasc')[:n]

    def older(self, n):
        return self.model.objects.order_by('data_nasc')[:n]

    def mans(self):
        return self.model.objects.filter(sexo = 'M').count()

    def womans(self):
        return self.model.objects.filter(sexo = 'F').count()

    def search_name(self, name):
        values = self.model.objects.filter(nome__istartswith = name).values()
        if bool(values) == False:
            return f'Nenhum nome foi encontrado na tabela. Tente novamente!'
        return values

    def to_json(self, people_name):
        people = list(self.model.objects.filter(nome = people_name). values())
        if bool(people) == False:
            return f'Nome incompleto ou inexistente na tabela. Digite corretamente!' 
        return people

class People(models.Model):

    GENDER_CHOICES = [
        ("F", "Feminino"),
        ("M", "Masculino"),
    ]

    nome = models.CharField(max_length=150, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=14, verbose_name= 'CPF')
    rg = models.CharField(max_length=15, verbose_name= 'RG')
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mae = models.CharField(max_length=150, verbose_name= 'Nome da Mãe')
    pai = models.CharField(max_length=150, verbose_name= 'Nome do Pai')
    celular = models.CharField(max_length=150)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.PositiveIntegerField()
    tipo_sanguineo = models.CharField(max_length=10, verbose_name="Tipo Sanguíneo")
    endereco = models.CharField(max_length=100, null=True, verbose_name='Endereço')
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)
    cep = models.CharField(max_length=100, null=True, verbose_name = 'CEP')
    pais = models.CharField(max_length=100, null=True, verbose_name = "País" )

    objects = PeopleManager()

    def __str__(self):
        return self.nome