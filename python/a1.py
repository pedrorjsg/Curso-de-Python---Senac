def incluir(contatos):
    nome = input("Digite o nome: ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone: ")
    contatos.append({"nome": nome, "endereco": endereco, "telefone": telefone})
    # Adicionando um print para verificar se o contato foi incluído corretamente
    print("Contato incluído com sucesso!")
    print(contatos)

def listar(contatos):
    if not contatos:
        print("Nenhum contato encontrado.")
    else:
        for i, contato in enumerate(contatos):
            print(f"Contato {i+1}:")
            print(f"Nome: {contato['nome']}")
            print(f"Endereço: {contato['endereco']}")
            print(f"Telefone: {contato['telefone']}")
            print("-" * 20)

def main():
    contatos = []
    
    while True:
        print("Menu")
        print("1 - Incluir")
        print("2 - Listar")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            incluir(contatos)
        elif opcao == '2':
            listar(contatos)
        elif opcao == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
