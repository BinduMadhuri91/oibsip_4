import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather():
    location = location_entry.get()
    if not location:
        messagebox.showerror("Error", "Please enter a location.")
        return

    api_key = "d40ae4aed632137e09c38c8264714ccd"  
    data = get_weather(api_key, location)
    
    if data:
        city_name = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        weather_info = (
            f"City: {city_name}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Conditions: {description.capitalize()}\n"
            f"Wind Speed: {wind_speed} m/s\n"
        )
        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "Unable to fetch weather data. Please check the location and try again.")

root = tk.Tk()
root.title("Advanced Weather App")

tk.Label(root, text="Enter City Name or ZIP Code:").pack(pady=10)

location_entry = tk.Entry(root)
location_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=display_weather).pack(pady=20)

weather_label = tk.Label(root, text="", justify="left")
weather_label.pack(pady=10)

root.mainloop()
