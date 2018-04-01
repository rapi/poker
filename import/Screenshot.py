import win32gui
from PIL import ImageGrab

class Screenshot:
    def __init__(self):
        self.windows=[]
        self.title=''
        self.dir='Screenshots/'
        print('init Screenshot')
    def make(self,title):
        self.title=title
        win32gui.EnumWindows(self.foreach_window,0)
        print(self.windows)

        for w in self.windows:
            main=win32gui.GetDesktopWindow()
            win32gui.SetForegroundWindow(w)
            bbox = win32gui.GetWindowRect(w)
            img = ImageGrab.grab(bbox)
            img.save()


    def foreach_window(self,hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            text=win32gui.GetWindowText(hwnd)
            if text.upper().find(self.title.upper())>-1:
                self.windows.append(hwnd)
