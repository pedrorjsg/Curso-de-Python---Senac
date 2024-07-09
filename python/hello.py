# ler o nome de usuario
nome = input("Qual é o seu nome? ").strip().title()

#nome = nome.strip().title().capitalize()

primeiro, sobrenome = nome.split(" ")
# exibir uma mensagem na tela de saudação
print(f"Olá, {nome}")
print(sobrenome)