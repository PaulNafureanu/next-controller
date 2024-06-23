import win32gui
import win32con


class WinApp:

    @staticmethod
    def selectApp(name: str):
        appWindow = None
        appTitle = None

        # Get all the window handlers and store the app handler
        def enum_windows_callback(windowHandler, windows: list):
            if win32gui.IsWindowVisible(windowHandler):
                nonlocal appWindow, appTitle
                title = win32gui.GetWindowText(windowHandler).lower()
                windows.append((windowHandler, title))
                if name.lower() in title:
                    appWindow = windowHandler
                    appTitle = title

        windows = []
        win32gui.EnumWindows(enum_windows_callback, windows)

        # win32gui.SetForegroundWindow(appWindow)
        if appWindow:
            # If the window is minimized, restore it
            if win32gui.IsIconic(appWindow):
                win32gui.ShowWindow(appWindow, win32con.SW_RESTORE)
            # Bring the window to the foreground
            win32gui.SetForegroundWindow(appWindow)
            # Sometimes, SetForegroundWindow might need additional focus commands
            win32gui.SetWindowPos(
                appWindow,
                win32con.HWND_TOPMOST,
                0,
                0,
                0,
                0,
                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
            )
            win32gui.SetWindowPos(
                appWindow,
                win32con.HWND_NOTOPMOST,
                0,
                0,
                0,
                0,
                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
            )

        return (appWindow, appTitle)
