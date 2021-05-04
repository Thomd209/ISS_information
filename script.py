from tkinter import *
import requests
import webbrowser

root = Tk()
root.title('ISS information')

title = Label(text='ISS information', font=('Arial', 24))
title.place(relx=0.40, rely=0.025)

quantity_people_question = Label(text='How many people are in space right now?', font=('Arial', 12))
quantity_people_question.place(relx=0.025, rely=0.125)

astros_request = requests.get('http://api.open-notify.org/astros.json')
astros_dict = astros_request.json()
astros_list = astros_dict['people']
quantity_people = len(astros_list)

quantity_people_answer = Label(text=f'Quantity of people are in space right now: {quantity_people}', font=('Arial', 12))
quantity_people_answer.place(relx=0.025, rely=0.175)

people_list_lib = Label(text='List of people and crafts are in space right now:', font=('Arial', 12))
people_list_lib.place(relx=0.025, rely=0.23)

people_list = Listbox(width=50, font=('Arial', 12))
people_list.place(relx=0.025, rely=0.27)

for elem in astros_list:
    name = elem['name']
    craft = elem['craft']
    people_list.insert(END, f'Name: {name}, craft: {craft}')

button_description = Label(text='Show the location of the ISS:', font=('Arial', 12))
button_description.place(relx=0.025, rely=0.59)

iss_location_request = requests.get('http://api.open-notify.org/iss-now.json')
iss_location_dict = iss_location_request.json()
latitude = iss_location_dict['iss_position']['latitude']
longitude = iss_location_dict['iss_position']['longitude']


def show_location():
    webbrowser.open(f'https://earth.google.com/web/search/{latitude}, {longitude}')


btn_show = Button(text='Show', bg='blue', fg='white', font=('Arial', 12), command=show_location)
btn_show.place(relx=0.025, rely=0.64)

root.mainloop()
