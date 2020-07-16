#!/usr/bin/env python3
"""
Pomodoro
"""

__author__ = "Andrew Lowe"
__version__ = "0.1.0"
__license__ = "MIT"

import curses
import argparse
import time
import datetime as dt

def print_screen(screen,text):
  screen.addstr(0,0,text)
  screen.refresh()


class Pomodoro:

  def __init__(self,work_time=25,break_time=5):
    self.work_secs=work_time*60
    self.break_secs=break_time*60
    self.breaks = 0

  def start(self):
    self.start_time = dt.datetime.now()
    self.pomo_end_time = self.start_time + dt.timedelta(seconds=self.work_secs)
    self.break_end_time = self.start_time + dt.timedelta(seconds=self.work_secs+self.break_secs)
  
  def get_state(self):
    now = dt.datetime.now()

    if now < self.pomo_end_time:
      return "pomo"
    elif now <= self.break_end_time:
      return "break"
    else:
      return "done"

  def restart(self):
    self.breaks += 1
    self.start()

def init_args():
  """ This is executed when run from the command line """
  parser = argparse.ArgumentParser()

  # Required positional argument
  #parser.add_argument("arg", help="Required positional argument")

  # Optional argument flag which defaults to False
  parser.add_argument("-f", "--flag", action="store_true", default=False)

  # Optional argument which requires a parameter (eg. -d test)
  parser.add_argument("-n", "--name", action="store", dest="name")

  # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
  parser.add_argument(
      "-v",
      "--verbose",
      action="count",
      default=0,
      help="Verbosity (-v, -vv, etc)")

  # Specify output of "--version"
  parser.add_argument(
      "--version",
      action="version",
      version="%(prog)s (version {version})".format(version=__version__))

  args = parser.parse_args()
  return args

args = init_args()

def main(screen=None):

  if not screen : curses.wrapper(main)
  else:
    #print(args)
    pomo = Pomodoro(1,2)
    pomo.start()
    screen.clear()
    while True:
      # Pomodora started
      pom_end_time = pomo.pomo_end_time
      pom_state = pomo.get_state()
      pom_start_time = pomo.start_time
      print_screen(screen,f'{pom_state} and {pom_end_time} - start is {pom_start_time}')
      screen.refresh()
      time.sleep(5)

if __name__ == "__main__": main()
