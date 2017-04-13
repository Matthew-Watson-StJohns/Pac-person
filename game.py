import game_interface, game_model, tkinter


def main():
    root = tkinter.Tk()
    root.geometry("800x600+300+300")
    app = game_interface.MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
