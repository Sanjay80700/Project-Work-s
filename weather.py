from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root=Tk()
root.title("Weather Forcasting App")
root.geometry("750x470+200+60")
root.configure(bg="#57adff")
root.resizable(False,False)

##LOCATION
def getweather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)


    ##WEATHER API
    api="https://api.openweathermap.org/data/2.8/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&&units=metric&exclude=hourly&appid=74b829191caf38a0c0c68a24ec2b50b7" 
    json_data = requests.get(api).json()

    ##CURRENT WEATHER
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    
    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hpa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(description))


    #FIRST cell
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']

    photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")
    day1temp.place(x=10,y=70)



    
    #SECOND cell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']

    img=(Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image=img.resize((30,30))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']

    day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")
    day2temp.place(x=10,y=80)

    
    #THIRD cell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    img=(Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image=img.resize((30,30))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']

    day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")
    day3temp.place(x=10,y=80)

    
    #FOURTH cell
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']

    img=(Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image=img.resize((30,30))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']

    day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")
    day4temp.place(x=10,y=80)
    
    #FIFTH cell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']

    img=(Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image=img.resize((30,30))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']

    day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")
    day5temp.place(x=10,y=80)

    
    #SIXTH cell
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']

    img=(Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image=img.resize((30,30))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']

    day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")
    day6temp.place(x=10,y=80)

    
    #SEVENTH cell
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    img=(Image.open(f"icon/{seventhdayimage}@2x.png"))
    resized_image=img.resize((30,30))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']

    day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")
    day7temp.place(x=10,y=80)



    #DAY'S

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=3)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=4)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=5)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=6)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=2)
    day7.config(text=seventh.strftime("%A"))





##ICON
image_icon=PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="images/rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x="60",y="120")


##LABEL
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=70,y=130)

label1=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=70,y=150)

label1=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=70,y=170)

label1=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=70,y=190)

label1=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=70,y=210)


##SEARCH BOX
Search_image=PhotoImage(file="images/rectangle 4.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=300,y=150)


##IMAGE
weat_image=PhotoImage(file="images/cloud (2).png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=315,y=160)

textfield=tk.Entry(root,justify='center',width=15,font=('Impact',25,'bold'),bg="#203243",border=0,fg='white')
textfield.place(x=370,y=160)
textfield.focus()

search_icon=PhotoImage(file="images/search_4366917.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor='hand2',bg='#203243',command=getweather)
myimage_icon.place(x=665,y=163)

##BUTTON BOX
frame=Frame(root,width=750,height=150,bg='#212120')
frame.pack(side=BOTTOM)

##BOTTOM BOX
firstbox=PhotoImage(file="images/rectangle 2.png")
secondbox=PhotoImage(file="images/rectangle 3.png")

Label(frame,image=firstbox,bg="#212120").place(x=10,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=170,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=260,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=350,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=440,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=530,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=620,y=20)



##CLOCK
clock=Label(root,font=('Bahnschrift',50,'bold'),fg='white',bg='#57adff')
clock.place(x=40,y=10)



##TIMEZONE
timezone=Label(root,font=('Bahnschrift',20,'bold'),fg='white',bg='#57adff')
timezone.place(x=510,y=12)

long_lat=Label(root,font=('Bahnschrift',10,'bold'),fg='white',bg='#57adff')
long_lat.place(x=510,y=42)




##Temperature,Humidity,Pressure,Wind,Decription
t=Label(root,font=("helvetica",11),fg="white",bg="#203243")
t.place(x=180,y=130)
h=Label(root,font=("helvetica",11),fg="white",bg="#203243")
h.place(x=180,y=150)
p=Label(root,font=("helvetica",11),fg="white",bg="#203243")
p.place(x=180,y=170)
w=Label(root,font=("helvetica",11),fg="white",bg="#203243")
w.place(x=180,y=190)
d=Label(root,font=("helvetica",11),fg="white",bg="#203243")
d.place(x=180,y=210)


#FIRST cell
firstframe=Frame(root,width=140,height=120,bg="#282829")
firstframe.place(x=14,y=340)

day1=Label(firstframe,font="arial 18",bg="#282829",fg="#fff")
day1.place(x=25,y=2)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=40,y=26)

day1temp=Label(firstframe,bg="#282829",fg="#fff",font="arial 15 bold")
day1temp.place(x=100,y=50)

#SECOND cell 
secondframe=Frame(root,width=84,height=120,bg="#282829")
secondframe.place(x=172,y=342)

day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=20,y=10)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=30,y=39)

day2temp=Label(secondframe,bg="#282829",fg="#fff")
day2temp.place(x=2,y=70)

#THIRD cell
thirdframe=Frame(root,width=84,height=120,bg="#282829")
thirdframe.place(x=352,y=342)

day3=Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=10)

thirdimage=Label(thirdframe,bg="#282829")
thirdimage.place(x=30,y=39)

day3temp=Label(thirdframe,bg="#282829",fg="#fff")
day3temp.place(x=2,y=70)

#FOURTH cell
fourthframe=Frame(root,width=84,height=120,bg="#282829")
fourthframe.place(x=442,y=342)

day4=Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=20,y=10)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=30,y=39)

day4temp=Label(fourthframe,bg="#282829",fg="#fff")
day4temp.place(x=2,y=70)

#FIFTH cell
fifthframe=Frame(root,width=84,height=120,bg="#282829")
fifthframe.place(x=532,y=342)

day5=Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=20,y=10)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=30,y=39)

day5temp=Label(fifthframe,bg="#282829",fg="#fff")
day5temp.place(x=2,y=70)


#SIXTH cell
sixthframe=Frame(root,width=84,height=120,bg="#282829")
sixthframe.place(x=622,y=342)

day6=Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=20,y=10)

sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=30,y=39)

day6temp=Label(sixthframe,bg="#282829",fg="#fff")
day6temp.place(x=2,y=70)

#SEVENTH cell
seventhframe=Frame(root,width=84,height=120,bg="#282829")
seventhframe.place(x=262,y=342)

day7=Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=20,y=10)

seventhimage=Label(seventhframe,bg="#282829")
seventhimage.place(x=30,y=39)

day7temp=Label(seventhframe,bg="#282829",fg="#fff")
day7temp.place(x=2,y=70)



root.mainloop()
   
