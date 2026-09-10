print(type("Giulia")) # O tipo de dado é <class 'str'>
print(type(26)) # O tipo de dado é <class 'int'>
print(type(3.14)) # O tipo de dado é <class 'float'>
print(type(3.1)) # O tipo de dado é <class 'float'>
print(type(True)) # O tipo de dado é <class 'bool'>
print(type(False)) # O tipo de dado é <class 'bool'>

nome = "Giulia" # = Atribuição de valor a variável nome
idade = 26 # = Atribuição de valor a variável idade
print(nome) # = Exibe o valor da variável nome
print(idade) # = Exibe o valor da variável idade

print("Meu nome é", nome, "e minha idade é", idade) # = Exibe uma frase concatenando texto e variáveis
print(f"Meu nome é {nome} e minha idade é {idade}") # = Exibe uma frase utilizando f-string para concatenar texto e variáveis

# Operadores aritméticos

print(10 + 5) # = Soma
print(10 - 5) # = Subtração 
print(10 * 5) # = Multiplicação
print(10 / 2) # = Divisão
print(10 // 2) # = Divisão inteira
print(10 ** 2) # = Potência
print(10 % 2) # = Resto da divisão

# Operadores de atribuição
a = 2
b = 4
c = 6
d = 8
e = 10
f = 12

a += 5 # a = a + 5 -> a = 2 + 5 = 7
b -= 3 # b = b - 3 -> b = 4 - 3 = 1
c *= 2 # c = c * 2 -> c = 6 * 2 = 12
d /= 4 # d = d / 4 -> d = 8 / 4 = 2.0
e //= 5 # e = e // 5 -> e = 10 // 5 = 2
f %= 3 # f = f % 3 -> f = 12 % 3 = 0

# Operadores de comparação

print( 5 == 5) # = Igualdade | operador == compara se os valores são iguais
print( 5 != 5) # = Diferença | operador != compara se os valores são diferentes
print( 5 > 3) # = Maior que | operador > compara se o primeiro valor é maior que o segundo
print( 5 < 3) # = Menor que | operador < compara se o primeiro valor é menor que o segundo
print( 5 >= 5) # = Maior ou igual a | operador >= compara se o primeiro valor é maior ou igual ao segundo
print( 5 <= 3) # = Menor ou igual a | operador <= compara se o primeiro valor é menor ou igual ao segundo

# Operadores lógicos

print(5 > 3 and 5 < 10) # = E | operador and retorna True se ambas as condições forem verdadeiras
print(5 > 3 or 5 < 10)  # = OU | operador or retorna True se pelo menos uma das condições for verdadeira
print(not (5 > 3))      # = NÃO | operador not retorna True se a condição for falsa

