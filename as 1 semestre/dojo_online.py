""" 1. Contar números ímpares em uma lista
Crie uma algoritmo  que leia uma lista de números inteiros, de forma indeterminadas até ser inserir 0 e retorne a quantidade de números ímpares nela.

Exemplo de entrada:

[2, 3, 5, 8, 10]

Saída esperada:

Quantidade de ímpares: 2
 """
print("EXERCÍCIO 1\n")
impares = []
lista = []
while True:
    n = int(input("Digite o número da lista: "))
    lista.append(n)
    if n == 0:
        lista.pop()
        break
    if n % 2 != 0:
        impares.append(n)
print(f"Lista: {lista}")
print(f"Impares: {impares}")
print(f"Quantidade de ímpares: {len(impares)}")

""" 2. Separar pares e ímpares e ordená-los
Crie uma algoritmo  que leia uma lista de números inteiros, de forma indeterminadas até ser inserir 0 e separe os números pares e ímpares, ordene cada grupo em ordem crescente e imprima o resultado.

Exemplo de entrada:

[7, 2, 5, 8, 4]

Saída esperada:

Pares ordenados: [2, 4, 8]  

Ímpares ordenados: [5, 7]
"""
print("\nEXERCÍCIO 2")
pares = []
impares = []
while True:
    n = int(input("Digite o número da lista: "))
    if n == 0:
        break
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    pares.sort()
    impares.sort()
print(f"Pares: {pares}")
print(f"Impares: {impares}")

""" 3. Substituir palavras em uma string
Escreva um algoritmo que leia uma frase e substitua uma palavra específica por outra definida pelo usuário.

Exemplo de entrada:

frase = "Eu gosto de programar em Python."  

palavra_a_substituir = "Python"  

nova_palavra = "JavaScript"

Saída esperada:

Frase alterada: "Eu gosto de programar em JavaScript."

"""
print("\nEXERCÍCIO 3")
frase = input("Digite a frase: ")
substituir = input("Digite a palavra a substituir: ")
nova = input("Digite a nova palavra: ")
frase = frase.replace(substituir, nova)
print(f"Frase alterada: {frase}")

""" 4. Cálculo de venda de vários itens
Crie um programa que simule uma calculadora de vendas. O programa deve permitir ao usuário inserir o nome de um item, sua quantidade e preço unitário. O loop continua até que o usuário digite "sair". No final, exiba o total da venda.

Exemplo de interação:

Digite o nome do item (ou 'sair' para encerrar): maçã  

Quantidade: 3  

Preço unitário: 1.50  

Digite o nome do item (ou 'sair' para encerrar): banana  

Quantidade: 2  

Preço unitário: 0.75  

Digite o nome do item (ou 'sair' para encerrar): sair  

Total da venda: R$ 6.75
"""
print("\nEXERCÍCIO 4")
total_item = 0
total_venda = 0
while True:
    nome = input("Digite o nome do item (ou 'sair' para encerrar): ").lower()
    if nome == "sair":
        break
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço unitário: "))
    total_item = quantidade * preco
    total_venda += total_item
print(f"Total da venda: R${total_venda:.2f}")

""" 5. Inverter uma lista sem usar funções prontas
Crie um que receba uma lista de números e a inverta, sem usar funções prontas como reverse() ou fatiamento.

Exemplo de entrada:

[1, 2, 3, 4, 5]

Saída esperada:

Lista invertida: [5, 4, 3, 2, 1]
 """
print("\nEXERCÍCIO 5")
def inverter_lista(lista):
    inicio = 0
    fim = len(lista) - 1
        
    while inicio < fim:
        
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
            
        inicio += 1
        fim -= 1
        
    return lista

lista_original = []
for i in range(10):
    numero = int(input(f"Digite o {i+1} número da lista: "))
    lista_original.append(numero)
print(f"Lista original: {lista_original}")    
lista_invertida = inverter_lista(lista_original)
print(f"Lista invertida: {lista_invertida}")

""" 6. Contar vogais em uma string
Escreva um programa que conte a quantidade de cada vogal em uma frase fornecida pelo usuário e retorne com os resultados.

Exemplo de entrada:

"Programar é divertido"

Saída esperada:
a=2
e=1
i=2
0=2
u=1
 """
print("\nEXERCÍCIO 6")
def contar_vogais(frase):
    a = e = i = o = u = 0
    for letra in frase:
        if letra == "a": a+=1
        elif letra == "e": e+=1
        elif letra == "i": i+=1
        elif letra == "o": o+=1
        elif letra == "u": u+=1
    print(f"a={a}\ne={e}\ni={i}\no={o}\nu={u}")

contar_vogais(input("Digite uma frase: "))

""" 7. Remover duplicados de uma lista
Crie um algoritmo que receba uma lista com números repetidos e retorne uma nova lista apenas com números únicos, na ordem em que aparecem.

Exemplo de entrada:

[1, 2, 2, 3, 4, 4, 5]

Saída esperada:

[1, 2, 3, 4, 5] """
print("\nEXERCÍCIO 7")
lista = []
lista_corrigida = []
for i in range(7):
    n = int(input(f"Digite o {i+1} número da lista: "))
    lista.append(n)
    if n not in lista_corrigida:
        lista_corrigida.append(n)
    else:
        continue
print(f"Lista normal: {lista}")
print(f"Lista sem duplicados: {lista_corrigida}")
