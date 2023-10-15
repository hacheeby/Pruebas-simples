
horas = 5


horas = int(input("Número de horas trabajadas: "))



if horas <= 40:
    resultado = horas * 8
    print("has cobrado un total de", resultado, "€")
else:
    if 40 < horas <60:
        resultado2 = (horas - 40) * 12 + 40*8
        print("has cobrado un total de", resultado2, "€€")
    else:
            print("ERROR, no puedes trabajar", horas, "horas")



