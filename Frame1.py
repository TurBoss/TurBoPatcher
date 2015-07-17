#Boa:Frame:Frame1

import wx
import bsdiff4

genOriginalBytes = ""
genModifiedBytes = ""

patchOriginalBytes = ""
patchFilePatch = ""

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON6, 
 wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(10)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(401, 331), size=wx.Size(400, 250),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(392, 223))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(392, 223),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Original',
              name='button1', parent=self.panel1, pos=wx.Point(64, 48),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Modified',
              name='button2', parent=self.panel1, pos=wx.Point(168, 48),
              size=wx.Size(75, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'Go',
              name='button3', parent=self.panel1, pos=wx.Point(272, 48),
              size=wx.Size(75, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'Original',
              name='button4', parent=self.panel1, pos=wx.Point(64, 128),
              size=wx.Size(75, 23), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label=u'Patch',
              name='button5', parent=self.panel1, pos=wx.Point(168, 128),
              size=wx.Size(75, 23), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BUTTON5)

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6, label=u'Go',
              name='button6', parent=self.panel1, pos=wx.Point(272, 128),
              size=wx.Size(75, 23), style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_FRAME1BUTTON6)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Generate Patch', name='staticText1', parent=self.panel1,
              pos=wx.Point(40, 24), size=wx.Size(75, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Patch File', name='staticText2', parent=self.panel1,
              pos=wx.Point(40, 104), size=wx.Size(46, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        global genOriginalBytes
        event.Skip()
        dlg = wx.FileDialog(self, 'Choose a original file', '.', '', '*', wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                
                originalFile = open(filename,'rb')
                genOriginalBytes = originalFile.read()
                originalFile.close()
                
        finally:
            dlg.Destroy()

    def OnButton2Button(self, event):
        global genModifiedBytes
        event.Skip()
        dlg = wx.FileDialog(self, 'Choose a modified file', '.', '', '*', wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                
                modifiedFile = open(filename,'rb')
                genModifiedBytes = modifiedFile.read()
                modifiedFile.close()
                
        finally:
            dlg.Destroy()

    def OnButton3Button(self, event):
        event.Skip()
        dlg = wx.FileDialog(self, 'Save a patch', '.', '', '*.patch', wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                
                destinationPatch = open(filename,'wb')
                patchFile = bsdiff4.diff(bytes(genOriginalBytes), bytes(genModifiedBytes))
                
                destinationPatch.write(patchFile)
                destinationPatch.close()
                
                
        finally:
            dlg.Destroy()

    def OnButton4Button(self, event):
        global patchOriginalBytes
        event.Skip()
        dlg = wx.FileDialog(self, 'Choose a original file', '.', '', '*', wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                
                originalFile = open(filename,'rb')
                patchOriginalBytes = originalFile.read()
                originalFile.close()
                
        finally:
            dlg.Destroy()

    def OnButton5Button(self, event):
        global patchFilePatch
        event.Skip()
        dlg = wx.FileDialog(self, 'Choose a patch file', '.', '', '*.patch', wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                
                patchFile = open(filename,'rb')
                patchFilePatch = patchFile.read()
                patchFile.close()
                
        finally:
            dlg.Destroy()

    def OnButton6Button(self, event):
        event.Skip()
        dlg = wx.FileDialog(self, 'Save patched', '.', '', '*', wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                
                destinationFile = open(filename,'wb')
                
                patchFile = bsdiff4.patch(bytes(patchOriginalBytes),patchFilePatch)
                destinationFile.write(patchFile)
                destinationFile.close()
                
        finally:
            dlg.Destroy()
