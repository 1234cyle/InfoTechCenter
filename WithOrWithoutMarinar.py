#Weather branch

import random  # Import the random module to generate random choices

def random_weather():
    """
    This function returns a random weather condition as a string.
    """

    # Create a list of possible weather conditions
    weather_conditions = [
        "Sunny ☀️",
        "Cloudy ☁️",
        "Rainy 🌧️",
        "Stormy ⛈️",
        "Snowy ❄️",
        "Windy 🌬️",
        "Foggy 🌫️"
    ]

    # Randomly select and return one weather condition from the list
    return random.choice(weather_conditions)

# Call the function and print the result
print("\nToday's weather:", random_weather(),"\n")
