import wx

import clock_panel
import configuration

app_title = 'Kid Clock'

class MainFrame(wx.Frame):
  def __init__(self):
    super().__init__(parent=None, title=app_title)
    # self.SetClientSize(500,500)
    panel = wx.Panel(self)

    # sizer = wx.BoxSizer(wx.VERTICAL)
    sizer = wx.GridSizer(1, 1, 1)

    # self.text_ctrl = wx.TextCtrl(panel)
    # press_btn = wx.Button(panel, label='Click me')
    # press_btn.Bind(wx.EVT_BUTTON, self.press_btn_on_press)
    config = configuration.Config()
    wakeup = config.get_wakeup_time()
    sleep = config.get_sleep_time()

    print(f'wakeup hour {wakeup.hour} min {wakeup.minute}')
    print(f'sleep hour {sleep.hour} min {sleep.minute}')

    clock = clock_panel.ClockPanel(panel, wakeup_time=wakeup, sleep_time=sleep)
    sizer.Add(clock, 0, wx.ALL | wx.EXPAND, 1)

    # box_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
    # box_sizer.Add(press_btn, 0, wx.ALL | wx.CENTER, 5)
    # box_sizer.Add(clock, 0, wx.ALL | wx.EXPAND, 5)

    panel.SetSizer(sizer)

    self.Show()


if __name__ == '__main__':
  app = wx.App()
  frame = MainFrame()
  frame.Show()
  app.MainLoop()