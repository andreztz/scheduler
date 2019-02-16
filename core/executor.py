import json
import threading
import time
import schedule
from core.pluginsys import PLUGINS


def job(**kwargs):
    for plug in PLUGINS:
        plugin = plug.Plugin(**kwargs)
        plugin.run()


def run_threaded(job_func, **kwargs):
    job_thread = threading.Thread(target=job_func, kwargs=kwargs)
    job_thread.start()


def main():

    with open("data.json") as f:
        list_obj = json.load(f)

    for item in list_obj:
        schedule.every().day.at(item.get("time")).do(run_threaded, job, **item)

    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
