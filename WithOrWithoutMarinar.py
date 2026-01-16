#Welcome branch

#Libraries Imported Here

import sys
import time

import sys
import time

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"

RED     = "\033[91m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
CYAN    = "\033[96m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
WHITE   = "\033[97m"

# Color rotation list
COLORS = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, WHITE]

print(f"\n{GREEN}{BOLD}Welcome Branch - Developer: Cyle Krohling{RESET}\n")
print(f"{BLUE}Welcome to InfoTechCenter V.1.0{RESET}\n")

x = 0
ellipsis = 0

while x != 16:
    x += 1
    ellipsisMessage = (
        f"{BLUE}InfoTechCenter OS is Booting{YELLOW}" + "." * ellipsis + f"{RESET}"
    )
    ellipsis += 1

    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()
    time.sleep(0.75)

    if ellipsis == 4:
        ellipsis = 0

    if x == 16:
        print(
            f"\n\n{GREEN}{BOLD}"
            "Operating System Booted up - ID Scanned & Verified - Access Granted"
            f"{RESET}\n"
        )
