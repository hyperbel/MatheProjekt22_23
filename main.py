import oop
import database

def main():
     try:
        create_db()
     except:
        print("Datenbank sollte schon da sein")

if __name__ == "__main__":
    main()