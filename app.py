from src.gui.start import Application
from src.win.apps import WinApp


if __name__ == "__main__":
    app = Application(
        title="Next Controller", themename="vapor", size=[600, 400], minsize=[600, 400]
    )
    app.position_center()
    app.mainloop()

    # WinApp.selectApp('chrome')
