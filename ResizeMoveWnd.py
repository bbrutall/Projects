import win32gui

APP_TITLE_NAME = 'C:\Python27\python.exe'               #Title of windows application

windows_titles=[]
windows_long_int = []
app_titles = []

def Callback(hWnd, windows_long_int):
    windows_long_int.append(hWnd)
    windows_titles.append(win32gui.GetWindowText(hWnd))

def UpdateList(app_title, long_int, titles, current_titles):
    win32gui.EnumWindows(Callback, long_int)
    for ints, names in zip(long_int, titles):
        if names == app_title:
            current_titles.append(ints)

def MoveResizeWindow(x, y, width, height, indent_x, indent_y):
    for element in app_titles:
        x += indent_x
        y += indent_y
        win32gui.MoveWindow(element, x, y, width, height, True)

UpdateList(APP_TITLE_NAME, windows_long_int, windows_titles, app_titles)

if len(app_titles) == 1:                                #Number of running clients
    MoveResizeWindow(2000, 50, 1500, 930, 200, 100)     #MoveResizeWindow(coordinate X, coordinate Y, width, height, indent-right, indent-down)
elif len(app_titles) == 2:
    MoveResizeWindow(1525, -275, 1300, 850,  400, 300)
elif len(app_titles) >= 3:
    MoveResizeWindow(1625, -75, 1280, 800,  300, 100)
