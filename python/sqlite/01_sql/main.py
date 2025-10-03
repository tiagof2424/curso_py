try:
    import os
    from core import config
    import sqlite3 as sql
except ImportError as e:
    print("Error al importar",e)

#conectarse y crear el archivo .db
conn = sql.connect(config.full_path_file_db)
curso = conn.cursor()

curso.execute("""
    CREATE TABLET IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, 
        age INTEGER,
        email TEXT UNIQUE          
    )
""")
conn.commit()
curso.execute("INSERT INTO students(name, age, email) VALUES (?,?,?)",[""])