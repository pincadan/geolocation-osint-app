import geopy
from geopy.geocoders import Nominatim
import requests
import folium

def geolocate_address(address):
    geolocator = Nominatim(user_agent="GeoLocateMe")
    location = geolocator.geocode(address)
    return location.address, location.latitude, location.longitude

def reverse_geocode(latitude, longitude):
    geolocator = Nominatim(user_agent="GeoLocateMe")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    return location.address

def get_weather_data(latitude, longitude):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return None

def display_map(latitude, longitude, address):
    map = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup=address).add_to(map)
    return map

def main():
    print("Welcome to GeoLocateMe!")
    print("Please choose an option:")
    print("1. Geolocate an address")
    print("2. Reverse geocode coordinates")
    print("3. Get weather data")
    print("4. Display map")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        address = input("Enter an address to geolocate: ")
        location, latitude, longitude = geolocate_address(address)
        print(f"Address: {location}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    elif choice == "2":
        latitude = input("Enter the latitude: ")
        longitude = input("Enter the longitude: ")
        address = reverse_geocode(latitude, longitude)
        print(f"Address: {address}")
    elif choice == "3":
        latitude = input("Enter the latitude: ")
        longitude = input("Enter the longitude: ")
        weather_data = get_weather_data(latitude, longitude)
        if weather_data:
            print(f"Weather: {weather_data['weather'][0]['description']}")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Humidity: {weather_data['main']['humidity']}%")
        else:
            print("Failed to retrieve weather data.")
    elif choice == "4":
        latitude = input("Enter the latitude: ")
        longitude = input("Enter the longitude: ")
        address = reverse_geocode(latitude, longitude)
        map = display_map(latitude, longitude, address)
        map.save("map.html")
        print("Map saved as 'map.html'")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()