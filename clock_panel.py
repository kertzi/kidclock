import wx
import datetime

# Contrast picker: https://www.thoughtco.com/contrasting-foreground-background-colors-4061363

# For Green background
GRAY_COLOR = wx.Colour(105,105,105)
# For Red background
YELLOW_COLOR = wx.Colour(255,238,0)

class ClockPanel(wx.Panel):
  def __init__(self, parent, wakeup_time, sleep_time, font_size=50):
    super().__init__(parent)
    # set our minimum size based on the text with
    dc = wx.MemoryDC()
    self.width, self.height= (200, 200)
    # height and width are reversed since we are drawing text vertically
    self.SetMinSize((self.height,self.width)) 
    self.wakeup_time = wakeup_time
    self.sleep_time = sleep_time
    self.bg_colour = wx.Colour(0,0,0)
    self.fg_colour = GRAY_COLOR
    self.font_size = font_size

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

  def SetWakeupColours(self):
    self.bg_colour = wx.GREEN
    self.fg_colour = GRAY_COLOR

  def SetSleepColours(self):
    self.bg_colour = wx.RED
    self.fg_colour = YELLOW_COLOR

  def OnTimer(self, event):
    dc = wx.AutoBufferedPaintDC(self)

    now= datetime.datetime.now()
    now = datetime.datetime(2022,1,12,7,5,1)

    sleep = now.replace(hour=self.sleep_time.hour, minute=self.sleep_time.minute, second=0)
    wakeup = now.replace(hour=self.wakeup_time.hour, minute=self.wakeup_time.minute, second=0)

    if now > wakeup and now < sleep:
      # in wakeup time
      self.SetWakeupColours()
    else:
      # in sleep time
      self.SetSleepColours()

    self.Repaint(dc)

  def Repaint(self, dc):
    width, height = self.GetClientSize()
    
    font = wx.Font(wx.FontInfo(self.font_size).Family(wx.FONTFAMILY_ROMAN).Bold())
    dc.SetFont(font)

    time_str = self.GetTimeStr()
    text_width, text_height = dc.GetTextExtent(time_str)

    text_x = (width / 2) - (text_width / 2)
    text_y = (height / 2) - (text_height / 2)
    
    dc.Clear()
    dc.SetTextForeground(self.fg_colour)
    self.SetBackgroundColour(self.bg_colour)
    dc.DrawText(time_str, text_x, text_y)

  def GetTimeStr(self):
    dt = datetime.datetime.now()
    return dt.strftime("%H:%M:%S")
  
  def OnPaint(self, event):
    dc = wx.AutoBufferedPaintDC(self)
    self.Repaint(dc)
    event.Skip()


