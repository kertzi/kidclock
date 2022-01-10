import wx
import clock_panel

app_title = 'Kid Clock'

class MainFrame(wx.Frame):
  def __init__(self):
    super().__init__(parent=None, title=app_title)
    # self.SetClientSize(500,500)
    panel = wx.Panel(self)

    box_sizer = wx.BoxSizer(wx.VERTICAL)

    # self.text_ctrl = wx.TextCtrl(panel)
    # press_btn = wx.Button(panel, label='Click me')
    # press_btn.Bind(wx.EVT_BUTTON, self.press_btn_on_press)

    clock = clock_panel.ClockPanel(panel)
    box_sizer.Add(clock, 0, wx.ALL | wx.EXPAND, 1)

    # box_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
    # box_sizer.Add(press_btn, 0, wx.ALL | wx.CENTER, 5)
    # box_sizer.Add(clock, 0, wx.ALL | wx.EXPAND, 5)

    panel.SetSizer(box_sizer)

    self.Show()

  def press_btn_on_press(self, event):
    value = self.text_ctrl.GetValue()
    if not value:
      print("No value")
    else:
      print(f'You typed: "{value}"')


if __name__ == '__main__':
  app = wx.App()
  frame = MainFrame()
  frame.Show()
  app.MainLoop()