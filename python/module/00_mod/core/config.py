def calcular(n1,op,n2):
    if op  == "/" and n2==0:
        return
    result = eval(f"{n1}+{op}+{n2}")
    print(result)