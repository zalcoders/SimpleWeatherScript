from data import WEATHER_DATA

def get_weather(city):
    """Retrieve weather data for a given city."""
    data = WEATHER_DATA.get(city.title(), "No data available for this city.")
    return data["temperature"], data["condition"]

def get_recommendation(condition):
    if condition == "Rainy":
        return "Don't forget your umbrella!"
    elif condition == "Sunny":
        return "Wear some sunscreen!"
    else:
        return "Have a great day!"

def present_info(name, temp, condition):
    print(f"In {name}, current tempretur is: {temp} and the condition is: {condition}")

def main():
    city = input("Enter the name of the city to get its current weather: ")
    temp, condition = get_weather(city)
    present_info(city, temp, condition)

if __name__ == "__main__":
    main()
