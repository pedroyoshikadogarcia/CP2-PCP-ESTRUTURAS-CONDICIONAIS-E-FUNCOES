def encontrar_menor(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3

cp1 = float(input("Nota do Checkpoint 1: "))
cp2 = float(input("Nota do Checkpoint 2: "))
cp3 = float(input("Nota do Checkpoint 3: "))
sp1 = float(input("Nota da Sprint 1: "))
sp2 = float(input("Nota da Sprint 2: "))
gs = float(input("Nota da Global Solution: "))

menor_cp = encontrar_menor(cp1, cp2, cp3)

media = ((cp1 + cp2 + cp3 - menor_cp + sp1 + sp2) / 4) * 0.4 + (gs * 0.6)

media_peso = media * 0.4

print(f"Menor Checkpoint desconsiderado: {menor_cp:.1f}")
print(f"Média do Semestre: {media:.1f}")
print(f"Média com Peso (40%): {media_peso:.1f}")