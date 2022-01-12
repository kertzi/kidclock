import configparser
import datetime

from wx.core import Log, LogError, LogWarning

class Config:
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read(filenames=['config.ini'])

  def remove_invalid_chars(self, str):
    result = str.strip('"')

    if str.startswith('0') and not str.endswith('0'):
      result = result[1:]

    return result

  def get_wakeup_time(self):
    time_str = self.config.get('general', 'WakeUpTime')
    hour_str, min_str = time_str.split(':')

    hour_str = self.remove_invalid_chars(hour_str)
    min_str = self.remove_invalid_chars(min_str)

    hour = int(hour_str)
    min = int(min_str)
    
    dt = datetime.time(hour=hour, minute=min)

    return dt

  def get_sleep_time(self):
    time_str = self.config.get('general', 'SleepTime')
    hour_str, min_str = time_str.split(':')

    hour_str = self.remove_invalid_chars(hour_str)
    min_str = self.remove_invalid_chars(min_str)

    hour = int(hour_str)
    min = int(min_str)

    dt = datetime.time(hour=hour, minute=min)
    return dt

  def get_clock_font_size(self):
    try:
      size_str = self.config.get('general', 'ClockFontSize')
      return int(size_str.strip('"'))
    except configparser.NoOptionError as noOpt:
      LogWarning("ClockFontSize option missing from config.ini, using default")
      return 50
    