def bereken_bmi(gewicht, lengte_cm):
    lengte_m = lengte_cm/100
    return gewicht/pow(lengte_m, 2)


def bmi_orde(bmi):
    if bmi < 18.5:
        return "BMI te laag"
    if 18.5 <= bmi < 25:
        return "BMI normaal"
    if 25 <= bmi < 35:
        return "Je bent beetje dik"
    if bmi >= 35:
        return "Wollah ga afvallen ofz"


def bereken_bmr(geslacht, gewicht, lengte_cm, leeftijd):
    geslacht = geslacht.lower().replace(" ", "")
    if geslacht == "man" or geslacht == "men" or geslacht == "mann":
        return (10 * gewicht) + (6.25 * lengte_cm) - (5 * leeftijd) + 5
    elif geslacht == "woman" or geslacht == "women" or geslacht == "vrouw":
        return (10 * gewicht) + (6.25 * lengte_cm) - (5 * leeftijd) - 161
    else:
        raise Exception("Geslacht " + geslacht + " is niet geldig")


def bereken_epoc(intensiteit, duur):
    return 0.0215 * intensiteit * duur


def bereken_karvonen(hfwerk, hfrust, hfmax):
    return ((hfwerk - hfrust) / (hfmax - hfrust))*100


def print_hoofdmenu():
    print("Maak uw keuze\n[1] = BMI\n[2] = BMR\n[3] = EPOC\n[4] = karvonen\n[5] = exit")