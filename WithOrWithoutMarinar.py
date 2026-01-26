#Weather branch

import random  # Import the random module to generate random choices


def random_weather():
    """
    This function randomly selects and returns a weather condition.
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

    # Randomly choose and return one weather condition from the list
    return random.choice(weather_conditions)


class Car:
    """
    This class represents a car and its driving settings.
    """

    def __init__(self):
        # Set default car settings when a Car object is created
        self.max_speed = 120        # Maximum speed in mph
        self.driving_mode = "Normal"  # Default driving mode

    def adjust_for_weather(self, weather):
        """
        Adjusts the car's driving mode and max speed based on the weather.
        """

        # Simulate the car checking weather conditions
        print("📡 Car system: Checking weather conditions...")
        print(f"\n📡 Car system: Weather detected -> {weather}")

        # Change car behavior depending on the detected weather
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

# Generate today's random weather
weather_today = random_weather()

# Display today's weather
print("\n🌍 Today's weather:", weather_today, "\n")

# Create a Car object
my_car = Car()

# Adjust the car's settings based on today's weather
my_car.adjust_for_weather(weather_today)
