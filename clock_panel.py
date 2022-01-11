import wx
import datetime

class ClockPanel(wx.Panel):
  def __init__(self, parent, wakeup_time, sleep_time):
    super().__init__(parent)
     # set our minimum size based on the text with
    dc = wx.MemoryDC()
    self.width, self.height= (200, 200)
    # height and width are reversed since we are drawing text vertically
    self.SetMinSize((self.height,self.width)) 
    self.wakeup_time = wakeup_time
    self.sleep_time = sleep_time
    self.bg_colour = wx.GREEN

    self.InitUI()
    self.InitTimer()

  def InitUI(self):
    self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.SetBackgroundColour(self.bg_colour)
    self.Bind(wx.EVT_PAINT, self.OnPaint)
    self.Bind(wx.EVT_SIZE, self.OnSize)

  def InitTimer(self):
    self.timer = wx.Timer(self)
    self.Bind(wx.EVT_TIMER, self.OnTimer)
    self.timer.Start(1000)
  
  def OnSize(self, event):
    dc = wx.AutoBufferedPaintDC(self)
    
    self.Repaint(dc)
    event.Skip()

  def OnTimer(self, event):
    dc = wx.AutoBufferedPaintDC(self)

    now_time = datetime.datetime.now().time()
    now_time = datetime.datetime(2022,1,11,20,1,0).time()
    if now_time > self.sleep_time:
      self.bg_colour = wx.RED
    
    if now_time > self.wakeup_time:
      self.bg_colour = wx.GREEN

    self.Repaint(dc)

  def Repaint(self, dc):
    width, height = self.GetClientSize()
    
    font = wx.Font(wx.FontInfo(50).Family(wx.FONTFAMILY_ROMAN).Bold())
    dc.SetFont(font)

    time_str = self.GetTimeStr()
    text_width, text_height = dc.GetTextExtent(time_str)

    text_x = (width / 2) - (text_width / 2)
    text_y = (height / 2) - (text_height / 2)
    
    dc.Clear()
    dc.SetTextForeground(wx.WHITE)
    dc.DrawText(time_str, text_x, text_y)

  def GetTimeStr(self):
    dt = datetime.datetime.now()
    return dt.strftime("%H:%M:%S")
  
  def OnPaint(self, event):
    dc = wx.AutoBufferedPaintDC(self)
    self.Repaint(dc)
    event.Skip()


