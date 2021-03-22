import time
import os
import watchdog.events
import watchdog.observers

'''class OnMyWatch:
    # Set the directory on watch
    watchDirectory = os.path.abspath("watch2.py")
    watchDirectory = watchDirectory.replace("\watch2.py", "")

    def __init__(self):
        self.observer = watchdog.observers.Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()'''


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.txt'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.watchDirectory)
        f = open("temp.txt", "r")
        announcement = f.read()
        f.close()
        os.remove("temp.txt")
        return announcement

def watchstart():
    if __name__ == "__main__":
        src_path = os.path.abspath("watch2.py")
        src_path = src_path.replace("\watch.py", "")
        event_handler = Handler()
        observer = watchdog.observers.Observer()
        observer.schedule(event_handler, path=src_path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()