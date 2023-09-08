import os
import datetime

# Função para criar uma pasta com a data atual

def criar_pasta_com_data():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    data_atual = datetime.date.today()
    nome_pasta = data_atual.strftime("%Y-%m-%d")
    caminho_pasta = os.path.join(diretorio_atual, nome_pasta)

    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    return caminho_pasta

# Função para coletar dados do usuário

def coletar_dados_usuario():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    profissao = input("Digite sua profissão: ")
    frase_do_dia = input("Digite sua frase do dia: ")

    return nome, idade, profissao, frase_do_dia

# Função para criar um arquivo de relatório com os dados do usuário

def criar_relatorio(nome, idade, profissao, frase_do_dia):
    data_atual = datetime.date.today()
    nome_pasta = criar_pasta_com_data()
    nome_arquivo = f"{nome}.txt"
    caminho_arquivo = os.path.join(nome_pasta, nome_arquivo)

    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write(f"Relatório de Usuário\n")
        arquivo.write(f"Data: {data_atual}\n")
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Profissão: {profissao}\n")
        arquivo.write(f"Frase do dia: {frase_do_dia}\n")

def main():
    nome, idade, profissao, frase_do_dia = coletar_dados_usuario()
    criar_relatorio(nome, idade, profissao, frase_do_dia)
    print("Relatório criado com sucesso!")

if __name__ == "__main__":
    main()