import pysftp
import os
import sys
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

user = None
pwd = None
host = None
dest = None
files_to_monitor = []

def upload(file):
    if (file.split("/")[-1] in files_to_monitor):
        print("[%d] Watchdog - %s." % (random.randint(1000, 9999),file))
        srv = pysftp.Connection(host=host, username=user,password=pwd)

        with srv.cd(dest):  # chdir
            srv.put(file)  # upload file

        srv.close()  # Closes the connection

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if (event.event_type == 'created') or (event.event_type == 'modified'):
            # print("Watchdog received modified event - % s. [%d]" % (event.src_path, random.randint(1000, 9999)))
            if (user is not None):
                upload(event.src_path)



class GenericWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = Handler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )

if __name__ == "__main__":
    with open("../files_to_monitor.txt", "r") as ff:
        for i in ff:
            files_to_monitor += [i.replace("\n","")]

    src_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    if len(sys.argv) > 2:
        user = sys.argv[2]
        pwd = sys.argv[3]
        host = sys.argv[4]
        dest = sys.argv[5]
    for i in os.listdir(src_path):
        upload(os.path.join(src_path, i))
    GenericWatcher(src_path).run()

def watch(local_path, file_names, user1, pwd1, host1, dest1):
    global files_to_monitor
    files_to_monitor = file_names
    src_path = local_path
    global user
    user = user1
    global pwd
    pwd = pwd1
    global host
    host = host1
    global dest
    dest = dest1
    for i in os.listdir(src_path):
        upload(os.path.join(src_path, i))
    GenericWatcher(src_path).run()