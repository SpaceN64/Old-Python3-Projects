print("Checking connection...")
import time
time.sleep(0.4)

import socket
IPaddress=socket.gethostbyname(socket.gethostname())
if IPaddress=="127.0.0.1":
    print("No internet, your localhost is "+ IPaddress)
    exit()
else:
    print("Connected, with the IP address: "+ IPaddress )

time.sleep(0.4)

print("Checking Bootstrap...")
import os
time.sleep(0.6)

print("""
Welcome! This is a dictionary (about things aiden likes) by Aiden Sorabji!

----------------------------------

Last Updated: December 7, 2020
""")

Tesla = ["tesla"]
Apple = ["apple"]
iPhone = ["iPhone"]
iPad = ["iPad"]
Mac = ["mac"]
Discord = ["discord"]
Spotify = ["spotify"]
Youtube = ["youtube"]
Reddit = ["reddit"]
l2020 = ["2020"]
Python = ["python"]
Minecraft = ["minecraft"]
MacOs = ["macos"]
Family = ["family"]
Hi = ["hi", "hello", "Hi", "Hello"]
JackSucks = ["JackSucks"]

print("Please type a word:")
di = input(">>> ")

if di in Tesla:
    print("""Tesla

A car company owned by the famous Elon Musk (Kind of a Meme). Their cars
are famous for driving by themselves. This mode is called "Auto Pilot"
""")

elif di in Apple:
    print("""Apple

A Company based in Silcon Valley that sells a variety of products. Apple's
founder, Steve Jobs (See Also "Steve Jobs") created Apple as a Computer
company, but started selling different tech in the 1970s.""")

elif di in l2020:
    print("""2020 - The Year where everything went wrong

2020 Was a year where everything that could go wrong went wrong. They had
a Pandemic, multiple famous people dying (RIP), and other bad things.""")

elif di in Hi:
    print("Hello! What is your name?")
    name = input(">>> ")
    print("Hello, " + name + "!")
    time.sleep(0.8)

elif di in Python:
    print("""Python

A coding Language that this very code is using! :)""")
    
elif di in JackSucks:
    print("""JackSucksAtLife

A youtube channel with over a million subscribers on Youtube™ (As of Dec 7).
He is most known for his Minecraft Video's and intense screaming.

Most Viewed Video (Reuploaded): https://tinyurl.com/yyl6bvpp""")

elif di in 




time.sleep(9.5)  
print("")
print("""Exitting...""")
time.sleep(1)
exit()
