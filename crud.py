import mysql.connector
from mysql.connector import errorcode


class BancoDeDados():
    def __init__(self):
        
        try:
            conexao = mysql.connector.connect(user='root',password='root',host='localhost',database='teste_conexao')

        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\n \n\n USUARIO OU SENHA INVALIDOS \n \n\n ")
            elif erro.errno == errorcode.ER_BAD_DB_ERROR:
                print(" \n \n\n BANCO DE DADOS NAO EXISTE \n \n\n ")
                
            else:
                print("\n \n\n", erro ,"\n \n\n")

        

        

        #chama a funcao que vai inserir os dados no banco de dados 
        #comando_ddl(conexao)
        #else:
            #fechar a conexao com o banco de dados 
            #conexao.close()

    def comando_ddl(conectar):
        #Cursor e uma estrutura de controle que permite percorer registros, alem de facilitar a adição e remoção de registros do banco de dados
        cursor = conectar.cursor()
        #Montando uma string com o comando insert usando uma tupla
        #insert_registro = ("insert into usuario (nome,telefone)" "values (%s,%s)")
        # criando os dados 
        #dados = ('Pedro','99542010')

        """
        # apagando registro
        remover_usuario = ("delete from usuario where cod_user = 3")
        cursor.execute(remover_usuario)
        """

        """
        #atualização de dados
        atualizar_contato = ("update usuario set nome = %s, telefone = %s where cod_user = 3")
        contato = ('shirley','99774746')
        cursor.execute(atualizar_contato,contato)
        """

        """
        #Montando o comando insert com as chaves do dicionario 
        inserir_contato =("insert into usuario (nome,telefone)"
                        "values (%(nome)s,%(telefone)s)")
        #Criando um dicionario com os dados a serem inseridos 
        contato = {'nome':'Cayque Mito',
                'telefone':'99562046'}
        cursor.execute(inserir_contato,contato)

        """
        # procurando registro na tabela
        consulta = ("select telefone from usuario")
        cursor.execute(consulta)
        #cria uma lista 
        lista = []
        for x in cursor:
            # atribui a ultima posição da lista 
            lista = lista+[x]
            #print("valor de x",x)
            # exibi oque a lista recebeu
            #print("recebimento da lista ",lista)
        # executa a lista 
        print(lista)
        # transfere uma posição da lista para uma funcao que lisba o valor por que ele vem com ('')
        valor_limpo = tratamento_do_banco(lista[0]) 

        print (" o numero do lucas e :",valor_limpo)

            
        """
        #executa a instrução que deseja 
        cursor.execute("select * from usuario")
        # monstra a instrução executada 
        for x in cursor:
            print(x)
        """

        """
        consulta = ("select nome,telefone from usuario")
        cursor.execute(consulta)
        ## imprimindo resultado da busca 
        for (nome,telefone) in cursor:
            print(f"Nome:{nome},telefone:{telefone}")

        """


        #executando o comando insert mais a tupla
        #cursor.execute(insert_registro,dados)
        print('registro inserido com sucesso')
        #Gravando a informação permanentemente
        conectar.commit()
        #fechando o cursos
        cursor.close()
        #fechando conexao 
        conectar.close()

    def tratamento_do_banco(nome):
        nome =(nome[-1])

        return nome 
    def criacao(self, conectar):
        cursor = conectar.cursor()
        criar_banco =("create database Criação_altomatizada")
