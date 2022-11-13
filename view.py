from banco import *


#CRUD
# Inserir informacoes
def inserir_info(i):
    with cnx:
        cnx.reconnect()
        cur = cnx.cursor()
        query = "INSERT INTO tb_cliente (nome_cliente, dta_nasc_cliente, telefone_cliente, cod_cidade) VALUES (%s, %s, %s, %s)"
        cur.execute(query, i)
        cnx.commit()
        cur.close()
        cnx.close()


# Mostrar informacoes
def mostrar_info():
    lista = []
    with cnx:
        cnx.reconnect()
        cur = cnx.cursor()
        query = "SELECT id_cliente, nome_cliente, dta_nasc_cliente, telefone_cliente, nome_cidade " \
                "FROM tb_cliente JOIN tb_cidade ON id_cidade=cod_cidade"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)

        cur.close()
        cnx.close()
    return lista





# Atualizar informacoes
def atualizar_info(i):
    with cnx:
        cnx.reconnect()
        cur = cnx.cursor()
        query = "UPDATE tb_cliente SET nome_cliente=%s, dta_nasc_cliente=%s, telefone_cliente=%s, cod_cidade=%s WHERE id_cliente=%s"
        cur.execute(query, i)
        cnx.commit()
        cur.close()
        cnx.close()



# Deletar informacoes
def deletar_info(i):
    with cnx:
        cnx.reconnect()
        cur = cnx.cursor()
        query = "DELETE FROM tb_cliente WHERE id_cliente=%s"
        cur.execute(query, i)
        cur.close()
        cnx.close()


def mostrar_cidade():
    lista = []
    with cnx:
        cnx.reconnect()
        cur = cnx.cursor()
        query = "SELECT nome_cidade FROM tb_cidade"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)

        cur.close()
        cnx.close()
    return lista
