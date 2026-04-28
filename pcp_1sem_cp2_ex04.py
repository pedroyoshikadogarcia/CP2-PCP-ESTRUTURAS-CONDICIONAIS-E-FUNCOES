def calcular_horas_extras(salario_base, horas):
    valor_total_he = salario_base * 0.015 * horas
    return valor_total_he

def calcular_descontos_faltas(salario_base, faltas):
    valor_total_faltas = salario_base * 0.02 * faltas
    return valor_total_faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "s":
        if cargo == 1:
            return 1000.0
        elif cargo == 2:
            return 500.0
        elif cargo == 3:
            return 300.0
        elif cargo == 4:
            return 100.0
    return 0.0

nome = input("Nome do funcionario: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiario): "))
salario_base = float(input("Salário base: "))
horas_ex = float(input("Total de horas extras: "))
faltas = int(input("Total de faltas no mês: "))
recebeu_b = input("Recebeu bônus por desempenho? (s/n): ").lower()

adicional_he = calcular_horas_extras(salario_base, horas_ex)
desconto_faltas = calcular_descontos_faltas(salario_base, faltas)
bonus_valor = calcular_bonus(cargo, recebeu_b)

acrescimos = adicional_he + bonus_valor
salario_bruto = salario_base + adicional_he + bonus_valor
salario_final = salario_bruto - desconto_faltas

print(f"\n--- Holerite: {nome} ---")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Total de Acréscimos (HE + Bônus): R$ {acrescimos:.2f}")
print(f"Total de Descontos (Faltas): R$ {desconto_faltas:.2f}")
print(f"Salário Final: R$ {salario_final:.2f}")