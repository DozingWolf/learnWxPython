import wx
import windows_with_menubar


class mainFrame(windows_with_menubar.MyFrame1):
    def __init__(self,parent):
        windows_with_menubar.MyFrame1.__init__(self,parent)

    def exit_windows(self,event):
        exit()

app = wx.App()

frame = mainFrame(None)

frame.Show(True)

app.MainLoop()
