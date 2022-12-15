import os, sys, sqlite3


def create_db():
	# Prüfen ob Datenbank schon da ist
	if os.path.exists("mathe.db"):
		print("Datei bereits vorhanden")
		sys.exit(0)

	con = sqlite3.connect("mathe.db")
	cur = con.cursor()
	
	# Tabelle user erstellen
	sql = "CREATE TABLE user (" \
	      "userID INT, " \
	      "username TEXT, "  \
	      "passwort TEXT);"
	cur.execute(sql)
	con.commit()
	con.close()
