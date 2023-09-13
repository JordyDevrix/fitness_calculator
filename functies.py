def bereken_bmi(gewicht, lengte_cm):
    lengte_m = float(lengte_cm)/100
    bmi = float(gewicht)/(pow(float(lengte_m), 2))
    return bmi


def bereken_bmr(geslacht, gewicht, lengte_cm, leeftijd):
    geslacht = geslacht.lower().replace(" ", "")
    if geslacht == "man" or geslacht == "men" or geslacht == "mann":
        bmr = (10 * float(gewicht)) + (6.25 * float(lengte_cm)) - (5 * float(leeftijd)) + 5
        return bmr
    elif geslacht == "woman" or geslacht == "women" or geslacht == "vrouw":
        bmr = (10 * float(gewicht)) + (6.25 * float(lengte_cm)) - (5 * float(leeftijd)) - 161
        return bmr
    else:
        bmr = 0.00
        return bmr


def bereken_epoc(intensiteit, duur):
    epoc = 0.0215 * float(intensiteit) * float(duur)
    return epoc


def bereken_karvonen(hfwerk, hfrust, hfmax):
    karvonen = ((float(hfwerk) - float(hfrust)) / (float(hfmax) - float(hfrust)))*100
    return karvonen


def print_hoofdmenu():
    print("Maak uw keuze\n[1] = BMI\n[2] = BMR\n[3] = EPOC\n[4] = karvonen\n[5] = exit")