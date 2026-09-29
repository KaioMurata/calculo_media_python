# Calculadora de Média
 Codigo em python para calcular a média de um aluno e verificar se ele esta aprovado ou nao

---
### Tecnologia Utilizada:
> Python v3.11.9
---
### Executar:
#### Uma IDE de sua preferência 
---
### Codigo:
```
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
```
---
### Autor e Contato:
>Kaio Matteucci Murata <br>
>kaio.murata@hotmail.com <br>
>[Acesse meu portfólio ](https://github.com/KaioMurata)