try:
    import os
    from core import config
    import pandas as pd
except ImportError as e:
    print("Error al importar",e)

def create_excel(data,columns):
    if not os.path.exists(config.folder_excel):
        os.makedirs(config.folder_excel)

    # crear un dataframe que es similar a una tabla
    # cuenta con filas y columnas
    # pd.dataframe(datos_a_cargar, nombres_de_los_columnas)
    data_file = pd.Dataframe(data, columns=columns)
    data_file.to_excel(config.full_path_file_excel, engine="openpyxl")