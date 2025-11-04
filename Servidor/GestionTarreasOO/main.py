import json,os

class Task():
    def __init__(self,title,description,priority,expiration_date,completed=False):
        self.title=title
        self.description=description
        self.priority=priority
        self.expiration_date=expiration_date
        self.completed=completed

    def mark_as_completed(self):
        self.completed=True
        print(f"Tarea '{self.title}' marcada como completada.")

    def update(self, title=None, description=None, priority=None, expiration_date=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if priority:
            self.priority = priority
        if expiration_date:
            self.expiration_date = expiration_date
        print(f"Tarea '{self.title}' actualizada.")

    def __str__(self):
        return f"Tarea: {self.title} || Prioridad: {self.priority} \n {self.description} \n Expira: {self.expiration_date}    Estado:{self.completed} \n================================================= "

    def to_dict(self):
        return {
            "titulo": self.title,
            "descripcion": self.description,
            "prioridad": self.priority,
            "fecha_vencimiento": self.expiration_date,
            "completada": self.completed
        }

    @staticmethod#Es una función auxiliar relacionada con la clase,
                #pero que no necesita acceder ni modificar los atributos de la clase o del objeto.
    def from_dict(data):
        return Task(
            data['titulo'],
            data['descripcion'],
            data['prioridad'],
            data['fecha_vencimiento'],
            data['completada']
        )



class TaskManager():
    
    def __init__(self):
        self.tasks=[]
    
    def add_task(self,task):#se puede hacer con un list comprehesion tmb
        if not any(t.title==task.title for t in self.tasks):
            self.tasks.append(task)
            return f"Tarea `{task.title} añadida a la agenda` "
        return f"Tarea `{task.title} ya existente en la agenda` "
    
    def delete_task(self,title):
        self.tasks=[t for t in self.tasks if t.title!=title]

    def actualizar_tarea(self, titulo, **kwargs):
        for tarea in self.tasks:
            if tarea.title == titulo:
                tarea.update(**kwargs)
                return
        print(f"No se encontró la tarea con título '{titulo}'.")

    def list_tasks_priority(self, lista=None) -> list[Task]:
        """Ordena una lista de tareas por prioridad. Si no se proporciona lista, usa todas las tareas."""
        priority_order = {"Alta": 1, "Media": 2, "Baja": 3}
        tasks_to_sort = lista if lista is not None else self.tasks
        return sorted(tasks_to_sort, key=lambda t: priority_order.get(t.priority, 4))

    def pending_tasks(self) -> list[Task]:
        """Devuelve las tareas pendientes ordenadas por prioridad."""
        pending_tasks = [task for task in self.tasks if not task.completed]
        return self.list_tasks_priority(pending_tasks)

    def     completed_tasks(self) -> list[Task]:
        """Devuelve las tareas completadas ordenadas por prioridad."""
        completed = [task for task in self.tasks if task.completed]
        return self.list_tasks_priority(completed)

    def save_tasks(self,file):
        try:
            with open(file,"w",encoding="utf-8") as f:
                json.dump([t.to_dict() for t in self.tasks], f, indent=4)#formateamos las task como un diccionario
        except Exception as e:
            print(f"Error al guardar tareas: {e}")

    def load_tasks(self,file):
        if not os.path.exists(file):
            print("No se encontró el archivo. Se creará un archivo vacío.")
            self.tasks = []
            return

        try:
            with open(file,"r",encoding="utf-8") as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in tasks_data]
                print("Tareas cargadas")
        except Exception as e:
            print(f"Error al cargar tareas: {e}")



"""def main():
    oTaskManager=TaskManager()
    
    oTaskManager.load_tasks("tareas.json")
    while True:
        print("\n===================== Menu Gestor de Tareas =====================")
        print("1.Añadir nueva tarea. ")
        print("2. Marcar tarea como completada.")
        print("3. Actualizar tarea.")
        print("4.Ver todas las tareas pendientes.")
        print("5.Ver todas las tareas completadas.")
        print("6.Cargar tareas")
        print("7.Salir (Guardar tareas)")
        
        
        opcion = input("Selecciona una opción: ").strip()
        match opcion:
            case"1":
                title=input("Titulo de la tarea: ").strip()
                task_descrp=input("Descripcion de la tarea: ")
                priority=input("Prioridad de la tarea(Alta/Media/Baja): ")
                fecha_vencimiento=input("Introduzca la fecha(dd-mm-aaaa): ")
                task=Task(title,task_descrp,priority,fecha_vencimiento,False)
                print(oTaskManager.add_task(task))
            case"2":
                title=input("Titulo de la tarea a marcar como completada: ").strip()
                for t in oTaskManager.tasks:
                    if t.title==title:
                        t.mark_as_completed()
                        break
            case"3":
                title=input("Titulo de la tarea a actualizar: ").strip()
                new_title=input("Nuevo titulo (dejar en blanco para no cambiar): ").strip()
                new_descrp=input("Nueva descripcion (dejar en blanco para no cambiar): ").strip()
                new_priority=input("Nueva prioridad(Alta/Media/Baja) (dejar en blanco para no cambiar): ").strip()
                new_date=input("Nueva fecha(dd-mm-aaaa) (dejar en blanco para no cambiar): ").strip()
                oTaskManager.actualizar_tarea(title,
                                            title=new_title if new_title else None,
                                            description=new_descrp if new_descrp else None,
                                            priority=new_priority if new_priority else None,
                                            expiration_date=new_date if new_date else None)
            case"4":
                print("\n--- TAREAS PENDIENTES ---")
                for t in oTaskManager.pending_tasks():
                    print(t)
                
            case"5":
                print("\n--- TAREAS Completadas ---")
                for t in oTaskManager.completed_tasks():
                    print(t)
            case"6":
                oTaskManager.load_tasks("tareas.json")
            case"7":
                oTaskManager.save_tasks("tareas.json")
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")



if __name__=="__main__":
    main()
    """

manager = TaskManager()
manager.add_task(Task("Tarea1", "Descripción1", "Alta", "2025-11-01", False))
manager.add_task(Task("Tarea2", "Descripción2", "Baja", "2025-11-02", False))
manager.add_task(Task("Tarea3", "Descripción3", "Media", "2025-11-03", True))

for t in manager.pending_tasks():
    print(t)
for t in manager.completed_tasks():
    print(t)