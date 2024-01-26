from data import WEATHER_DATA

def get_weather(city):
    """Retrieve weather data for a given city."""
    return WEATHER_DATA.get(city.title(), "No data available for this city.")

def get_recommendation(condition):
    if condition == "Rainy":
        return "Don't forget your umbrella!"
    elif condition == "Sunny":
        return "Wear some sunscreen!"
    else:
        return "Have a great day!"

def main():
    city = input("Enter the name of the city to get its current weather: ")
    weather = get_weather(city)
    print(f"Weather in {city.title()}: {weather}")

if __name__ == "__main__":
    main()
