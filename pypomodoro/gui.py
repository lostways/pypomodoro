"""
Gui classs: handles printing to the screen and user input
"""
import curses

class Gui:

    def __init__(self,screen):
        self.screen = screen

    def get_time_display(self,time_text) -> str:
      a = "####" 
      b = "#  #"
      c = "#   "
      d = "   #"
      o = "   "
      x = " # "

        
                   # 0,1,2,3,4,5,6,7,8,9,:
      templates = [ [a,d,a,a,b,a,a,a,a,a,o],
                    [b,d,d,d,b,c,c,d,b,b,x],
                    [b,d,a,a,a,a,a,d,a,a,o],
                    [b,d,c,d,d,d,b,d,b,d,x],
                    [a,d,a,a,d,a,a,d,a,a,o] ]

      out = ""
      for row in templates: 
        for digit in time_text:
          if digit == ":":
            digit = 10
          else:
            digit = int(digit,10)
          out = out + row[digit] + " "
        out = out + "\n"

      return out
      
    def print_screen(self,text):
      x = 0
      y = 0

      num_rows, num_cols = self.screen.getmaxyx()
      middle_row = int(num_rows / 2)
      middle_col = int(num_cols / 2)
     

      lines = text.rstrip("\n").split("\n")
      longest_line = max(map(len,lines))

      y = middle_row - int(len(lines) / 2)
      x = middle_col - int(longest_line / 2)

      for line in lines:
        self.screen.addstr(y,x,line + "\n", curses.color_pair(1))
        y = y + 1
      self.screen.refresh()

    def handle_screen_input(self):
      try:
        key = self.screen.getkey()
      except curses.error as e:
        if str(e) == 'no input': return ''
        raise e
      return key
