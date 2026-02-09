#betatestDev

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

#Gasoline branch

class SmartCar:
    def __init__(self, tank_capacity=50.0, low_fuel_threshold=25):
        """
        Initialize the SmartCar object.
        
        Parameters:
        - tank_capacity (float): Maximum capacity of the fuel tank.
        - low_fuel_threshold (float): Percentage threshold below which the car needs gas soon.
        
        Attributes:
        - gas_level (float): Current amount of fuel in the tank.
        - gas_stations (list of dicts): Simulated nearby gas stations with info.
        - alarm_time (datetime or None): Time to wake up in the morning to get gas if needed.
        """
        self.tank_capacity = tank_capacity
        self.low_fuel_threshold = low_fuel_threshold  # percentage threshold
        self.gas_level = self._get_random_gas_level()  # Initialize gas level randomly
        self.gas_stations = self._load_gas_stations()  # Load nearby gas stations
        self.alarm_time = None  # ⏰ Alarm time placeholder

    def _get_random_gas_level(self):
        """
        Simulates reading the fuel level from a sensor using randomness.
        Returns a float between 0 and tank_capacity, rounded to 2 decimals.
        """
        return round(random.uniform(0, self.tank_capacity), 2)

    def _load_gas_stations(self):
        """
        Simulates nearby gas stations.
        Each station is represented as a dictionary containing:
        - name: Station name
        - distance: Distance from car (in miles)
        - price: Fuel price per gallon
        - snacks: Boolean indicating if snacks are available
        - slurpees: Boolean indicating if slurpees are available
        - open: Boolean indicating if station is currently open
        """
        return [
            {
                "name": "Shell",
                "distance": round(random.uniform(0.5, 10), 2),
                "price": round(random.uniform(3.20, 4.20), 2),
                "snacks": True,
                "slurpees": False,
                "open": random.choice([True, False])
            },
            {
                "name": "Quicktrip",
                "distance": round(random.uniform(0.5, 10), 2),
                "price": round(random.uniform(3.10, 4.10), 2),
                "snacks": True,
                "slurpees": True,
                "open": random.choice([True, False])
            },
            {
                "name": "Buckees",
                "distance": round(random.uniform(0.5, 10), 2),
                "price": round(random.uniform(3.00, 4.00), 2),
                "snacks": True,
                "slurpees": False,
                "open": random.choice([True, False])
            },
            {
                "name": "Speedway",
                "distance": round(random.uniform(0.5, 10), 2),
                "price": round(random.uniform(3.15, 4.15), 2),
                "snacks": True,
                "slurpees": True,
                "open": random.choice([True, False])
            },
            {
                "name": "Costco Gas",
                "distance": round(random.uniform(1, 15), 2),
                "price": round(random.uniform(2.95, 3.75), 2),
                "snacks": False,
                "slurpees": False,
                "open": random.choice([True, False])
            },
        ]

    def gas_percentage(self):
        """
        Returns the current fuel level as a percentage of the tank capacity.
        """
        return (self.gas_level / self.tank_capacity) * 100

    def needs_gas_soon(self):
        """
        Determines if the car needs fuel soon based on the low_fuel_threshold.
        Returns True if fuel is below threshold, else False.
        """
        return self.gas_percentage() <= self.low_fuel_threshold

    def set_morning_alarm(self):
        """
        Sets a wake-up alarm for 7:00 AM if fuel is low.
        - If gas is low and no alarm exists, set alarm for tomorrow morning at 7:00 AM.
        - If gas is sufficient and an alarm was previously set, cancel it.
        """
        if self.needs_gas_soon() and self.alarm_time is None:
            # Create a datetime object for 7:00 AM today
            tomorrow_morning = datetime.now().replace(
                hour=7, minute=0, second=0, microsecond=0
            )
            # If 7:00 AM today has already passed, set for tomorrow
            if tomorrow_morning <= datetime.now():
                tomorrow_morning += timedelta(days=1)

            self.alarm_time = tomorrow_morning
            print(f"⏰ Wake-up alarm set for {self.alarm_time.strftime('%I:%M %p')} to get gas.")

        elif not self.needs_gas_soon() and self.alarm_time is not None:
            # Cancel alarm if fuel is sufficient
            print("⏰ Wake-up alarm canceled (gas level is okay).")
            self.alarm_time = None

    def choose_best_gas_station(self):
        """
        Chooses the best gas station based on the following priority:
        1. Station must be open
        2. Cheapest fuel price
        3. Availability of snacks
        4. Availability of slurpees
        5. Closest distance

        Returns the best station dictionary or None if no stations are open.
        """
        open_stations = [s for s in self.gas_stations if s["open"]]
        if not open_stations:
            return None

        # Sort stations by priority rules
        return sorted(
            open_stations,
            key=lambda s: (
                s["price"],
                not s["snacks"],    # prioritize stations with snacks
                not s["slurpees"],  # prioritize stations with slurpees
                s["distance"]
            )
        )[0]

    def display_status(self):
        """
        Displays the current fuel status and evaluates nearby gas stations.
        Also sets or cancels a morning alarm if needed.
        """
        # Print fuel level
        print(f"\n⛽ Gas Level: {self.gas_level} / {self.tank_capacity} "
              f"({self.gas_percentage():.1f}%)")

        # Update morning alarm based on fuel level
        self.set_morning_alarm()

        # If fuel is low, find the best gas station
        if self.needs_gas_soon():
            print("\n⚠️ Low fuel detected! Evaluating gas stations...\n")
            station = self.choose_best_gas_station()

            if station is None:
                print("🚫 No open gas stations nearby! Drive carefully...\n")
                return

            # Print recommended station details
            print("🏆 Best Gas Station Choice:")
            print(f"• Name: {station['name']}")
            print(f"• Price: ${station['price']} per gallon")
            print(f"• Distance: {station['distance']} miles")
            print(f"• Open: {'Yes' if station['open'] else 'No'}")
            print(f"• Snacks: {'Yes' if station['snacks'] else 'No'}")
            print(f"• Slurpees: {'Yes' if station['slurpees'] else 'No'}\n")
        else:
            print("\n✅ Fuel level is sufficient. No need to refuel yet.\n")

# Example usage
car = SmartCar()
car.display_status()
#Gasoline branch End
