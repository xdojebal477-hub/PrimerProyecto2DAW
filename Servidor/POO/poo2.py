class Persona():
    
    def __init__(self,nombre,apellido,edad)->None:
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    def __str__(self):
        return f"Soy {self.nombre} {self.apellido} y tengo {self.edad} años"

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        self.asignaturas=[]
    
    def add_subject(self,*args)->None:
        for subject in args:
            if subject not in self.asignaturas:
                self.asignaturas.append(subject)

    def __str__(self):
        asignaturas_str = ', '.join(a.name for a in self.asignaturas)
        return f"{super().__str__()} y tengo las siguientes asignaturas: {asignaturas_str if asignaturas_str else 'ninguna'}"

    def show_teachers_from(self)->None:
        res=[]
        for a in self.asignaturas:
            if not a.teacher.nombre in res:
                res.append(a.teacher.nombre)
        return res

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
    

    def add_subject(self,*args)->None:
        for subject in args:
            if subject not in self.imparte:
                self.imparte.append(subject)

    def __str__(self):
        return f"{super().__str__()} e imparto las siguientes asignaturas: {self.imparte}"

class Asignatura():
    def __init__(self,name,hweek,teacher):
        self.name=name
        self.hweek=hweek
        self.teacher=teacher
    def __str__(self):
        return f"{self.name}: {self.hweek} horas semanales, impartida por {self.teacher}"
    

class Grupo():

    def __init__(self,name):
        self.name=name
        self.alumnos=[]

    def add_student(self,student):
        self.alumnos.append(student)
    def show_teachers_group(self):
        res = []
        for alumno in self.alumnos:
            for asignatura in alumno.asignaturas:
                res.append(asignatura.teacher.nombre)
        return set(res)
        # res=[ asi.teacher.nombre for a in self.alumnos for asi in a.asignaturas]
        # res_fin=set(res)
        # return res
        # # return set(asignatura.teacher.nombre for alumno in self.alumnos for asignatura in alumno.asignaturas)



t1=Profesor("JI","Huertas",30)
t2=Profesor("DD","Vega",32)


a1=Asignatura("Servidor",7,t1)
a2=Asignatura("Cliente",6,t2)
a3=Asignatura("IA",3,t2)




e1=Estudiante('Daniel','Ojeda Balsera',19)


e1.add_subject(a1,a2,a3)
print(e1)

print(e1.show_teachers_from())
g1=Grupo("2DAW")
print(g1.show_teachers_group())