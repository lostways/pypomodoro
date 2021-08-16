import unittest

import datetime as dt

from pypomodoro.pomodoro import Pomodoro

class TestPomodoro(unittest.TestCase):

    def test_init(self):
        pom = Pomodoro(work_time=10,break_time=5)
        self.assertEqual(pom.work_secs,10 * 60)
        self.assertEqual(pom.break_secs,5 * 60)
        self.assertEqual(pom.pomo_number,1)
        self.assertEqual(pom.start_time,None)
        self.assertEqual(pom.break_end_time,None)
        self.assertEqual(pom.started,False)

    def test_start(self):
        pom = Pomodoro()
        pom.start()
        self.assertAlmostEqual(
            pom.start_time,
            dt.datetime.now(),
            delta=dt.timedelta(seconds=1)
        )
        self.assertEqual(
            pom.pomo_end_time,
            pom.start_time + dt.timedelta(seconds=pom.work_secs)
        )
        self.assertEqual(
            pom.break_end_time,
            pom.pomo_end_time + dt.timedelta(seconds=pom.break_secs)
        )
        self.assertEqual(pom.started, True)

    def test_get_state(self):
        pom = Pomodoro(work_time=10, break_time=5)
        self.assertEqual(pom.get_state(), "init")

        pom.start()
        self.assertEqual(pom.get_state(), "pomo")
        
        break_time = dt.datetime.now() + dt.timedelta(seconds=pom.work_secs + 5)

        #TODO Time travel to test state changes
        self.assertEqual(pom.get_state(), "break")
        self.assertEqual(pom.get_state(), "done")

if __name__ == '__main__':
    unittest.main()
