import sys

a = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
b = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

def getWochentag(tag, monat, jahr):
    if (jahr < 1900)or(jahr > 2099):
        return "Es koennen nur Wochentage zwischen 1900 und 2099 berechnet werden."

    sum = tag + getMonatsCode(monat, jahr) + getJahresCode(jahr)
    print("Tag = " + str(tag))
    print("Monat = " + str(getMonatsCode(monat, jahr)))
    print("Jahr = " + str(getJahresCode(jahr)))
    print("Summe = " + str(sum))
    print("Summe % 7 = " + str(sum % 7))

    if isSchaltjahr(jahr) and monat < 3:
        print("1 abziehen, da es ein " + b[monat-1] + " im Schaltjahr ist")
        print("Summe = ", str(sum), "- 1 = " + str(sum-1))
        sum = sum - 1

    wochentagCode = sum % 7
    return a[wochentagCode]

def getJahresCode(jahr):
    #Bsp 2016: jz = 16; x = 4; y = 20 % 7 = 6
    jz = jahr % 100
    x = jz / 4
    y = (jz + x) % 7

    #Bei anderen Jahrhunderten muss man ggf noch eine Zahl draufaddieren
    if jahr >= 1900 and jahr <= 1999:
        y += 1

    return int(y)

def getMonatsCode(monat, jahr):
    a = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    monatsCode = a[monat - 1]
    return monatsCode

def isSchaltjahr(jahr):
    return (jahr % 400) == 0 or ((jahr % 4) == 0 and (jahr % 100) != 0)

print(getWochentag(int(sys.argv[1:][0]), int(sys.argv[1:][1]), int(sys.argv[1:][2])))
