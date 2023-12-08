import requests

class WeatherForecastApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"

    def get_current_weather(self, city):
        endpoint = "weather"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        data = response.json()

        if response.status_code == 200:
            self.display_current_weather(data)
        else:
            print("Error fetching current weather. Please try again.")

    def get_5_day_forecast(self, city):
        endpoint = "forecast"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        data = response.json()

        if response.status_code == 200:
            self.display_5_day_forecast(data)
        else:
            print("Error fetching 5-day forecast. Please try again.")

    @staticmethod
    def display_current_weather(data):
        print(f"Current Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} km/h")

    @staticmethod
    def display_5_day_forecast(data):
        print(f"5-Day Forecast for {data['city']['name']}:")
        for forecast in data['list']:
            date = forecast['dt_txt']
            temperature = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"Day {date}: {temperature}°C, {description}")

if __name__ == "__main__":
    print("Welcome to the Weather Forecast Application!")
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    app = WeatherForecastApp(api_key)

    while True:
        print("\n1. Get current weather conditions")
        print("2. Get 5-day forecast")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            city = input("Enter the city or location: ")
            app.get_current_weather(city)
        elif choice == "2":
            city = input("Enter the city or location: ")
            app.get_5_day_forecast(city)
        elif choice == "3":
            print("Thank you for using the Weather Forecast Application!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
