import wx

mainAPP = wx.App()

mainWindows = wx.Frame(None,title='wxPython Hello world!',size=(400,300))

mainPanel = wx.Panel(mainWindows)

mainLabel = wx.StaticText(mainPanel,label='Hello World!',pos=(100,100))

mainWindows.Show(True)

mainAPP.MainLoop()
