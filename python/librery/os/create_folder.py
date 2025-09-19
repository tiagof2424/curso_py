import os

name_folder ="./backups_tiago"
#crear la  ruta de la carpeta definida en la variable namefolder
path_folder= os.path.join(name_folder)
#comprobar si una carpeta existe o no
if not os.path.exists(path_folder):
    #crear carpeta o directorio
    os.mkdir(path_folder)