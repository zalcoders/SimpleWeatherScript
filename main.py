from data import WEATHER_DATA

def get_weather(city, show_recomendations):
    """Retrieve weather data for a given city."""
    data = WEATHER_DATA.get(city.title(), "No data available for this city.")
    if show_recomendations:
        recomendation = get_recommendation(data["condition"])
    else:
        recomendation = None
    return data["temperature"], data["condition"], recomendation

def get_recommendation(condition):
    if condition == "Rainy":
        return "Don't forget your umbrella!"
    elif condition == "Sunny":
        return "Wear some sunscreen!"
    else:
        return "Have a great day!"

def present_info(name, temp, condition, final_recomendation):
    print(f"In {name}, current tempretur is: {temp} and the condition is: {condition}")
    if final_recomendation is not None:
        print(f"And our recomendation is: {final_recomendation}")

def main():
    city = input("Enter the name of the city to get its current weather: ")
    wants_recomendations = input("Do you want to see our recomendation for today?(y/n): ")
    if wants_recomendations == "y":
        show_recomendations = True
    else:
        show_recomendations = False
    temp, condition, final_recomendation = get_weather(city, show_recomendations)
    present_info(city, temp, condition, final_recomendation)
    

if __name__ == "__main__":
    main()

