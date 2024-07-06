#nome = input("Digite o perdonagem: ")

#if nome == "Frodo":
#    print("Hobbit")
#elif nome == "Sam":
 #   print("Hobbit")
#elif Nome == "Aragorn":
 #   print("Homem")
#elif nome == "Gandalf":
#    print("Mago")     



#------------------------------

nome = input("Digite o personagem")
match nome: 
    case "Frodo" | "Sam":
        print("Hobbit")
    case "Arogorn":
        print("Homem")
    case "Gandalf":
        print("Mago")
    case _:
        print("Quem??")                

#if nome == "Frodo":
#    print("Hobbit")
#elif nome == "Sam":
 #   print("Hobbit")
#elif Nome == "Aragorn":
#    print("Homem")
#elif nome == "Gandalf":
#    print("Mago")            