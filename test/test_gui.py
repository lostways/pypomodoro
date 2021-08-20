import unittest
import hashlib
import curses

from pypomodoro.gui import Gui

class TestGui(unittest.TestCase):
    
    def setUp(self):
        self.debug_text = None

        self.screen = curses.initscr()
        curses.start_color()
        self.gui = Gui(self.screen)

    def tearDown(self):
        curses.endwin()
        if self.debug_text:
            print("\n\n" + self.debug_text + "\n")

    def test_get_time_display(self):

        expected_hash = "ef8593c645d7f5954c1029f29da0641cf1cbba61"
        time_display = self.gui.get_time_display("01:23:04")
        time_display_hash = hashlib.sha1(time_display.encode()).hexdigest()
        self.assertEqual(time_display_hash, expected_hash)
        #self.debug_text = time_display_hash 

    def test_get_center_start(self):
        pass
