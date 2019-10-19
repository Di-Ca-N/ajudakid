from django.db import models


class Endereco(models.Model):
	pais = models.CharField(max_length=50, default="Brasil")
	estado = models.CharField(
		max_length=2, 
		choices=(
			("AC", "AC"),
			("CE", "CE"),
			("DF", "DF"),
			("TO", "TO"),
			("RS", "RS"),
			("SC", "SC"),
			("PR", "PR"),
			("PA", "PA"),
			("RO", "RO"),
			("RR", "RR"),
			("SE", "SE"),
			("PE", "PE"),
			("MT", "MT"),
			("MS", "MS"),
			("BA", "BA"),
			("RN", "RN"),
			("AM", "AM"),
			("SP", "SP"),
			("RJ", "RJ"),
			("MG", "MG"),
			("ES", "ES"),
			("GO", "GO"),
			("AL", "AL"),
			("AP", "AP"),
			("MA", "MA"),
			("PI", "PI"),
		)
	)
	cidade = models.CharField(max_length=100)
	bairro = models.CharField(max_length=100)
	rua = models.CharField(max_length=300)
	numero = models.CharField(max_length=10)
	complemento = models.CharField(max_length=50, blank=True)
