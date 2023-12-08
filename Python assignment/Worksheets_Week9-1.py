import requests # Import requests moduel 
#define the Weather API class
class WeatherAPI:
    #Initialize of the code
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"
    # Method to make API requests and retrieve weather data
    def get_weather(self, endpoint, params):
        params['appid'] = self.api_key
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        #the error circumstance actions
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
#define WeatherForecastApp class
class WeatherForecastApp:
    #Initialize of the code
    def __init__(self, api_key):
        self.api = WeatherAPI(api_key)
    # Method to get current weather conditions for a specific city
    def get_current_weather(self, city):
        endpoint = "weather"
        params = {'q': city, 'units': 'metric'}
        return self.api.get_weather(endpoint, params)
    # Method to get 5-day forecast for a specific city
    def get_5_day_forecast(self, city):
        endpoint = "forecast"
        params = {'q': city, 'units': 'metric'}
        return self.api.get_weather(endpoint, params)
    # Method to display current weather information
    """
    display format of weather
    print temperature, description, humidity and wind speed
    """
    def display_weather(self, data):
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} km/h")
    # Method to display the 5-day forecast
    """
    display format of 5 day forecast
    first print city 
    define data, temperature, description
    and print the result iterate while day in the data 
    """
    def display_5_day_forecast(self, data):
        print(f"5-Day Forecast for {data['city']['name']}:")
        for day in data['list']:
            date = day['dt_txt']
            temperature = day['main']['temp']
            description = day['weather'][0]['description']
            print(f"{date}: {temperature}°C, {description}")

    def run(self):
        # Main execution method
        #print welcome message
        print("Welcome to the Weather Forecast Application!")
        #Iterate while the circumstance is valid
        while True:
            #print option menu
            print("1. Get current weather conditions")
            print("2. Get 5-day forecast")
            print("3. Exit")
            #input the selection
            choice = input("Enter your choice (1/2/3): ")
            """
            if the input value is equal to 1
            receive the input value of city or location
            define the weather_data equal to current weather of input value of city or location
            and if data is true display the result
            if the input value is equal to 2
            receive the input value of city or location
            define the forecase_data equal to get 5 day forecast of city
            and if data is true display 5 day forecast results
            despite that the input value is 3 print the end message and break the loop
            hence the program is finished
            however the input value is invalid value 
            print the error message
            """
            if choice == '1':
                city = input("Enter the city or location: ")
                weather_data = self.get_current_weather(city)
                if weather_data:
                    print(f"Current Weather in {city}:")
                    self.display_weather(weather_data)
            elif choice == '2':
                city = input("Enter the city or location: ")
                forecast_data = self.get_5_day_forecast(city)
                if forecast_data:
                    self.display_5_day_forecast(forecast_data)
            elif choice == '3':
                print("Thank you for using the Weather Forecast Application!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
#the below is able to process the code
if __name__ == "__main__":
    #own api_key
    api_key = "e0428aa7be8a24c3c3e862dbe611e901"
    weather_app = WeatherForecastApp(api_key)
    weather_app.run()
