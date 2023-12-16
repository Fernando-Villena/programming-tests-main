class SQL:
    seq = 0
    
    #Variable para almacenar los libros
    database = {}

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        record_id = SQL.seq
        SQL.database.setdefault(table_name, {})[record_id] = kwargs
        return record_id

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actualizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)
        SQL.database.setdefault(table_name, {})[record_id].update(kwargs)

    def list(self, table_name="books"):
        print(f"Lista de {table_name}")
        return SQL.database.get(table_name, {})

    def retrieve(self, record_id, table_name="books"):
        print(f"Se obtiene {record_id} desde {table_name}")
        return SQL.database.get(table_name, {}).get(record_id, None)

    def delete(self, record_id, table_name="books"):
        print(f"Se eliminó {record_id} desde {table_name}")
        if table_name in SQL.database and record_id in SQL.database[table_name]:
            del SQL.database[table_name][record_id]


class Book:
    def __init__(self, nombre: str, autor: str = None, num_paginas: int = None):
        self.id = None
        self.nombre = nombre
        self.autor = autor
        self.num_paginas = num_paginas
    
    #Guardar los libros
    def save(self):
        if self.id is None:
            self.id = SQL().create(nombre=self.nombre, autor=self.autor, num_paginas=self.num_paginas)
        else:
            SQL().update(record_id=self.id, nombre=self.nombre, autor=self.autor, num_paginas=self.num_paginas)
    
    #Listar todos los libros
    @staticmethod
    def list_books():
        return SQL().list(table_name="books")
    
    #Obtener un libro por su id
    @staticmethod
    def get_book(record_id: int):
        return SQL().retrieve(record_id)
    
    #Eliminar un libro por su id
    def delete(self):
        if self.id is not None:
            SQL().delete(record_id=self.id)
            self.id = None

#Aqui se puede ver el uso

libro = Book(nombre="Cien años de soledad", autor="Gabriel García Márquez", num_paginas=400)
libro2 = Book(nombre="1984", autor="George Orwell", num_paginas=320)
libro3 = Book(nombre="Orgullo y prejuicio", autor="Jane Austen", num_paginas=250)
libro4 = Book(nombre="El señor de los anillos: La comunidad del anillo", autor="J.R.R. Tolkien", num_paginas=550)

#Se realiza el guardado de los libros
libro.save()
libro2.save()
libro3.save()
libro4.save()

#En esta parte se actualiza el libro 
libro2.nombre = "Código Da Vinci"
libro2.autor = "Dan Brown"
libro2.num_paginas = 464
libro2.save()

#Elimina el libro 
libro.delete()

#Lista todos los libros
print(Book.list_books())

#Obtiene un libro por su id
print(Book.get_book(record_id=4))


