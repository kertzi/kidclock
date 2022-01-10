import wx

class ClockPanel(wx.Panel):
  def __init__(self, parent):
    super().__init__(parent)
     # set our minimum size based on the text with
    dc = wx.MemoryDC()
    self.text_width, self.text_height= (200, 200)
    # height and width are reversed since we are drawing text vertically
    self.SetMinSize((self.text_height,self.text_width)) 
    self.InitUI()

  def InitUI(self):
    self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.Bind(wx.EVT_PAINT, self.OnPaint)
    self.Bind(wx.EVT_SIZE, self.OnSize)
    
  
  def OnSize(self, event):
    dc = wx.AutoBufferedPaintDC(self)
    self.repaint(dc)
    event.Skip()

  def repaint(self, dc):
    width, height = self.GetClientSize()
    print(f"W: {width} H: {height}")
    
    dc.Clear()
    brush = wx.Brush("white")

    dc.SetTextForeground(wx.BLACK)
    font = wx.Font(20, wx.ROMAN, wx.ITALIC, wx.NORMAL)
    dc.SetFont(font)
    dc.DrawText("10:20", 200, 10)
    dc.SetPen(wx.Pen(wx.BLACK, 5))
    dc.DrawLine(10, 10, width, height)

  
  def OnPaint(self, event):
    dc = wx.AutoBufferedPaintDC(self)
    self.repaint(dc)
    event.Skip()


