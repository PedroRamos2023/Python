from datetime import datetime, timedelta

class PessoaFisica:
    def __init__(self, nome, cpf, data_admissao, salario_medio):
        self.nome = nome
        self.cpf = cpf
        self.data_admissao = data_admissao
        self.salario_medio = salario_medio

class PessoaJuridica:
    def __init__(self, nome_fantasia, cnpj, data_criacao, faturamento_medio):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.data_criacao = data_criacao
        self.faturamento_medio = faturamento_medio

def main():
    tipo_pessoa = input("Digite 'PF' para pessoa física ou 'PJ' para pessoa pessoa jurídica: ")

    if tipo_pessoa == 'PF':
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_admissao = input("Data de admissão na empresa (DD-MM-AAAA): ")
        salario_medio = float(input("Salário médio dos últimos 3 meses: "))

        data_admissao = datetime.strptime(data_admissao, "%d-%m-%Y")
        tres_meses_antes = datetime.now() - timedelta(days=90)
    
        if data_admissao < tres_meses_antes:
            pessoa = PessoaFisica(nome, cpf, data_admissao, salario_medio)
            limite_cartao = pessoa.salario_medio * 0.4
            status_credito = "Liberado"
        else:
            limite_cartao = 0
            status_credito = "Aguardando nova análise em 3 meses."
    elif tipo_pessoa == 'PJ':
        nome_fantasia = input("Nome fantasia: ")
        cnpj = input("CNPJ: ")
        data_criacao = input("Data de criação da empresa (DD-MM-AAAA): ")
        faturamento_medio = float(input("Faturamento líquido médio dos últimos 3 meses: "))

        data_criacao = datetime.strptime(data_criacao, "%d-%m-%Y")
        quinze_meses_antes = datetime.now() - timedelta(days=450)

        if data_criacao < quinze_meses_antes:
            pessoa = PessoaJuridica(nome_fantasia, cnpj, data_criacao, faturamento_medio)
            limite_cartao = pessoa.faturamento_medio * 0.4
            status_credito = "Liberado"
        else:
            limite_cartao = 0
            status_credito = "Aguardando nova análise em 15 meses"
    else:
        print("Tipo de pessoa inválido.")
        return

    print("\nDados da pessoa:")
    if tipo_pessoa == 'PF':
        print(f"Nome: {pessoa.nome}")
        print(f"CPF: {pessoa.cpf}")
        print(f"Data de admissão na empresa: {pessoa.data_admissao}")
        print(f"Salário médio dos últimos 3 meses: R${pessoa.salario_medio:.2f}")
    elif tipo_pessoa == 'PJ':
        print(f"Nome fantasia: {pessoa.nome_fantasia}")
        print(f"CNPJ: {pessoa.cnpj}")
        print(f"Data de criação da empresa: {pessoa.data_criacao}")
        print(f"Faturamento líquido médio dos últimos 3 meses: R${pessoa.faturamento_medio:.2f}")

    print("\nAnálise de crédito:")
    print(f"Status do cartão de crédito: {status_credito}")
    if limite_cartao > 0:
        print(f"Limite do cartão de crédito: R${limite_cartao:.2f}")
if __name__ == "__main__":
    main()