startwert = input("Startwert: ")
flostart = float(startwert)
def prozentsatz(wert):
    return wert / 100 
kirchensteuer = flostart * prozentsatz(8)
strkirch = str(kirchensteuer)
Soli = flostart * prozentsatz(5)
strsoli = str(Soli)
Lohnsteuer = flostart * prozentsatz(30)
strLohn = str(Lohnsteuer)
Krank = flostart * prozentsatz(7.3)
strkra = str(Krank)
Arbeitslos = flostart * prozentsatz(1.25)
strArb = str(Arbeitslos)
Rent = flostart * prozentsatz(9.3)
strRent = str(Rent)
print ("Rentenversicherung: " + strRent + " € " + " Arbeitslosenversicherung: " + strArb + " €" + " Krankenkassenbeitrag: " + strkra + " €" + " Lohnsteuer: " + strLohn + " €" + " Solidaritätsbeitrag: " + strsoli + " €" + " Kirchensteuer: " + strkirch + " €")

mit = flostart - Soli - kirchensteuer - Lohnsteuer - Krank - Arbeitslos - Rent
rundeMit = round(mit)
strmit = str(rundeMit)
print ("Netto Gehalt mit Kirchensteuer: " + strmit + " €")

ohne = flostart - Soli - Lohnsteuer - Krank - Arbeitslos - Rent
rundeOhne = round(ohne)
strohne = str(rundeOhne)
print ("Netto Gehalt ohne Kirchensteuer: " + strohne + " €")

ohneSoliMitKirche = flostart - kirchensteuer - Lohnsteuer - Krank - Arbeitslos - Rent
rundeohneSoliMitKirche = round(ohneSoliMitKirche)
srSMK = str(rundeohneSoliMitKirche)
print ("Netto Gehalt Ohne Soli mit Kirche: " + srSMK + " €")

ohneSoliOhneKirche = flostart - kirchensteuer - Lohnsteuer - Krank - Arbeitslos - Rent
rundeohneSoliOhneKirche = round(ohneSoliOhneKirche)
srSOK = str(rundeohneSoliOhneKirche)
print ("Netto Gehalt Ohne Soli und Ohne Kirche: " + srSOK + " €")



