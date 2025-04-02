from django.db import models

class Operadora(models.Model):
    registro_ans = models.CharField(max_length=20, primary_key=True)
    cnpj = models.CharField(max_length=20)
    razao_social = models.TextField()
    nome_fantasia = models.TextField(null=True, blank=True)
    modalidade = models.CharField(max_length=100)
    logradouro = models.TextField(null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    complemento = models.TextField(null=True, blank=True)
    bairro = models.TextField(null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    ddd = models.CharField(max_length=5, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    endereco_eletronico = models.TextField(null=True, blank=True)
    representante = models.TextField(null=True, blank=True)
    cargo_representante = models.TextField(null=True, blank=True)
    regiao_de_comercializacao = models.IntegerField(null=True, blank=True)
    data_registro_ans = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'operadoras'
    
    def __str__(self):
        return self.razao_social