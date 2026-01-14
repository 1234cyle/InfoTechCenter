#Welcome branch

#Libraries Imported Here
import sys
import time

print("\nWelcome Branch - Developer: Cyle Krohling\n")
print("Welcome to InfoTechCenter V.1.0\n")

x = 0
ellipsis = 0

while x != 16:
    x += 1
    ellipsisMessage = ("InfoTechCenter OS is Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r\033[KK" + ellipsisMessage)
    sys.stdout.flush()
    time.sleep(0.75)
    if ellipsis == 4:
        ellipsis = 0
    if x == 16:
        print("\n\nOperating System Booted up - ID Scanned & Verified - Access Granted\n")