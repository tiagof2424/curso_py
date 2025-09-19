try:
    import os
except ImportError as e:
    print("error al importar la libreria", e)

cwd = os.getcwd()
print(cwd)