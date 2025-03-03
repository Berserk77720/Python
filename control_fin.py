import pandas as pd

def main():
    print("=== Cadastro de Receitas ===")
    trabalho = float(input("Valor recebido do trabalho: R$ "))
    prestacao = float(input("Valor recebido de prestação de serviços: R$ "))

    print("\n=== Cadastro de Despesas (digite 0.00 se não houver gasto) ===")
    uber = float(input("Uber: R$ "))
    pop99 = float(input("99POP: R$ "))
    cartao_terceiros = float(input("Compras no cartão de crédito de terceiros: R$ "))
    cartao_pessoal = float(input("Cartão de crédito pessoal: R$ "))
    agua = float(input("Água: R$ "))
    luz = float(input("Luz: R$ "))
    telefone = float(input("Telefone Móvel: R$ "))
    internet = float(input("Internet: R$ "))
    gas = float(input("Gás de cozinha: R$ "))
    compras_comida = float(input("Compras comida: R$ "))

    # Cálculos
    total_recebido = trabalho + prestacao
    total_gastos = uber + pop99 + cartao_terceiros + cartao_pessoal + agua + luz + telefone + internet + gas + compras_comida
    saldo = total_recebido - total_gastos

    # Organizando os dados para a planilha
    dados = {
        "Descrição": [
            "Valor Recebido (Trabalho)",
            "Valor Recebido (Prestação de Serviços)",
            "Total Recebido",
            "Uber",
            "99POP",
            "Compras no cartão de terceiros",
            "Cartão de crédito pessoal",
            "Água",
            "Luz",
            "Telefone Móvel",
            "Internet",
            "Gás de cozinha",
            "Compras comida",
            "Total Gastos",
            "Saldo"
        ],
        "Valor (R$)": [
            trabalho,
            prestacao,
            total_recebido,
            uber,
            pop99,
            cartao_terceiros,
            cartao_pessoal,
            agua,
            luz,
            telefone,
            internet,
            gas,
            compras_comida,
            total_gastos,
            saldo
        ]
    }

    df = pd.DataFrame(dados)

    # Gerando a planilha Excel
    arquivo_excel = "controle_financeiro.xlsx"
    df.to_excel(arquivo_excel, index=False)
    print(f"\nPlanilha gerada com sucesso: {arquivo_excel}")

if __name__ == "__main__":
    main()
