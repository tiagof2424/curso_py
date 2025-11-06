n1 = input("num1:")
n2 = input("num2:")
op = input("op:")
print (n1[0])
def iterar_conjunto(n1,n2):
    for n in n1:
        if n == "," or n == " " or n == "[" or n == "]": 
            continue
        print(int(n)+int(n2))

if op == "+":
    if n1[0] == "[" and n1[-1] == "]":
        print(int(n1[1])+int(n2))
        print(int(n1[3])+int(n2),'\n')
        iterar_conjunto(n1,n2)
   # print(int(n1)+int(n2))
elif op == "-":
    print(int(n1)-int(n2))
elif op == "/":
    print(int(n1)/int(n2))
elif op == "*":
    print(int(n1)*int(n2))
else:
    print ("error")
