# Pflichtenheft zum Mathe Projekt 2022/2023 im Fach Informatik
### Von Thomas Zimmer & Finn Lasse Scholze

## Zielbestimmung
* Es soll eine Datenbank zum Speichern von usern da sein
* Es soll dem User die Mathematik näher gebracht werden
* Die Software soll die Möglichkeit haben an einen Graph ran zu zoomen oder weg zu zoomen
* Die funktionen sollen graphisch dargestellt werden 
* Schnittpunkte und Nullstellen sollen ausgerechnet werden, und angezeig werden
* Die Achsen des Koordinatensystems sollen Variabel bezeichnet werden

## Einsatz
* Die Zielgruppe von der Software sind Matheinteressierte Menschen
* Die Software soll begleitend im Matheuntericht benutzt werden


## Produktübersicht
* Diese Software wird von Thomas Zimmer & Finn Lasse Scholze erstellt
* Die Software Besitzt eine Oberfläche, auf der der User Funktionen ausrechnen kann, und diese dann Grafisch angezeigt bekommt. Mit informationen über diese 

## Funktionen
+ Der User kann sich am Anfang anmelden oder einen Account erstellen
+ Die Software kann folgende Mathefunktionen berechnen:
    + Lineare Funktionen
    + Quadratische Funktionen
    + Ganzrationale Funktionen
    + Trigonometrische Funktionen 
    + Exponentialfunktionen
    + Einstieg Differenzialrechnung
    + Kurvendiskussion
    + Integralrechnung
+ Diese Können im Jeweiligen Menüpunkt ausgewählt werden
+ Hilfe zu den Jeweiligen Funktionen können jederzeit aufgerufen werden

## Leistungen
* Das Projekt soll bis zum 14.04.2023 fertig werden
* Werte werden in Floats gespeichert

## Qualitätsanforderungen
* Die Software soll möglich scnell zu bedienen sein
* Außerdem soll die Software möglichst schnell laufen 

## Benutzeroberfläche
* Die Oberfläche der Software wird wie eine standart Oberfläche ausehen:
    * Kopfzeilen Menü mit den punkten: Funktionen Account und Hilfe
    * Jede Funktion besitzt ein eigenes Fenster in dem Input Felder sind, und das Koordinatensystem in dem die Funktion angezeigt wird
    * Unter dem Punkt Hilfe findet der User ein eigenes Fenster mit Hilfe

## Technisches Umfeld
* Als Programmiersprache wird Python verwendet mit den Folgenden Bibilotheken:
    * numpy
    * matplotlib
    * threading
    * re
    * tkinter
    * sqlite3
    * sys
    * os
* Nach der ersten benutzung braucht der Nutzer keine Internet verbindung, da die Datenbank auf dem System selbst als Datei läuft. Und die Pakete beim ersten mal runtergeladen werden wenn diese nicht vorhanden sein sollten.

## Gliederung
* Jede Fuktion hat ein eigenes Fenster, so kann während der Entwicklung jeweils eine einzige Funktion erstellt werden. 

## Ergänzungen
* Die Komplette Software wird OpenSource auf Github veröffentlicht github.com/hyperbel/MatheProjekt22_23 
* Die Software wird unter der GPL_2.0 Lizenz veröffentlicht

## Tests
* Nach dem erstellen einer Funktion wird diese getestet
* Zum Ende der entwicklung wird die Software komplett getestet, um Bugs und andere Probleme z.B. rechen Fehler zu verhindern.