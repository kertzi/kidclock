import wx

import clock_panel
import configuration

app_title = 'Kid Clock'

class MainFrame(wx.Frame):
  def __init__(self):
    super().__init__(parent=None, title=app_title)
    # self.SetClientSize(500,500)
    panel = wx.Panel(self)

    sizer = wx.GridSizer(1, 1, 1)

    config = configuration.Config()
    wakeup = config.get_wakeup_time()
    sleep = config.get_sleep_time()
    font_size = config.get_clock_font_size()

    print(f'wakeup time: {wakeup.hour}:{wakeup.minute}')
    print(f'sleep time: {sleep.hour}:{sleep.minute}')

    clock = clock_panel.ClockPanel(panel, wakeup_time=wakeup, sleep_time=sleep, font_size=font_size)
    sizer.Add(clock, 0, wx.ALL | wx.EXPAND, 5)

    panel.SetSizer(sizer)

    self.Show()


if __name__ == '__main__':
  app = wx.App()
  frame = MainFrame()
  frame.Show()
  app.MainLoop()