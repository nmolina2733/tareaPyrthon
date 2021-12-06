import cx_Oracle

class Alumno:
    codigoAlumno=0
    nombre = ""
    carrera = ""
    modulo = ""
    jornada = ""
    codigoMatricula=0

    def __init__(self,cod,nom,car,mo,jo,codma):
        self.codigoAlumno= cod
        self.nombre=nom
        self.carrera=car
        self.modulo=mo
        self.jornada=jo
        self.codigoMatricula=codma

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

class Profesor:
    codigoProfesor=0
    nombre= ""
    ramo=""
    seccion=""

    def __init__(self,codP,nom,ra,sec):
        self.codigoProfesor=codP
        self.nombre=nom
        self.ramo=ra
        self.seccion=sec

class Matricula:
    codigoMatricula=0
    rut=""
    carrera=""
    fecha =""
    semestre=""
    valorMatricula=0
    cuotas=0
    metodoPago=""

    def __init__(self,codigo,ru,carr,fe,sem,val,cuo,metP):
        self.codigoMatricula=codigo
        self.rut=ru
        self.carrera=carr
        self.fecha=fe
        self.semestre=sem
        self.valorMatricula=val
        self.cuotas=cuo
        self.metodoPago=metP

class Modulo:
    pass

class Secciones:
    codigoSeccion=0
    ramo1=0
    ramo2=0
    ramo3=0
    ramo4=0

    def __init__(self,cod,r1,r2,r3,r4):
        self.codigoSeccion=cod
        self.ramo1=r1
        self.ramo2=r2
        self.ramo3=r3
        self.ramo4=r4

class Usuaraios:
    usuario=""
    contraseña=""

    def __init__(self,us,con):
        self.usuario=us
        self.contraseña=con

class Ramo:
    codigoRamo=0
    carrera=0
    descripcion=""

    def __init__(self,cr,ca,des):
        self.codigoRamo=cr
        self.carrera=ca
        self.descripcion=des
        
class Jornada:
    codigoJornada=0
    descripcion=""

    def __init__(self,cj,des):
        self.codigoJornada=cj
        self.descripcion=des
        



