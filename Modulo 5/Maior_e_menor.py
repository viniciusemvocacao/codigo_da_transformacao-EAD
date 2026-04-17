lista = [3, 7, 2, 9, 5]
print(f"A lista de números é: {lista}")

def maior_e_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

maior, menor = maior_e_menor(lista)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")