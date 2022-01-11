import configparser
import datetime

class Config:
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read(filenames=['config.ini'])

  def remove_invalid_chars(self, str):
    result = str.strip('"')
    print(f'result after 1: {result}')

    if str.startswith('0') and not str.endswith('0'):
      result = result[1:]

    print(f'result after 2: {result}')
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