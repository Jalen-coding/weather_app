# Building a Interactivae Flet App with Python
# API's and Street Map

import flet as ft
import requests
from api_key import API_KEY

# Build out the API and get a response
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Open Weather API
def get_weather(city):
    params = {"q":city,"appid":API_KEY,"units":"imperial"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "city":data["name"],
            "temp":data["main"]["temp"],
            "humidity":data["main"]["humidity"],
            "weather":data["weather"][0]["description"],
            "lat":data["coord"]["lat"],
            "lon":data["coord"]["lon"]
        }
    return None

def main(page: ft.Page):
    page.title = "Flet Weather App"
    page.bgcolor = ft.Colors.GREEN_400
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 700

    city_input = ft.TextField(
        label="Enter City",
        width=300,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        border_radius=10
    )

    result_text = ft.Text("",size=18,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)

    # Call and get weather data
    def search_weather(e):
        city = city_input.value.strip()
        if not city:
            result_text.value = "Please enter a city name..."
            page.update()
            return

        weather_data = get_weather(city)

        if weather_data:
            result_text.value=f"City: {weather_data["city"]}\nTemperature: {weather_data["temp"]}C\n Humididty: {weather_data["humidity"]}%\nWeather: {weather_data["weather"]}"

        else:
            result_text.value="City not found. Try again..."

        page.update()

    # Search Button
    search_button = ft.ElevatedButton(
        "Search",
        on_click=search_weather,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=10)
    )

    # Container for UI
    container = ft.Container(
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Flet Weather App",size=30,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),
                city_input,
                search_button,
                result_text,
            ],
        ),
        alignment=ft.alignment.center,
        padding=20,
        border_radius=15,
        bgcolor=ft.Colors.BLUE_GREY_800,
        shadow=ft.BoxShadow(blur_radius=15,spread_radius=2,color=ft.Colors.BLACK12)
    )

    page.add(container)

if __name__ == "__main__":
    ft.app(target=main)