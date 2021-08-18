from dataclasses import dataclass, field
import datetime as dt

@dataclass
class Pomodoro:
    work_time: int
    break_time: int
    start_time: dt.datetime = field(init=False)
    pomo_end_time: dt.datetime = field(init=False)
    break_end_time: dt.datetime = field(init=False)
    pomo_number: int = field(default=1,init=False)
    started: bool = field(default=False,init=False)

    def start(self):
        work_secs = self.work_time * 60
        break_secs = self.break_time * 60

        self.start_time = self._get_time()
        self.pomo_end_time = self.start_time + dt.timedelta(seconds=work_secs)
        self.break_end_time = self.start_time + dt.timedelta(
            seconds=work_secs + break_secs
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
