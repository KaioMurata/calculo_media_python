def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

print("=== Sistema de Notas do Aluno ===")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = calcular_media(nota1, nota2)
print(f"A média do aluno é: {media:.2f}")

if media >= 7.0:
    print("Status: Aprovado")
else:
    print("Status: Reprovado")