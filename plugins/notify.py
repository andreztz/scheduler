from notify import Notification


class Plugin:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.time = kwargs.get("time")
        self.messages = kwargs.get("message")
        self.path = kwargs.get("path")

    def run(self, **kwargs):
        msg = f"{self.time}:: {self.messages} - {self.name}"
        Notification("new message", msg)
