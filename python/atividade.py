#nota1 = int(input("digite a primeira nota: "))
#nota2 = int(input("digite a segunda nota: "))

#function calcularMedia(nota1, nota2){
#   return((nota1) + (nota2)/2)
#}
#print(calcularMedia)



# verificar o conceito


# Ler duas Notas
#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))

# Calcular a média
#media = (nota1 + nota2) / 2

# exibir o conceito
#if media >= 9:
#        print("Conceito: O") 
#   elif media > 7 and media <= 8.9:
#       print("Conceito: B")
#   elif media > 5 and media <= 6.9:
#        print("Conceito: S")
#    else:
#        print("Conceito: I")

    
#---------------------------------------
def calcularMedia(valor1, valor2):
    return (valor1 + valor2)/2

def calcularConceito(valor):
    if valor >= 9:
        return "O"
    elif valor > 7 and valor <= 8.9:
        return "B"
    elif valor > 5 and valor <= 6.9:
        return "S"
    else:
        return "I"

def main():
# ler duas notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    #calcular a média
    media = calcularMedia(nota1, nota2)
    #verificar o conceito
    print(calcularConceito(media))
main()    

    






