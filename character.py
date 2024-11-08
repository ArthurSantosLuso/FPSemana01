# Definir o array/lista para armazenar os personagens
character = [] 

# Ciclo que corre até o utilizador inserir 3 personagens
while len(character) < 3: 
    # Inserir o nome
    nome = input() 
    # Inserir o ataque
    atk = int(input()) 
    # Inserir a Defesa
    defesa = int(input()) 

    # stats = (atk, defesa) # Pode ser feito assim, criar uma variavel tuple

    # adicionar o personagem no array/lista
    character.append([nome, (atk, defesa)]) # ou poderia ser feito 'character.append([nome, stats])'

# Imprimir todos os personagens
print(character)  

# A função max() procura o maior dentro de um array/lista, aqui é dado um parametro 'key=lambda x: x[1][0]'
# basicamente o x[1] faz com que a função procure pelo tuple de cada personagem, que estão do index 1~
# e depois o x[1][0] procura o valor de ataque, e junto com a função max(), ele guarda na var 'biggest_atk' o array inteiro com maior ataque.
biggest_atk = max(character, key=lambda x: x[1][0]) 

# aqui a mesma coisa, so muda que ao inves de procurar pelo maior ataque ele procura pela maior defesa.
biggest_def = max(character, key=lambda x: x[1][1])

# imprimir o maior ataque e a maior defesa
print(f"Ataque {biggest_atk[0]} {biggest_atk[1][0]}")
print(f"Defesa {biggest_def[0]} {biggest_def[1][1]}")

