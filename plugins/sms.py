"""
https://www.twilio.com/
"""

import collections
import os

from twilio.rest import Client

cfg = {
    "accountSID": os.environ.get("accountSID"),
    "authToken": os.environ.get("authToken"),
    "myTwilioNumber": os.environ.get("myTwilioNumber"),
    "myCellPhone": os.environ.get("MYCELL"),
}


class Sms(object):
    def __init__(self, arg, **kwargs):
        try:
            twilioCli = Client(cfg["accountSID"], cfg["authToken"])
            message = twilioCli.messages.create(
                body=arg.msg, from_=cfg["myTwilioNumber"], to=cfg["myCellPhone"]
            )
        except Exception as exc:
            print(exc)


class Plugin:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name")
        self.time = kwargs.get("time")
        self.messages = kwargs.get("messages")
        self.path = kwargs.get("path")

    def run(self, **kwargs):
        arg = collections.namedtuple("arg", ["msg"])
        arg.msg = f"{self.time}:: {self.messages} - {self.name}"
        Sms(arg, **cfg)
