def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = calcular_media(nota1, nota2, nota3)
print(f"A média do aluno é: {media}")
if media >= 6:
    print("Aluno aprovado!")
else:   
    print("Aluno reprovado!")