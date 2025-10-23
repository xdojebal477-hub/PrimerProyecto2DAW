class Pelicula():
    
    def __init__(self,titulo,director,año) ->None:
        self.titulo=titulo
        self.director=director
        self.año=año

    def __str__(self) ->str:
        return f"{self.titulo} del director {self.director} del año {self.año}"


class Bilbioteca():
    
    def __init__(self) ->None:
        self.lista=[]
    
    def add_film(self,peli)->None:
        existing_films=[f for f in self.lista]
        if not peli in existing_films:
            self.lista.append(peli)
            return
        print("Pelicula ya añadida previamente")
        return
    
    def show_films(self)->str:
        for p in self.lista:
            print(f" - {p}")

    def search_film(self)->Pelicula:
        pass

    def remove_film(self,titulo):
        for f in self.lista:
            if f.titulo.lower()==titulo.lower():
                self.lista.pop(f)
            if not f in self.lista:
                print(f" Pelicula {f}")


p1=Pelicula("pelicula1","DOB",2025)
print(p1)
p2=Pelicula("pelicula2","MJ",2026)
print(p2)
p3=Pelicula("pelicula3","CN",2025)
print(p3)
biblioteca=Bilbioteca()
biblioteca.add_film(p1)
biblioteca.add_film(p2)
biblioteca.add_film(p3)
biblioteca.add_film(p1)
biblioteca.show_films()
biblioteca.remove_film(p1.titulo)
