#Main branch

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
# End of Welcome Branch

#Weather branch

import random
from datetime import datetime, timedelta


def random_weather():
    """
    Randomly selects and returns a weather condition.
    This simulates getting today's weather.
    """

    # List of possible weather conditions
    weather_conditions = [
        "Sunny ☀️",
        "Cloudy ☁️",
        "Rainy 🌧️",
        "Stormy ⛈️",
        "Snowy ❄️",
        "Windy 🌬️",
        "Foggy 🌫️"
    ]

    # Pick and return one weather condition at random
    return random.choice(weather_conditions)


def update_alarm_based_on_weather(weather, base_alarm_time="07:00"):
    """
    Simulates updating a phone alarm to wake up earlier
    depending on weather conditions.
    """

    # Convert the base alarm time (string) into a datetime object
    alarm_time = datetime.strptime(base_alarm_time, "%H:%M")

    print("⏰ Alarm system: Checking weather impact on commute...")

    # Decide how much earlier to wake up based on weather
    if "Sunny" in weather or "Cloudy" in weather:
        extra_minutes = 0
    elif "Rainy" in weather or "Windy" in weather:
        extra_minutes = 15
    elif "Foggy" in weather:
        extra_minutes = 20
    elif "Snowy" in weather:
        extra_minutes = 30
    elif "Stormy" in weather:
        extra_minutes = 45
    else:
        extra_minutes = 0

    # Subtract extra minutes from the alarm time
    new_alarm_time = alarm_time - timedelta(minutes=extra_minutes)

    # Display the alarm update results
    print("\n⏰ Alarm update:\n")
    print(f"   ➤ Original alarm: {base_alarm_time}\n")
    print(f"   ➤ Weather buffer: {extra_minutes} minutes\n")

    if extra_minutes > 0:
        print(f"   ➤ New alarm set to: {new_alarm_time.strftime('%H:%M')} ⏱️\n")
    else:
        print("   ➤ No change needed. Alarm stays the same 👍\n")

    print("✅ Alarm adjustment complete.\n")

    # Return the new alarm time as a string
    return new_alarm_time.strftime("%H:%M")


class Car:
    """
    Represents a car and its driving settings.
    """

    def __init__(self):
        # Default car settings
        self.max_speed = 120        # Maximum speed in mph
        self.driving_mode = "Normal"  # Default driving mode

    def adjust_for_weather(self, weather):
        """
        Adjusts the car's driving mode and max speed
        based on the detected weather.
        """

        print("📡 Car system: Checking weather conditions...")
        print(f"\n📡 Car system: Weather detected -> {weather}")

        # Change settings based on weather type
        if "Sunny" in weather:
            self.max_speed = 120
            self.driving_mode = "Sport"
        elif "Cloudy" in weather:
            self.max_speed = 110
            self.driving_mode = "Normal"
        elif "Rainy" in weather:
            self.max_speed = 90
            self.driving_mode = "Rain"
        elif "Stormy" in weather:
            self.max_speed = 70
            self.driving_mode = "Safety"
        elif "Snowy" in weather:
            self.max_speed = 60
            self.driving_mode = "Snow"
        elif "Windy" in weather:
            self.max_speed = 85
            self.driving_mode = "Stability"
        elif "Foggy" in weather:
            self.max_speed = 75
            self.driving_mode = "Fog"

        # Display the updated car settings
        print("\n🚗 Car response:\n")
        print(f"   ➤ Driving mode set to: {self.driving_mode}\n")
        print(f"   ➤ Max speed limited to: {self.max_speed} mph\n")
        print("✅ Adjustments complete.\n")


# ---------------- Main Program ----------------

# Generate today's (random) weather
weather_today = random_weather()

# Display today's weather
print("\n🌍 Today's weather:", weather_today, "\n")

# Update the alarm time based on today's weather
update_alarm_based_on_weather(weather_today, base_alarm_time="07:00")

# Create a Car object
my_car = Car()

# Adjust the car's behavior based on today's weather
my_car.adjust_for_weather(weather_today)
#end Weather branch
