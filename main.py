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
import pyfiglet

def print_screen(screen,text,center=True):
  x = 0
  y = 0

  if center == True :
    num_rows, num_cols = screen.getmaxyx()
    middle_row = int(num_rows / 2)
    middle_col = int(num_cols / 2)

    lines = text.rstrip("\n").split("\n")
    longest_line = max(map(len,lines))

    y = middle_row - int(len(lines) / 2)
    x = middle_col - int(longest_line / 2)

  for line in lines:
    screen.addstr(y,x,(" " * 10) + line + (" " * 10) + "\n", curses.color_pair(1))
    y = y + 1
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
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

    pomo = Pomodoro(1,2)
    pomo.start()
    screen.clear()
    while True:
      # Pomodora started
      now = dt.datetime.now()
      pom_end_time = pomo.pomo_end_time
      break_end_time = pomo.break_end_time
      pom_state = pomo.get_state()
      pom_start_time = pomo.start_time
      if pom_state == "pomo":
        time_left = pom_end_time - now
      else :
        time_left = break_end_time - now
      time_left = str(time_left).split(".")[0]
      time_left_text = pyfiglet.figlet_format(f'{time_left}',font="block")
      print_screen(screen,time_left_text)
      time.sleep(1)

if __name__ == "__main__": main()
