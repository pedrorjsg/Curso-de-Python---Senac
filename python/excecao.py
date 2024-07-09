#Exceptions
#
# Comando try
# COmando except

while True:
    try:
        x = int(input("Digite um valor para x: "))
        print(f"x é {x}")
        break
    except ValueError:
        print("x não é um número")
    else:
         break
 