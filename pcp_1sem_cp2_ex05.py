def pode_aprovar(idade, renda, valor):
    if idade >= 18 and valor <= (renda * 20):
        return True
    else:
        return False

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    numerador = taxa * (1 + taxa)**parcelas
    denominador = (1 + taxa)**parcelas - 1
    pmt = valor * (numerador / denominador)
    return pmt

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

nome = input("Nome do cliente: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))
valor_emp = float(input("Valor do emprestimo: "))
n_parcelas = int(input("Número de parcelas (3 a 24): "))

if pode_aprovar(idade, renda, valor_emp):
    taxa = definir_taxa(n_parcelas)
    valor_parcela = calcular_parcela(valor_emp, taxa, n_parcelas)
    valor_total = calcular_total(valor_parcela, n_parcelas)
    total_juros = calcular_juros(valor_total, valor_emp)

    print(f"\n Empréstimo Aprovado para {nome}")
    print(f"Valor Financiado: R$ {valor_emp:.2f}")
    print(f"Taxa de Juros: {taxa * 100:.0f}% ao mês")
    print(f"Valor da Parcela ({n_parcelas}x): R$ {valor_parcela:.2f}")
    print(f"Valor Total Pago ao final: R$ {valor_total:.2f}")
    print(f"Total de Juros Pagos: R$ {total_juros:.2f}")
else:
    print(f"\n Empréstimo Negado para {nome}. Não atende aos requisitos de idade ou renda.")