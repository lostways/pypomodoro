#!/usr/bin/env python3
"""
Pomodoro
"""

__author__ = "Andrew Lowe"
__version__ = "0.6.1"
__license__ = "MIT"

import curses
import argparse
import time
import datetime as dt

from pomodoro import Pomodoro
from gui import Gui

def init_args():
  """ This is executed when run from the command line """
  parser = argparse.ArgumentParser()

  parser.add_argument("-w", "--work", default=25, type=float, action="store", dest="work_mins", help="Number of miinutes for work")
  parser.add_argument("-b", "--break", default=5, type=float, action="store", dest="break_mins", help="Number of minutes for break")
  parser.add_argument("-v", "--verbose", action="store_true", help="Move detailed display")
  
  # Specify output of "--version"
  parser.add_argument(
      "--version",
      action="version",
      version="%(prog)s (version {version})".format(version=__version__))

  args = parser.parse_args()
  return args


def main(screen=None):
  state_text = {
      'pomo' : 'Time to work',
      'break': 'Take a break',
      'done': 'Press space to get back to work',
      'init': 'Press space to start work'
  }
  time_left_init = "00:00:00"

  args = init_args()
  
  if not screen : curses.wrapper(main)
  else:
    #print(args)
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    screen.nodelay(True)

    pomo = Pomodoro(args.work_mins,args.break_mins)
    gui = Gui(screen)

    screen.clear()
    while True:
      pom_state = pomo.get_state()

      key_pressed = gui.handle_screen_input()

      if key_pressed == 'q':
        exit(0);

      now = dt.datetime.now()
      pom_end_time = pomo.pomo_end_time
      break_end_time = pomo.break_end_time
      pom_start_time = pomo.start_time

      if pom_state == "init":
        time_left = time_left_init
        if key_pressed == ' ':
          pomo.start()
          continue
      elif pom_state == "pomo":
        time_left = pom_end_time - now
      elif pom_state == "done":
        time_left = time_left_init
        if key_pressed == ' ':
          pomo.restart()
          continue
      else :
        time_left = break_end_time - now

      display_info = state_text[pom_state]

      if key_pressed != '':
        display_info = "Press 'q' to quit"
      
      if args.verbose and pom_state != "init":
        display_info += "\n" + f"Pomo number: {pomo.pomo_number}"
        display_info += "\n" + f"Pomo end time: {pomo.pomo_end_time:%H:%M:%S}"
        display_info += "\n" + f"Break end time: {pomo.break_end_time:%H:%M:%S%z}"
      time_left = str(time_left).split(".")[0]
      time_left = "{:0>8}".format(time_left)
      display_text = gui.get_time_display(time_left)
      display_text = display_text + "\n" + display_info
      gui.print_screen(display_text)
      time.sleep(1)

if __name__ == "__main__": main()
