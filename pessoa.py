from connection import cursor


def insere_pessoa(dados_pessoa):

    cursor.execute("INSERT INTO pessoa (nome, endereco, cpf, estado,"
                   "turma, periodo, modulo)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (
                       dados_pessoa['nome'],
                       dados_pessoa['endereco'],
                       dados_pessoa['cpf'],
                       dados_pessoa['uf'],
                       dados_pessoa['turma'],
                       dados_pessoa['periodo'],
                       dados_pessoa['modulo']
                   )
                   )


def retorna_pessoas():
    cursor.execute("SELECT * FROM pessoa")
    return cursor.fetchall()


def retorna_pessoa(id):


    cursor.execute("SELECT * FROM pessoa WHERE id = %s", [id])
    pessoa = cursor.fetchone()
    return pessoa


def atualiza_pessoa(pessoa):
    query = "UPDATE pessoa SET nome = %s, endereco = %s, estado = %s, periodo %s, modulo = %s" \
            "WHERE id = %s"

    params = [pessoa['nome'], pessoa['endereco'], pessoa['cpf'], pessoa['estado'], pessoa['estado'], pessoa['turma'], pessoa['periodo'],
              pessoa['modulo'], pessoa['id']]

    cursor.execute(query, params)


def remove_pessoa(id):
    cursor.excute("DELETE FROM pessoa id = %s", [id])
