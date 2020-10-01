d = int(input("Ingresa tu dia de nacimiento: "))
m = int(input("Ingresa tu mes de nacimiento: "))
if (m==1) and (d>=1 and d<=31):
    if d>=1 and d<=20:
        print("\ncapricornio")
    if d>=21 and d<=31:
        print("\nacuario")
elif (m==2) and (d>=1 and d<=29):
    if d>=1 and d<=18:
        print("\nacuario")
    if d>=19 and d<=29:
        print("\npiscis")
elif (m==3) and (d>=1 and d<=31):
    if d>=1 and d<=20:
        print("\npiscis")
    if d>=21 and d<=31:
        print("\naries")
elif (m==4) and (d>=1 and d<=30):
    if d>=1 and d<=20:
        print("\naries")
    if d>=21 and d<=30:
        print("\ntauro")
elif (m==5) and (d>=1 and d<=31):
    if d>=1 and d>=20:
        print("\ntauro")
    if d>= 21 and d<=31:
        print("\ngeminis")
elif (m==6) and (d>=1 and d<=30):
    if d>=1 and d<=21:
        print("\ngeminis")
    if d>=22 and d<=30:
        print("\ncancer")
elif (m==7) and (d>=1 and d<=31):
    if d>=1 and d<=22:
        print("\ncancer")
    if d>=23 and d<=31:
        print("\nleo")
elif (m==8) and (d>=1 and d<=31):
    if d>=1 and d<=22:
        print("\nleo")
    if d>=23 and d<=31:
        print("\nvirgo")
elif (m==9) and (d>=1 and d<=30):
    if d>=1 and d<=22:
        print("\nvirgo")
    if d>=23 and d<=30:
        print("\nlibra")
elif (m==10) and (d>=1 and d<=31):
    if d>=1 and d<=22:
        print("\nlibra")
    if d>=23 and d<=31:
        print("\nescorpio")
elif (m==11) and (d>=1 and d<=30):
    if d>=1 and d<=22:
        print("\nescorpio")
    if d>=23 and d<=30:
        print("\nsagitario")
elif (m==12) and (d>=1 and d<=31):
    if d>=1 and d<=21:
        print("\nsagitario")
    if d>=22 and d<=31:
        print("\ncapricornio")
else:
    print("\nEl mes",m,"no existe...")