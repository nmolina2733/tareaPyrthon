
import cx_Oracle

def mostrarTodos():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    cursor.execute('select * from Matricula')
    for line in cursor:
        print(line)
    cursor.close()
    conexion.close()

def mostrar():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    nombre = input("ingrese nombre ")
    seleccionar ='''select * from alumno where nombre = ('%s')'''% nombre
    cursor.execute(seleccionar)
    resultado = cursor.fetchone()
    print (resultado)
    cursor.close()
    conexion.close()

def matricular():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    carrera = input("\n|Programacion (1)|\n|Contabilidad (2)|\n|Diseño (3)|\n|Mecanica (4)|\n|Ingenieria en informatica (5)|: ")
    sede = input("Ingrese sede: ")
    fecha = input("Ingrese fecha de matricula: ")
    jornada = int(input("Ingrese jornada: \n| Diurna (1) |\n| Vespertina (2) | "))
    semestre = input("Ingrese semestre actual: ")
    valorMatricula = int(input("Ingrese valor matricula: "))
    cuotas= int(input("Ingrese valor cuota: "))
    metodoPago= input("Ingrese metodo de pago: | Credito | Debito| Efectivo |: ")

    insertar ='''insert into matriculas values (CodigoMatricula.nextval,CodigoAlumno.nextval,:carr, :sed, :fe, :jor, :sem, :valor, :cuo, :pago)'''
    cursor.execute(insertar,carr=carrera,sed=sede,fe=fecha,jor=jornada,
    sem=semestre,valor=valorMatricula,
    cuo=cuotas,pago=metodoPago)
    conexion.commit()
    print ("Matriculado correctamente")
    cursor.close()
    conexion.close()

def nuevoUsuario():

    conexion= cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')
    print ("conectado",conexion.version)
    
    cursor=conexion.cursor()
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contraseña: ")
    insertar ='''insert into usuarios values (:us, :pas)'''
    cursor.execute(insertar,us=usuario,pas=contrasena)
    conexion.commit()
    print ("Usuario creado correctamente")
    cursor.close()
    conexion.close()

def ingresarNotas():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    codigo = input("Ingrese codigo prueba: ")
    nombre = input("Ingrese Nombre alumno: ")
    nota = input("Ingrese nota: ")
    insertar ='''insert into notas values ('%s','%s','%s' )''' %(codigo,nombre,nota)
    cursor.execute(insertar)
    conexion.commit()
    cursor.close()
    conexion.close()

def verNotas():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    nombre = input("ingrese nombre ")
    seleccionar ='''select * from notas where nombre = ('%s')'''% nombre
    cursor.execute(seleccionar)
    resultado = cursor.fetchone()
    print (resultado)
    cursor.close()
    conexion.close()

def nuevaTabla():
    try:
        conexion= cx_Oracle.connect(
        user = 'escuela',
        password = '1234',
        dsn = 'localhost:1521/xe')
        print ("conectado",conexion.version)
        cursor=conexion.cursor()
        tablaNueva ='''create table modulo(
            codigo int,
            nombre varchar(100),
            carrera varchar(100))'''

        cursor.execute(tablaNueva)
        print ("Tabla creada correctamente")

    except Exception as ex:
        print (ex)

    finally:
        conexion.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

def eliminarDatos():

    try:
        conexion= cx_Oracle.connect(
        user = 'system',
        password = '273321',
        dsn = 'localhost:1521/xe')
        try:
            cursor=conexion.cursor()
            alumno = input("Ingrese nombre de alumno a eliminar: ")
            eliminar ='''delete from alumno where nombre=(Nombre=:nom)'''
            cursor.execute(eliminar,nom=alumno)
            conexion.commit()
            

        except Exception:
            print ("Error al eliminar datos")
    
        else:
            print ("Datos eliminados correctamente")

    except Exception as ex:
        print (ex)

    finally:
        conexion.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

def ingresarUsuario():
    try:
        conexion= cx_Oracle.connect(
        user = 'escuela',
        password = '1234',
        dsn = 'localhost:1521/xe')
        print ("conectado",conexion.version)
        try:
            cursor=conexion.cursor()
            insertar ='''insert into usuarios (usuario, contraseña) values ('natalie','1234')'''
            cursor.execute(insertar)
            conexion.commit()

        except Exception:
            print ("Error al ingresar usuario")
    
        else:
            print ("Usuario creado correctamente")

    except Exception as ex:
        print (ex)

    finally:
        conexion.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")


           
        
        
    cursor.close()
    conexion.close()

def mostrarModulo():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')
    cursor = conexion.cursor()
    cursor.execute('''select * from secciones ''')
    resultado=cursor.fetchall()
    print (resultado)
    cursor.close()
    conexion.close()

def asignarModulo():
    try:

        conexion = cx_Oracle.connect(
        user = 'escuela',
        password = '1234',
        dsn = 'localhost:1521/xe')
        cursor = conexion.cursor()
        cpr = int(input("Indique codigo de profesor: "))
        secciones = input("Indique seccion donde se asignara el profesor: ")
        cursor.execute('''update profesores set seccion=:secciones where CodigoProfesor=:cp''',seccion=secciones,cp=cpr)
        cursor.commit()

    except:
        print ("Error al asignar modulo")

def modificarUsuario():
    try:
        conexion= cx_Oracle.connect(
        user = 'escuela',
        password = '1234',
        dsn = 'localhost:1521/xe')
                
        cursor=conexion.cursor()
        contra = input("Ingrese usuario que desea modificar: ")
        contrasenaNueva = input("Ingrese nueva contraseña: ")
        cursor.execute('''update usuarios set contrasena=:Nueva where usuario=:us''',Nueva=contrasenaNueva,us=contra)
        conexion.commit()
        print ("Contraseña cambiada con éxito")
                    
    except Exception:
        print ("Error al editar")

def mostrarModulos():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    cursor.execute('select * from secciones')
    for line in cursor:
        print(line)
    cursor.close()
    conexion.close()

def modulosProfesor():
    try:
        conexion = cx_Oracle.connect(
        user = 'escuela',
        password = '1234',
        dsn = 'localhost:1521/xe')


        cursor = conexion.cursor()
        sec= input("Ingrese seccion: ")
        codigo = int(input("Ingrese codigo de profesor: "))
        cursor.execute('''update profesores set seccion=:secc where CodigoProfesor=:cod''',secc=sec,cod=codigo)
        conexion.commit()
        print ("Asignado correctamente ")
        cursor.close()
        conexion.close()
    except:
        print ("Error al asignar el modulo")

def mostrarAlumnos():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    cursor.execute('select * from alumnos')
    for line in cursor:
        print(line)
    cursor.close()
    conexion.close()

def agregarModulo():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    cursor.execute('''select * from secciones''')
    mostrar=cursor.fetchall()
    print (mostrar)
    codigo=input("Ingrese seccion: ")
    ramo1= int(input("Ingrese codigo ramo 1:  "))
    ramo2= int(input("Ingrese codigo ramo 2:  "))
    ramo3= int(input("Ingrese codigo ramo 3:  "))
    ramo4= int(input("Ingrese codigo ramo 4:  "))
    cursor.execute('''insert into secciones values (:cod,:n1,:n2,:n3,:n4)''',cod=codigo,n1=ramo1,n2=ramo2,n3=ramo3,n4=ramo4)
    conexion.commit()
    print ("Modulo agregado correctamente")
    cursor.close()
    conexion.close()

def editarModulo():
    try:
        conexion= cx_Oracle.connect(
        user = 'escuela',
        password = '1234',
        dsn = 'localhost:1521/xe')
                
        cursor=conexion.cursor()
        contra = input("Ingrese modulo que desea modificar: ")
        cod = input("Ingrese nuevo codigo de seccion: ")
        ramo1 = int(input("Ingrese codigo de curso 1: "))
        ramo2 = int(input("Ingrese codigo de curso 2: "))
        ramo3 = int(input("Ingrese codigo de curso 3: "))
        ramo4 = int(input("Ingrese codigo de curso 4: "))
        cursor.execute('''update secciones set CodigoSeccion=:cod and ramo1=:r1,ramo2=:r2,ramo3=:r3,ramo4=:r4 where CodigoSeccion=:codi''',cod=contra,r1=ramo1,r2=ramo2,r3=ramo3,r4=ramo4, codi=cod)
        conexion.commit()
        print ("Modulo modificado con éxito")
                    
    except Exception:
        print ("Error al editar")
        
def eliminarModulo():
    try:
        conexion= cx_Oracle.connect(
        user = 'escuela',
        password = '1234',
        dsn = 'localhost:1521/xe')
        
        cursor=conexion.cursor()
        modulo = input("Ingrese codigo de modulo a eliminar: ")
        eliminar ='''delete from secciones where codigosSeccion=:nom'''
        cursor.execute(eliminar,nom=modulo)
        conexion.commit()
        print ("Modulo eliminado correctamente")
            

    except Exception:
        print ("Error al eliminar datos")
    
def mostrarModuloProfe():
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')


    cursor = conexion.cursor()
    profe = int(input("Indique codigo de profesor a consultar"))
    cursor.execute('select * from profesores where CodigoProfesor=:pro',pro=profe)
    for line in cursor:
        print(line)
    cursor.close()
    conexion.close()
