# ======================================
# Welcome Branch
# ======================================

# ------------------------------
# Libraries Imported Here
# ------------------------------
# sys is used for writing to stdout without a newline
# time is used to add delays for the boot animation
import sys
import time

# ------------------------------
# ANSI Color & Style Codes
# ------------------------------
# RESET clears all colors/styles
# BOLD makes text bold
RESET   = "\033[0m"
BOLD    = "\033[1m"

# Foreground color codes
RED     = "\033[91m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
CYAN    = "\033[96m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
WHITE   = "\033[97m"

# ------------------------------
# Color Rotation List
# ------------------------------
# This list can be used to cycle colors if needed
COLORS = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, WHITE]

# ------------------------------
# Startup / Welcome Messages
# ------------------------------
# Displays the developer and application name with color styling
print(f"\n{GREEN}{BOLD}Welcome Branch - Developer: Cyle Krohling{RESET}\n")
print(f"{BLUE}Welcome to InfoTechCenter V.1.0{RESET}\n")

# ------------------------------
# Boot Animation Variables
# ------------------------------
# x controls how many times the loop runs
# ellipsis controls how many dots appear in the animation
x = 0
ellipsis = 0

# ------------------------------
# Boot Animation Loop
# ------------------------------
# Loop runs until x reaches 16 (simulated boot duration)
while x != 16:
    # Increment loop counter
    x += 1

    # Build the boot message with animated dots
    ellipsisMessage = (
        f"{BLUE}InfoTechCenter OS is Booting{MAGENTA}" + "." * ellipsis + f"{RESET}"
    )

    # Increase number of dots each cycle
    ellipsis += 1

    # Write the message on the same terminal line
    # \r returns cursor to start, \033[K clears the line
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    # Pause to control animation speed
    time.sleep(0.75)

    # Reset dots after reaching 3 (0–3 loop)
    if ellipsis == 4:
        ellipsis = 0

    # ------------------------------
    # Boot Completion Message
    # ------------------------------
    # When loop finishes, display successful boot message
    if x == 16:
        print(
            f"\n\n{GREEN}{BOLD}"
            "Operating System Booted up - ID Scanned & Verified - Access Granted"
            f"{RESET}\n"
        )
