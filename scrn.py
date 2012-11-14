def scrn(scrnName):
    import win32gui, win32ui, win32con, win32api
    hwin = win32gui.GetDesktopWindow()
    
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    
    bmp = win32ui.CreateBitmap()
    #bmp.CreateCompatibleBitmap(memdc, width, height)
    bmp.CreateCompatibleBitmap(srcdc, width, height)

    memdc.SelectObject(bmp)

    
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    bmp.SaveBitmapFile(memdc, (scrnName))
    memdc.DeleteDC()
    win32gui.DeleteObject(bmp.GetHandle())

scrn('test111111.bmp')