import oop
from database import create_db

def main():
     try:
        create_db()
     except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    oop.start()
