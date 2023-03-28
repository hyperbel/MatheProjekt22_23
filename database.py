""" Erstellt Datenbank """
import sqlite3

def create_db():
    """ Erstellt Datenbank """
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()

    # Tabelle user erstellen

    # MM-DD-YYYY HH:MM
    sql = "CREATE TABLE user (" \
          "username TEXT, "  \
          "passwort TEXT);"
    cur.execute(sql)
    con.commit()
    sql = "CREATE TABLE funktionen (" \
          "funktion TEXT, "	\
          "zeit TEXT, "	\
          "userid INTEGER);"
    cur.execute(sql)
    con.commit()
    con.close()
