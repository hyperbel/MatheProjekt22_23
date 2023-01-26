import oop_windows as win


# create a main function
def main():
    # create a window
    mainWindow = win.Window("Main Fenster", "400x400", win.WindowType.Main)
    mainWindow.run()


# call main function
if __name__ == "__main__":
    main()
