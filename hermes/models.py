from django.db import models

# Create your models here.
class Atividade(models.Model):
    nome = models.CharField()
    descricao = models.TextField()

class Colaborador(models.Model):
    nome = models.TextField()
    uf = models.CharField(max_length=2)
    cep = models.CharField()
    email = models.CharField()
    telefone = models.CharField()
    cargo = models.CharField()
    setor = models.CharField()
    turno = models.CharField()
    cpf = models.CharField()

class Calendario(models.Model):
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    descricao = models.TextField()
    titulo = models.TextField()
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

class Categoria(models.Model):
    nome = models.TextField()
    descricao = models.TextField()
    tipo = models.TextField()

class Produto(models.Model):
    nome = models.CharField()
    descricao = models.TextField()
    unidade = models.CharField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Fornecedor(models.Model):
    nome = models.CharField()
    cnpj = models.CharField()
    email_representante = models.CharField()
    telefone = models.CharField()
    endereco_matriz = models.CharField()

class Compras(models.Model):
    nota_fiscal = models.CharField()
    data_compra = models.DateField()
    preco_unitario = models.FloatField()
    valor_total = models.FloatField()
    status_compras = models.CharField()
    quantidade = models.IntegerField()
    data_entrega_prevista = models.DateField()
    data_entrega_real = models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

class Inventario(models.Model):
    quantidade = models.IntegerField()
    localizacao = models.CharField()
    lote = models.CharField()
    data_registrada = models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Movimentacao(models.Model):
    quantidade = models.IntegerField()
    tipo = models.CharField()
    lote = models.CharField()
    data_movimentacao = models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)

class Incidentes(models.Model):
    data_incidente = models.DateField()
    descricao = models.TextField()
    tipo = models.CharField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)