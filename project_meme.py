# Importing module
import webbrowser
# import module_Mood
from module_Mood import check_mood
import mysql.connector

#import music module
import module_music as music
from music_3 import MusicPlayer

# Creating connection object

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Harshit",
    database ="healthsys"
)

# checking connection establishment 
if (mydb.is_connected):
    print("connection established")

# Printing the connection object    
print(mydb)

# Importing image module PIL i.e Python Image Library

import PIL

from PIL import Image


#Importing MODULE 1 CREATED BY TEAM PC
import module_img

from module_img import *

print("\n")

# MAIN PROGRAM


"""USER NAME """

USER=input("NAME >>> ")


__Name__=USER.title() #new code edited resently

import re
if(bool(re.match('^[a-zA-Z" "]*$',__Name__))==True):
    print("valid")
    
else:
    print("invalid")
    quit()


print("HI !! ",__Name__," HOW ARE YOU FEELING ....")

# Moods
which_mood = {
    'happy':0,
    'sad':1,
    'angry':2,
    'gaming':3,
    'neutral':4,
    'all':5,
    'foody':6
}
while True:
    try:
        mood = input(">>> ")
        mood=mood.lower()


        if not check_mood(mood,which_mood['all']):
            print('invalid')
        else :
            print("oh!",mood)
            break
    except ValueError:
        print("Provide an string value...")
        continue

    
    

#user data for database


"""if (age>100):
    print("buddy !! life span of homosepians is less than 101 years")"""

while True:
  try:
    age = int(input("Age: ")) 
    if age>1 and age<100:
      print("Age entered successfully...")
      break
    else:
      print("Age should be >1 and <100...")      
  except ValueError:
    print("Provide an integer value...")
    continue
    
while True:
    try:
        gender = str(input('Gender:')).lower()
        if gender in ['male', 'female']:
            break
        else:
            print("error")
    except ValueError:
        print("Provide an string value...")
        continue    
        


address=input("City:")

"""
Pushing  Data To Database
"""
mood=mood.lower()


#condition for health


if check_mood(mood,which_mood['sad']) or check_mood(mood,which_mood['angry']):

    health = "bad"
    

elif check_mood(mood,which_mood['happy']) or check_mood(mood,which_mood['gaming']) or check_mood(mood,which_mood['neutral']) or check_mood(mood,which_mood["foody"]):

    health = "good"
    

#creating cursor{establishes conn between sql and python IDLE} 


cursor=mydb.cursor()

cursor.execute ("INSERT INTO moodlog (Name,Age,Gender,City,Mood,Health) VALUES ('{}','{}','{}','{}','{}','{}');".format(__Name__,age,gender,address,mood,health))



mydb.commit()


print("Data Entered Successfully!")
#STARTING OF MOOD DEPENDENCIED 


# NO STRING ERROR


# CONDITIONS :

import module_music as music
from music_3 import MusicPlayer


if check_mood(mood,which_mood['sad']):

    print("SO, what can i do to make your day !!\n")

    print("I Can do some cool things ,,\n1_Play music \n2_Give you motivation \n3_Make you laugh\n")

    lang = int(input(">>>"))
    match lang :
        case 1:
            print(" So, you like to hear some music : ")
            __ans__=input("Y/N\n>>>")
            __ans__=__ans__.lower()

            if (__ans__=="y" or __ans__== "yes"):

                music_player = MusicPlayer()
                music_player.run()

            else:
                print("Would you like to see some memes ....?\n ")
                __ans__=input("Y/N\n>>>")
                __ans__=__ans__.lower()


                if (__ans__=="y" or __ans__=="yes"):
                    import webbrowser

                    def open_html_page(file_path):
                       webbrowser.open(file_path, new=2)

                    # Example usage
                    html_file_path = r"C:\Users\harsh\mini_project_2\Untitled-1.html"
                    open_html_page(html_file_path)

                else:
                    print("Boy you really need some motivation ? ")
                    __ans__=input("Y/N\n>>>")
                    __ans__=__ans__.lower()
                    if (__ans__=="y" or __ans__=="yes"):
                        import module_music as music
                        music.motivational()
                

        case 3:
            print("So ,you like to see some memes ....?\n ")
            __ans__=input("Y/N\n>>>")
            __ans__=__ans__.lower()

            
            if (__ans__=="y" or __ans__=="yes"):
                import webbrowser
                def open_html_page(file_path):
                       webbrowser.open(file_path, new=2)

                    # Example usage
                html_file_path = r"C:\Users\harsh\mini_project_2\Untitled-1.html"
                open_html_page(html_file_path)

            else:
                #(__ans__=="n" or __ans__=="no"):
                print("THERE IS NOTHING I CAN DO NOW .............!!!\n You really need to seek G.O.D's attention ")

        case 2:
            print("So, motivation !!\n Here we GO!! ")
            import module_music as music
            music.motivation()

        case _:
            #(__ans__=="n" or __ans__=="no"):
            print("THERE IS NOTHING I CAN DO NOW .............!!!")



elif check_mood(mood,which_mood['happy']):

    print("Hope you make someone SMILE !!\n")

    print("SO, HOW can i make your day more joyful , here are certain things i can do - i can play music  , make you laugh , or i can give you motivation \n")

    print("Would you like to hear some music ???\n ")

    __ans__=input("Y/N\n>>>")
    __ans__=__ans__.lower()
    
    if (__ans__=="y" or __ans__== "yes"):
        

        music_player = MusicPlayer()
        music_player.run()
        
    elif(__ans__=="n" or __ans__== "no"):
        
        print("Would you like to see some memes ....?\n ")
        __ans__=input("Y/N\n>>>")
        __ans__=__ans__.lower()
    
        if (__ans__=="y" or __ans__=="yes"):
            import webbrowser
            def open_html_page(file_path):
            
                webbrowser.open(file_path, new=2)

                    # Example usage
            html_file_path = r"C:\Users\harsh\mini_project_2\Untitled-1.html"
            open_html_page(html_file_path)

    
    print(" DO need some motivation ? ")
    __ans__=input("Y/N\n>>>")
    __ans__=__ans__.lower()
    
    if (__ans__=="y" or __ans__=="yes"):

        import module_music as music
        music.motivational()

    else:
        pass
    
    print("Your chooice is : \n1- Play GAME \n2-  GAMING MUSIC")
    
    ch=int(input(">>>"))

    #gaming web site
    
    def play_game():
        import webbrowser
        webbrowser.open('http://poki.com', new=2)
        
    #memes 
      
    def memes():
        import webbrowser
        def open_html_page(file_path):
            webbrowser.open(file_path, new=2)

                    # Example usage
        html_file_path = r"C:\Users\harsh\mini_project_2\Untitled-1.html"
        open_html_page(html_file_path)
        


    #gaming music

    def gaming_music():
        music.gaming()
   


    if(ch==1):
        play_game()


    elif(ch==2):
        import module_music as music
        gaming_music()
    else :
        
       print("ALPHA TO CHARLIE !!! ITS MAY_DAY BUT YOU ARE NOOB......")
        

    


elif check_mood(mood,which_mood["gaming"]):
    print("Alpha to Charli ! Alpha to Charli!!! ")
    print("\n")
    print("Your chooice is : \n1- Play GAME \n2- MEMES\n3- GAMING MUSIC")
    

    #gaming web site
    
    def play_game():
        import webbrowser
        webbrowser.open('http://poki.com', new=2)
        
    #memes 
      
    def memes():

        import webbrowser
        def open_html_page(file_path):
            webbrowser.open(file_path, new=2)

                    # Example usage
        html_file_path = r"C:\Users\harsh\mini_project_2\Untitled-1.html"
        open_html_page(html_file_path)
        
    #gaming music

    def gaming_music():
        music.gaming()
        

    _ch_made_=int(input(">>>"))

    match _ch_made_:
        case 1:
            play_game()
        

        case 2:
            memes()
        
        case 3:
            import module_music as music
            gaming_music()
        case _:
            print("ALPHA TO CHARLIE !!! ITS MAY_DAY BUT YOU ARE NOOB......")


elif check_mood(mood,which_mood["foody"]):

    websites = {
    "pizza": "https://www.dominos.co.in",
    "burger": "https://www.mcdonalds.co.in",
    "samosa": "https://www.haldirams.com",
    "biryani": "https://www.behrouzbiryani.com",
    "dosa": "https://www.saravanabhavan.com",
    "chaat": "https://www.bikanervala.com",
    "idli": "https://www.udupi.com",
    "vada pav": "https://www.gajananvadapav.com",
    "pani puri": "https://www.lokmithbhavan.com",
    "paratha": "https://www.paranthe.com",
    "chole bhature": "https://www.kwalityrestaurant.in",
    "butter chicken": "https://www.punjabgrill.in",
    "samosa pav": "https://www.chaipeenilane.com",
    "misal pav": "https://www.bedekar.com",
    "dhokla": "https://www.khaman.com",
    "tandoori chicken": "https://www.nandos.co.in",
    "kulfi": "https://www.kuremal.com",
    "vada sambhar": "https://www.sagar.com",
    "kathi roll": "https://www.kusumrolls.com",
    "pav bhaji": "https://www.sardarspavbhaji.com",
    "rasgulla": "https://www.kc-das.com",
    "momo": "https://www.wowmomo.in",
    "jalebi": "https://www.rawatsweets.com",
    "papdi chaat": "https://www.kanha.com",
    "chicken biryani": "https://www.biryanihouse.com",
    "masala dosa": "https://www.malleshwarmasaladosa.com",
    "rabri": "https://www.halwakadhai.com",
    "rasgulla": "https://www.kcda.com",
    "kathi roll": "https://www.kusumrollcenter.com",
    "bhelpuri": "https://www.swastikbhelpuri.com",
    "taco": "https://www.tacobell.com",
    "pasta": "https://www.olivegarden.com",
    "ice cream": "https://www.baskinrobbins.com",
    "steak": "https://www.outback.com",
    "ramen": "https://www.ichiraku.com",
    "fried chicken": "https://www.kfc.com",
    "samosa": "https://www.haldirams.com"
    }


    food_item = input("What would you like to have : ")
    if food_item in websites:
        website = websites[food_item]
        print("Website for", food_item, "is:", website)

        webbrowser.open(website,new=1)


    else:
        print("Website for", food_item, "is not available.")
        site=input("Enter Your Favourite site with domain : ")

        webbrowser.open(site)