import os
def create():
    os.system("cls")
    print("""
        ***************************
        **** FORMULARIO CAMPER ****
        ***************************
        """)
    camper={
        "Nombre":input("Ingrese el nombre del camper: "),
        "Apellido":input("Ingrese el apellido del camper: "),
        "Edad":int(input("Ingrese la edad del camper: "))
    }
    
def read():
    print("Datos del camper encontrados")
    
def update():
    print("el camper se actualizo")
    
def delete():
    print("El camper se borro")
    
def menu():
    menu=["Guardar","Buscar","Actualizar","Eliminar","Salir"]
    
    while(True):
        os.system('cls')
        print("""
            ***************************
            ***** MENU DEL CAMPER *****
            ***************************
            """)
        print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: create()
                    case 2: read()
                    case 3: update()
                    case 4: delete()
                    case 5: break
    
        except ValueError:
            print(f"La opcion es invalida, porfavor ingrese algo valido.")
        
            

            