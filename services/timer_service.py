import threading
import time

import flet as ft


class Count(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.running = False
        self.hour = 0
        self.min = 0
        self.sec = 0

    def start_count(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def stop_counter(self):
        self.running = False

    def update_timer(self):
        elapsed_seconds = 0
        while self.running:
            hours = elapsed_seconds // 3600
            minutes = (elapsed_seconds % 3600) // 60
            seconds = elapsed_seconds % 60

            self.hour = "{:02d}".format(hours)
            self.min = "{:02d}".format(minutes)
            self.sec = "{:02d}".format(seconds)

            self.count.value = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.update()

            elapsed_seconds += 1

            time.sleep(1)

    def build(self):
        self.count = ft.Text("{:02d}:{:02d}:{:02d}".format(self.hour, self.min, self.sec))
        return self.count
