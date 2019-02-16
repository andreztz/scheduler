"""
https://www.twilio.com/
"""

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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Evia Sms",
        usage="%(prog)s [opções]",
        epilog='ex.: %(prog)s --sms "Olá Mundo"',
    )
    parser.add_argument("--msg", metavar="msg", type=str, help='"Um texto entre aspas"')

    arg = parser.parse_args()

    sms = Sms(arg, **cfg)
