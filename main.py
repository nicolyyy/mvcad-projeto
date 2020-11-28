import csv

from pessoa import insere_pessoa, retorna_pessoas, retorna_pessoa, atualiza_pessoa, remove_pessoa


def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')

        for pessoa in leitor:
            cpf = pessoa['cpf'].replace('.', '')
            pessoa['cpf'] = cpf.replace('-', '')
            insere_pessoa(pessoa)

# ler_arquivo()