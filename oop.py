""" object oriented way of main.py """
import oop_windows as win

def main():
    """ entry point of the program """
    main_window = win.Window("Main Fenster", "400x400", win.WindowType.MAIN)
    main_window.run()


if __name__ == "__main__":
    main()
