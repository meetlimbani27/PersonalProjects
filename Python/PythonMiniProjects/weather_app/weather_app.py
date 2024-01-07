# Import necessary modules
from tkinter import *            # https://docs.python.org/3/library/tkinter.html
from tkinter import ttk
import requests                  # https://docs.python-requests.org/en/latest/
import geocoder                  # https://geocoder.readthedocs.io


# Function to retrieve weather data
def data_get():
    # Check if the city name is empty
    if city_name.get() == "":
        # Use geolocation to get the latitude and longitude coordinates
        g = geocoder.ip('me')
        lat, lon = g.latlng

        # Make a request to the weather API using the latitude and longitude coordinates
        data = requests.get(f"http://api.weatherapi.com/v1/current.json?key=2a038d4a99d342f3a80171340231906&q={lat},{lon}").json()
    else:
        # Get the city name from the entry field
        city = city_name.get() 

        # Make a request to the weather API and retrieve the data
        data = requests.get(f"http://api.weatherapi.com/v1/current.json?key=2a038d4a99d342f3a80171340231906&q={city}").json()

    # Update the labels with the weather information
    w_label1.config(text=data["current"]["condition"]["text"])
    temp_label1.config(text=data["current"]["temp_c"])
    per_label1.config(text=data["current"]["pressure_mb"])
    wi_label1.config(text=data["current"]["wind_kph"])
    hum_label1.config(text=data["current"]["humidity"])
    cc_label1.config(text=data["current"]["cloud"])



# Create the main window
win = Tk()
win.title("Windoser")
win.config(bg="teal")
win.geometry("500x575")

# Create and place the app title label
name_label = Label(win, text="Windoser Weather App", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

# Create a variable to store the selected city name
city_name = StringVar()

# List of city names for the combobox
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Create and place the combobox widget
com = ttk.Combobox(win, text="Windoser Weather App", values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# Create and place the submit button
submit_button = Button(win, text="Submit", font=("Time New Roman", 19, "bold"), command=data_get)
submit_button.place(y=190, height=50, width=100, x=200)

# Create and place the weather labels
w_label = Label(win, text="Weather Climate", font=("Time New Roman", 15))
w_label.place(x=25, y=260, height=37, width=210)
w_label1 = Label(win, text="", font=("Time New Roman", 15))
w_label1.place(x=250, y=260, height=37, width=210)

# Create and place the wind speed labels
wi_label = Label(win, text="Wind (kph)", font=("Time New Roman", 15))
wi_label.place(x=25, y=312, height=37, width=210)
wi_label1 = Label(win, text="", font=("Time New Roman", 15))
wi_label1.place(x=250, y=312, height=37, width=210)

# Create and place the temperature labels
temp_label = Label(win, text="Temperature(C)", font=("Time New Roman", 15))
temp_label.place(x=25, y=364, height=37, width=210)
temp_label1 = Label(win, text="", font=("Time New Roman", 15))
temp_label1.place(x=250, y=364, height=37, width=210)

# Create and place the pressure labels
per_label = Label(win, text="Pressure(mb)", font=("Time New Roman", 15))
per_label.place(x=25, y=416, height=37, width=210)
per_label1 = Label(win, text="", font=("Time New Roman", 15))
per_label1.place(x=250, y=416, height=37, width=210)

# Create and place the humidity labels
hum_label = Label(win, text="Humidity(%)", font=("Time New Roman", 15))
hum_label.place(x=25, y=468, height=37, width=210)
hum_label1 = Label(win, text="", font=("Time New Roman", 15))
hum_label1.place(x=250, y=468, height=37, width=210)

cc_label = Label(win, text="cloud cover(%)", font=("Time New Roman", 15))
cc_label.place(x=25, y=520, height=37, width=210)
cc_label1 = Label(win, text="", font=("Time New Roman", 15))
cc_label1.place(x=250, y=520, height=37, width=210)

# Start the main event loop
win.mainloop()

