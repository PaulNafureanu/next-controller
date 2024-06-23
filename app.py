from gui.start import Application


if __name__ == "__main__":
    app = Application(
        title="Next Controller", themename="vapor", size=[600, 400], minsize=[600, 400]
    )
    app.position_center()
    app.mainloop()
