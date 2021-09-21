import kahoot
from kahoot import client
import random

i = 1;
code = int(input("Kahoot Game Code: "))
i2 = int(input("Amount of bots: "))
name = input("What do you want to name the bots?: ")

while i < i2:
    botnum = str(random.randint(1,2000))
    bot = client()
    bot.join(code,name + botnum)
    def joinHandle():
        pass
    bot.on("joined",joinHandle)
    print(name + botnum + "Has joined the kahoot")
    
    i += 1
