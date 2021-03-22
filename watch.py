import time
import os
import discordapp
def watchandwrite():
    while True:
        try:
            f = open("temp.txt", "x")
        except:
            time.sleep(30)
            continue
        finally:
            announcement = f.read()
            f.close()
            os.remove("temp.txt")
            discordapp.announcement(announcement)
        break
watchandwrite()