#!/usr/bin/env python
import wx, random

class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title, pos):
        wx.Frame.__init__(self, parent, title=title, pos=pos)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.control.AppendText("Welcome to the first dimension. Choose your path... choose it wisely. And remember: Whatever I forgot.")
        self.button = wx.Button(self, -1, "East")
        self.buttonb = wx.Button(self, -1, "West")
        sizer.Add(self.control, 4, wx.EXPAND)
        sizer.Add(self.button, 1, 1, wx.EXPAND)
        sizer.Add(self.buttonb, 1,6, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        self.SetSizer(sizer)
        self.SetSize(self.GetBestSize())
        self.Show(True)
    
    def OnButton(self, event):
        text = self.control.GetValue()
        if text:
            dialog = wx.MessageDialog(self, caption="Message", message=text)
            dialog.ShowModal()

app = wx.App(False)
MyFrame(None, 'The Path', pos=(100,100))
app.MainLoop()

