def bereken_bmi(gewicht, lengte_cm):
    lengte_m = float(lengte_cm)/100
    return float(gewicht)/(pow(float(lengte_m), 2))


def bereken_bmr(geslacht, gewicht, lengte_cm, leeftijd):
    geslacht = geslacht.lower().replace(" ", "")
    if geslacht == "man" or geslacht == "men" or geslacht == "mann":
        return (10 * float(gewicht)) + (6.25 * float(lengte_cm)) - (5 * float(leeftijd)) + 5
    elif geslacht == "woman" or geslacht == "women" or geslacht == "vrouw":
        return (10 * float(gewicht)) + (6.25 * float(lengte_cm)) - (5 * float(leeftijd)) - 161
    else:
        raise Exception("Geslacht " + geslacht + " is niet geldig")


def bereken_epoc(intensiteit, duur):
    return 0.0215 * float(intensiteit) * float(duur)


def bereken_karvonen(hfwerk, hfrust, hfmax):
    return ((float(hfwerk) - float(hfrust)) / (float(hfmax) - float(hfrust)))*100


def print_hoofdmenu():
    print("Maak uw keuze\n[1] = BMI\n[2] = BMR\n[3] = EPOC\n[4] = karvonen\n[5] = exit")