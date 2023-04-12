"""Main Wrapper Datei für das gesamte Programm"""
import oop
from database import create_db

def main():
    """Main Funktion"""
     try:
        create_db()
     except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    oop.start()
