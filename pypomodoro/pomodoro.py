import datetime as dt


class Pomodoro:
    def __init__(self, work_time=25, break_time=5):
        self.work_secs = work_time * 60
        self.break_secs = break_time * 60
        self.pomo_number = 1
        self.start_time = None
        self.pomo_end_time = None
        self.break_end_time = None
        self.started = False

    def start(self):
        self.start_time = self._get_time()
        self.pomo_end_time = self.start_time + dt.timedelta(seconds=self.work_secs)
        self.break_end_time = self.start_time + dt.timedelta(
            seconds=self.work_secs + self.break_secs
        )
        self.started = True

    def get_state(self):
        if self.started == False:
            return "init"

        now = self._get_time()

        if now < self.pomo_end_time:
            return "pomo"
        elif now <= self.break_end_time:
            return "break"
        else:
            return "done"

    def restart(self):
        self.pomo_number += 1
        self.start()

    def _get_time(self) -> dt.datetime:
        return dt.datetime.now()
