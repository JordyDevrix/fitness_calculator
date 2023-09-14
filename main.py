from functies import *
version = "v1.0.3-alpha"


def main():
    print("Welkom bij de fitness app", version)
    running = True
    while running:
        print_hoofdmenu()
        keuze = input()
        if keuze == '1':
            gewicht = int(input("gewicht: "))
            lengte = int(input("lengte: "))
            print("BMI: %.2f" % bereken_bmi(gewicht, lengte))
            print(bmi_orde(bereken_bmi(gewicht, lengte)), "\n")
        elif keuze == '2':
            geslacht = input("geslacht: ")
            gewicht = int(input("gewicht: "))
            lengte = int(input("lengte: "))
            leeftijd = int(input("leeftijd: "))
            print("BMR: %.2f" % bereken_bmr(geslacht, gewicht, lengte, leeftijd), "\n")
        elif keuze == '3':
            intensiteit = int(input("intensiteit: "))
            duur = int(input("duur: "))
            print("EPOC: %.2f" % bereken_epoc(intensiteit, duur), "\n")
        elif keuze == '4':
            hfwerk = int(input("HFwerk: "))
            hfrust = int(input("HFrust: "))
            hfmax = int(input("HFmax: "))
            print("Karvonen: %.2f" % bereken_karvonen(hfwerk, hfrust, hfmax), "\n")
        elif keuze == '5':
            print("Ending process")
            running = False
        else:
            print("Geen keuze gemaakt\nAutomatisch afsluiten gestart")
            running = False


if __name__ == '__main__':
    main()