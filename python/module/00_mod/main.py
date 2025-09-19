try:
    from core import config 
except ImportError as e:
    print("error al importar la libreria", e)
num1 = input ("numero1: ")
op = input ("op: ")
num2 = input ("numero2: ")
config.calcular(num1,op,num2)