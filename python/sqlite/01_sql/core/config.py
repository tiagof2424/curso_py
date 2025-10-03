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
full_path_file_db = os.path.join(full_path_db,filename_db)

#crear la carpeta donde guardaremos el archivo excel
folder_excel = "public/excel"
path_excel_folder = os.path.join((cwd + "/python/sqlite/01_sql"), folder_excel)

#crear
# la carpeta si no existe
if not os.path.exists(path_excel_folder):
    os.makedirs(path_excel_folder)

#crear el archivo excel
filename_excel = "example"
#comprobar que tenga el subfijo .xlsx
filename_excel = str(Path(filename_excel).with_suffix(".xlsx").stem + ".xlsx")
full_path_file_excel = os.path.join(path_excel_folder,filename_excel) 