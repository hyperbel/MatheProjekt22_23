startwert = input("Startwert: ")
flostart = float(startwert)
def prozentsatz(wert):
    return wert / 100 
kirchensteuer = flostart * prozentsatz(8)
strkirch = str(kirchensteuer)
print ("Kirchensteuer: " + strkirch + " €")
Soli = flostart * prozentsatz(5)
strsoli = str(Soli)
print ("Solidaritätsbeitrag: " + strsoli + " €")
Lohnsteuer = flostart * prozentsatz(30)
strLohn = str(Lohnsteuer)
print ("Lohnsteuer: " + strLohn + " €")
Krank = flostart * prozentsatz(7.3)
strkra = str(Krank)
print ("Krankenkassenbeitrag: " + strkra + " €")
Arbeitslos = flostart * prozentsatz(1.25)
strArb = str(Arbeitslos)
print ("Arbeitslosenversicherung: " + strArb + " €")
Rent = flostart * prozentsatz(9.3)
strRent = str(Rent)
print ("Rentenversicherung: " + strRent + " € ")

mit = flostart - Soli - kirchensteuer - Lohnsteuer - Krank - Arbeitslos - Rent
rundeMit = round(mit)
strmit = str(rundeMit)
print ("Netto Gehalt mit Kirchensteuer: " + strmit + " €")

ohne = flostart - Soli - Lohnsteuer - Krank - Arbeitslos - Rent
rundeOhne = round(ohne)
strohne = str(rundeOhne)
print ("Netto Gehalt ohne Kirchensteuer: " + strohne + " €")

