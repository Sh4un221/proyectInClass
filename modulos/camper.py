import os
from .variables import save,getAll,camper
def create():
    os.system("cls")
    print("""
        ***************************
        **** FORMULARIO CAMPER ****
        ***************************
        """)
    save({
        "Nombre":input("Ingrese el nombre del camper: "),
        "Apellido":input("Ingrese el apellido del camper: "),
        "Edad":int(input("Ingrese la edad del camper: ")),
        "Genero":input("Ingrese el genero del camper: ")
    })
    os.system('pause')
 
    
def read(codigo=None):
    os.system('cls')
    print("""
    *************************
    **** TABLA DE CAMPER ****
    *************************
    """)
    if(not codigo!=None):
        for i,val in enumerate(getAll()):
            print(f"""
                ________________________________
                Codigo:{i+1}
                Nombre:{val.get('Nombre')}
                Apellido:{val.get('Apellido')}
                Edad:{val.get('Edad')}
                Genero:{val.get('Genero')}
                _______________________________
            """)
    else:
        val=getAll()[codigo-1]
        print(f"""
        ________________________________
        Codigo:{codigo}
        Nombre:{val.get('Nombre')}
        Apellido:{val.get('Apellido')}
        Edad:{val.get('Edad')}
        Genero:{val.get('Genero')}
        _______________________________
        """)
    os.system('pause')
     
def update():
    
        bandera=True
        while(bandera):
                read()
                print("""
            *****************************
            ***** ACTUALIZAR CAMPER *****
            *****************************
            """)
            
                codigo=int(input("Cual es el codigo del camper que desea actualuzar?: \n"))
                read(codigo)
                print("""
                ¿Esta seguro que desea eliminar el camper?
                1.Si
                2.No
                3.Cancelar      
                """)
                opc=int(input())
            
                match(opc):
                    case 1: 
                        informacion={
                            "Nombre":input("Ingrese el nombre del camper: "),
                            "Apellido":input("Ingrese el apellido del camper: "),
                            "Edad":int(input("Ingrese la edad del camper: ")),
                            "Genero":input("Ingrese el genero del camper: ")
                        }
                        camper[codigo-1]=informacion
                        bandera=False
                        os.system('pause')
                    case 3:
                        bandera=False
                    
        print("el camper se actualizo")
    
def delete():
        bandera=True
        while(bandera):
                read()
                print("""
            ***************************
            ***** ELIMINAR CAMPER *****
            ***************************
            """)
            
                codigo=int(input("Cual es el codigo del camper que desea eliminar?: \n"))
                read(codigo)
                
                print("""
                ¿Esta seguro que desea eliminar el camper?
                1.Si
                2.No
                3.Cancelar      
                """)
                opc=int(input())
            
                match(opc):
                    case 1: 
                        val=camper.pop(codigo-1)
                        os.system('cls')
                        print(f"""
                        El camper fue eliminado
                        ________________________________
                        Codigo:{codigo}
                        Nombre:{val.get('Nombre')}
                        Apellido:{val.get('Apellido')}
                        Edad:{val.get('Edad')}
                        Genero:{val.get('Genero')}
                        _______________________________
                        """)
                        os.system('pause')
                        bandera=False
                    
                    case 3:
                        bandera=False
            
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
        
            

            