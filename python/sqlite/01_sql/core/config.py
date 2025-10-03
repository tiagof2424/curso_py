try:
    import os
    from pathlib import Path
except ImportError as e:
    print("Error al importar",e)    


#obtener el directorio de trabajo actual
cwd = os. getcwd()
custom_path = os.path.join(cwd , "python/sqlite/01_sql")

#crear el nombre de la carpeta donde almacenaremos nuestro archivo .db acronimo base de datos
folder_db = "db/folder_db"

#unir toda la ruta de la carpeta folder db
full_path_db = os.path.join(custom_path,folder_db)


# comprobar si existe la carpeta folder_db, crearla en caso que no exista
if not os.path.exists(full_path_db):
    #crear carpeta
    os.makedirs(full_path_db)

#crear una base de dato de ejemplo
filename_db = "example"

#comprobar que el archivo contenga la extension .db 
filename_db = str(Path(filename_db).with_suffix(".db").stem + ".db")