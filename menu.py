
from consulta import agregarModulo, asignarModulo, editarModulo, eliminarDatos, eliminarModulo, matricular, modificarUsuario, modulosProfesor, mostrarAlumnos, mostrarModuloProfe, mostrarModulos, mostrarTodos, nuevoUsuario


def menuAlumno():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("__________________________________")
            print ("__________Menu Alumno___________\n")
            print ("1)  Inscribir alumno en modulo")
            print ("2)  Quitar alumno del modulo")
            print ("3)  Cambiar alumno de sección")
            print ("4)  Agregar nota a alumno")
            print ("5)  Editar nota a alumno")
            print ("6)  Quitar nota a alumno")
            print ("7)  Matricular alumno")
            print ("8)  Anular matricula")
            print ("9)  Editar matricula")
            print ("10) Listar alumnos matriculados")            
            print ("11) Volver")
            print ("12) Salir")
            print("__________________________________")
            opcion= int(input("Ingrese seleccion: \n"))
            if opcion < 1 or opcion > 12:
                print("La opcion ingresada no es valida, intente nuevamente...")
            
            elif opcion ==1:
                matricular()
            elif opcion==2:
                mostrarTodos()
                eliminarDatos()
            elif opcion ==7:
                matricular()
            elif opcion ==2:
                eliminarDatos()            
            elif opcion ==10:
                mostrarAlumnos()
            elif opcion == 12:
                continuar=False
                print("Gracias por usar mi programa")
                break
            else:
                print("Opcion no valida !!")

def menuModulos():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("__________________________________")
            print ("______Menu Modulos________\n")
            print ("1) Asignar modulo a docente")
            print ("2) Ver módulos docente")
            print ("3) Quitar módulos a docente")
            print ("4) Agregar modulo a sistema")
            print ("5) Editar modulo a sistema")
            print ("6) Eliminar modulo a sistema")
            print ("7) Ver todos los módulos del sistema")
            print ("8) Volver")
            print ("9) Salir")
            print("__________________________________")

            opcion= int(input("Ingrese seleccion: "))
            if opcion < 1 or opcion > 9:
                print("La opcion ingresada no es valida, intente nuevamente...")
            if opcion == 1:
                modulosProfesor()
            elif opcion==2:
                mostrarModuloProfe()
            elif opcion ==3:
                agregarModulo()
            elif opcion ==4:
                agregarModulo()
            elif opcion == 5:
                editarModulo()
            elif opcion==6:
                eliminarModulo()
            elif opcion == 7:
                mostrarModulos()
            elif opcion == 8:
                menuIngreso()
            elif opcion == 9:
                continuar=False
                print("Gracias por usar mi programa")
                break
            else:
                print("Opcion no valida !!")
            
def menuIngreso():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("__________________________________")
            print ("__________Bienvenido_____________")
            print ("1) Menu Modulos")
            print ("2) Menu Alumno")
            print ("3) Salir")
            print("__________________________________")

            opcion= int(input("Ingrese seleccion: "))
            if opcion < 1 or opcion > 5:
                print("La opcion ingresada no es valida, intente nuevamente...")
            elif opcion==1:
                menuModulos()
            elif opcion==2:
                menuAlumno()
            elif opcion == 3:
                continuar=False
                print("Gracias por usar mi programa")
                break
            else:
                print("Opcion no valida !!")

def menuUsuario():
    continuar=True
    while (continuar):
        opcionCorrecta= False
        while (not opcionCorrecta):
            print("____________________________________\n")
            print ("1) Crear Nuevo Usuario ")
            print ("2) Cambiar contraseña ")
            print ("3) Ingresar a menu inicial")
            print ("4) Salir ")
            print("____________________________________\n")
            opcion= int(input("Indique seleccion:"))
            
            if opcion < 1 or opcion > 5:
                print("La opcion ingresada no es valida, intente nuevamente...")
            elif opcion ==1:
                nuevoUsuario()
            elif opcion ==2:
                modificarUsuario()
            elif opcion ==3:
                menuIngreso()
            elif opcion == 4:
                continuar=False
                print("Gracias por usar mi programa")
                break
            else:
                print("Opcion no valida !!")
