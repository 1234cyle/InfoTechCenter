#Gasoline branch

import random
from datetime import datetime, timedelta

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
