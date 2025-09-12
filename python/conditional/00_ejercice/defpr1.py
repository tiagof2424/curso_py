name = "ez"
name1= "z"
# #condicional que compueba una variable
# if name == "ez" :
#     print("admin:",name)
# elif name =="z":
#     print("user: ",name)

#funcion que reutiliza el condicional anterior para evaluar una variable
def eval(name):
    if name == "ez" :
        print("admin:",name)
    elif name =="z":
        print("user: ",name)

eval(name)
eval(name1)