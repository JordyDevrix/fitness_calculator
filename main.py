from functies import *
version = "v0.0.1-alpha"


def main():
    print(version)
    while True:
        print_hoofdmenu()
        keuze = input()
        if keuze == '1':
            gewicht = input("gewicht: ")
            lengte = input("lengte: ")
            print("BMI: %.2f" % bereken_bmi(gewicht, lengte), "\n")
        elif keuze == '2':
            geslacht = input("geslacht: ")
            gewicht = input("gewicht: ")
            lengte = input("lengte: ")
            leeftijd = input("leeftijd: ")
            print("BMR: %.2f" % bereken_bmr(geslacht, gewicht, lengte, leeftijd), "\n")
        elif keuze == '3':
            intensiteit = input("intensiteit: ")
            duur = input("duur: ")
            print("EPOC: %.2f" % bereken_epoc(intensiteit, duur), "\n")
        elif keuze == '4':
            hfwerk = input("HFwerk: ")
            hfrust = input("HFrust: ")
            hfmax = input("HFmax: ")
            print("Karvonen: %.2f" % bereken_karvonen(hfwerk, hfrust, hfmax), "\n")
        elif keuze == '5':
            break
        else:
            print("Geen keuze gemaakt\nAutomatisch afsluiten gestart")
            break


if __name__ == '__main__':
    main()