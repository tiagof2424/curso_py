# tres chicos quieren comprar una consola, pero hay un problema, los precios no estan alado de los estantes, ellos quieren comprar la consola mas cara.
# tenemos que solicitar el dinero que tiene cada uno, si hay dos consolas con el mismo precio debemos mostrar las dos consolas y mostrar el vuelto por si les queda
trolintrolin_cash = 100.000
emirsita_cash = 200.000
marcelo_cash =400.000
console =  {
    "ps4": 200.000,
    "xboxseriesx": 190.000,
    "ps2": 90.000,
    "ps8": 400.000, 
}

if trolintrolin_cash <= console["ps4"]:
    print(f"trolintrolin te podes comprar la consola {console['ps2']}")
elif trolintrolin_cash <= console["ps8"] and trolintrolin_cash <= console["xboxseriesx"]:
    print(f"trolintrolin te podes comprar la consola ps8 ${console['ps8']} ,o te podes comprar la xoboxseriesx ${console['xboxseriesx']}")
if emirsita_cash <= console["ps4"]:
    print(f"emirsita te podes comprar la consola {console['ps4']}")
elif emirsita_cash <= console["ps8"] and emirsita_cash <= console["xboxseriesx"]:
    print(f"emirsita te podes comprar la consola ps4 ${console['ps4']} ,o te podes comprar la xoboxseriesx ${console['xboxseriesx']}")
if marcelo_cash <= console["ps8"]:
    print(f"marcelo te podes comprar la consola {console['ps8']}")
elif marcelo_cash <= console["ps8"] and marcelo_cash <= console["xboxseriesx"]:
    print(f"emirsita te podes comprar la consola ps4 ${console['ps4']} ,o te podes comprar la xoboxseriesx ${console['xboxseriesx']}")
    