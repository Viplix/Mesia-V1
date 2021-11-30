import random
import requests
import time
import threading
import base64
from os import name, chdir
from os.path import isfile
from pystyle import Anime, Colorate, Colors, Center, System, Write
from termcolor import cprint
import os
import subprocess
import socket 
import random, json, string

hostname = socket.gethostname() 
current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
IPAddr = socket.gethostbyname(hostname) 

file1 = open('Groups.txt', 'r')
Lines = file1.readlines()
file2 = open('People.txt', 'r')
Line = file2.readlines()
file3 = open('Proxies.txt', 'r')
proxies = file3.readlines()
file4 = open('UserAgents.txt', 'r')
userAgents = file4.readlines()
nl = []


keep_going = True
for i in userAgents:
  nl.append(i.replace('\n', ''))
userAgents = nl

file1.close()
file2.close()
file3.close()
file4.close()

list = []






if name == 'nt':
  path = '/'.join(__file__.split('\\')[:-1])
  chdir(path)




banner = """
                                                                                                                   
MMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEE   SSSSSSSSSSSSSSS IIIIIIIIII               AAA               
M:::::::M             M:::::::ME::::::::::::::::::::E SS:::::::::::::::SI::::::::I              A:::A              
M::::::::M           M::::::::ME::::::::::::::::::::ES:::::SSSSSS::::::SI::::::::I             A:::::A             
M:::::::::M         M:::::::::MEE::::::EEEEEEEEE::::ES:::::S     SSSSSSSII::::::II            A:::::::A            
M::::::::::M       M::::::::::M  E:::::E       EEEEEES:::::S              I::::I             A:::::::::A           
M:::::::::::M     M:::::::::::M  E:::::E             S:::::S              I::::I            A:::::A:::::A          
M:::::::M::::M   M::::M:::::::M  E::::::EEEEEEEEEE    S::::SSSS           I::::I           A:::::A A:::::A         
M::::::M M::::M M::::M M::::::M  E:::::::::::::::E     SS::::::SSSSS      I::::I          A:::::A   A:::::A        
M::::::M  M::::M::::M  M::::::M  E:::::::::::::::E       SSS::::::::SS    I::::I         A:::::A     A:::::A       
M::::::M   M:::::::M   M::::::M  E::::::EEEEEEEEEE          SSSSSS::::S   I::::I        A:::::AAAAAAAAA:::::A      
M::::::M    M:::::M    M::::::M  E:::::E                         S:::::S  I::::I       A:::::::::::::::::::::A     
M::::::M     MMMMM     M::::::M  E:::::E       EEEEEE            S:::::S  I::::I      A:::::AAAAAAAAAAAAA:::::A    
M::::::M               M::::::MEE::::::EEEEEEEE:::::ESSSSSSS     S:::::SII::::::II   A:::::A             A:::::A   
M::::::M               M::::::ME::::::::::::::::::::ES::::::SSSSSS:::::SI::::::::I  A:::::A               A:::::A  
M::::::M               M::::::ME::::::::::::::::::::ES:::::::::::::::SS I::::::::I A:::::A                 A:::::A 
MMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEE SSSSSSSSSSSSSSS   IIIIIIIIIIAAAAAAA                   AAAAAAA
                                                                                                                  
                                                                                                                  """[1:]

ascii = '''
███╗   ███╗███████╗███████╗██╗ █████╗ 
████╗ ████║██╔════╝██╔════╝██║██╔══██╗
██╔████╔██║█████╗  ███████╗██║███████║
██║╚██╔╝██║██╔══╝  ╚════██║██║██╔══██║
██║ ╚═╝ ██║███████╗███████║██║██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═╝
                                      '''[1:]





def init():
  os.system("title [MESIA] Login in..")
  System.Size(180, 50)
  Anime.Fade(text=Center.Center(banner), color=Colors.red_to_yellow, mode=Colorate.Vertical, enter=True)



menu = """
[1] Create Group  [3] Rename

[2] Spam User     [4] Soon...
"""

total_proxi = 0
for i in proxies:
  total_proxi = total_proxi + 1

loading = 0
init()
nl = []

for i in proxies:
  loading = loading + 1
  print(Colorate.Diagonal(Colors.red_to_yellow, " Scraped : "+i))
  nl.append(i.replace('\n', ''))
  os.system("title [MESIA] Scraping proxys ["+str(loading)+"/"+str(total_proxi)+"]")



proxies = nl
proxy = random.choice(proxies)
os.system('cls')
print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter("\n"+ascii)))
token = input(Colorate.Diagonal(Colors.red_to_yellow, "\n\n\n\n       User Token > "))
os.system("title [MESIA] Connected to "+str(current_machine_id))
headers = {"Authorization":str(token), "User-Agent": random.choice(userAgents)}
response = requests.get("https://discord.com/api/v9/users/787056370288427008/profile?with_mutual_guilds=true", headers=headers, proxies={"http":random.choice(proxies)})


names = [
            "Fuck you",
            "Stupid",
            "Ass",
            "Asshole",
            "Retard",
            "Fuck",
            "Raid",
            "Spam",
            "dont leave",
            "you cant leave",
            "get fucked",
            "bitch",
            "gore",
            "go outside",
            "mf",
            "motherfucker",
            "funny",
            "rage",
            "delete ur account",
            "i fucking hate u guys",
            "discord is a meme",
            "can not escape",
            "cant escape",
            "random shitty shit",
            "u are fucking gay",
            "imagine being dumb",
            "german fuckers",
            "u got a bad life lmao",
            "stop watching porn kid",
            "stfu",
            "lmao",
            "hehe i just hate you",
            "go work",
            "imagine wasting ur time by leaving",
            "u got such a low iq", "fuck your dad",
            "fuck your mom",
            "i fuck you until u die",
            "pls die already",
            "u cant stop me",
            "bruh",
            "pls burn in hell",
            "find us on Mesia",
            "fucked by Mesia",
            "wash ur hand lol",
            "sleep outside now",
            "hoes mad",
            "niqqa",
            "nigga",
            "sexy anna",
            "nibba",
            "best name idc",
            "fuck off",
            "oh boi you messed up",
            "bruh why you stink",
            "just calm down xD",
            "ur pants are wet lmao",
            "oh boi pls fuck me",
            "ur fucking sexy so go fuck me",
            "i love you so come to me and i fuck ya"]


def key_capture_thread():
    global keep_going
    input()
    keep_going = False



def create():
  proxy = random.choice(proxies)
  c = 0
  threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
  print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter("Press enter to stop")))
  while c < 100:
    if keep_going:
      c = c + 1
      time.sleep(1)
      data = {'recipients': []}
      response = requests.post("https://discord.com/api/v9/users/@me/channels",headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)},json=data, proxies={"http":random.choice(proxies)})
      try:
        ids = response.json()['id']
        f = open("Groups.txt", "a")
        f.write(f'{ids}')
        f.write(f'\n')
        f.close()
        os.system("title [MESIA] Created : "+str(c)+" Groups")
      except:
        cprint("Rate Limited", 'red')
        cprint(response.json(), 'blue')
        time.sleep(int(response.json()['retry_after']))
    else:
      break

headerss = {"Authorization" : f"{token}",
          "Content-Type" : "application/json",
          "User-Agent" : random.choice(userAgents)}


def addUser(target_id):
  r = requests.get("https://canary.discordapp.com/api/v6/users/@me", headers=headerss)
  tokeinfo = r.json()
  owner_id = tokeinfo["id"]
  while True:
    for line in Lines:
      r = requests.post('https://discordapp.com/api/v9/users/@me/channels', headers=headerss, json={"recipients":[f"{owner_id}", f"{target_id}"]})
      line = line.replace('\n', '')
      print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(target_id+" Added To : "+line)))

def removeUser(target_id):
  r = requests.get("https://canary.discordapp.com/api/v6/users/@me", headers=headerss)
  tokeinfo = r.json()
  owner_id = tokeinfo["id"]
  while True:
    for line in Lines:
      r = requests.delete('https://discordapp.com/api/v9/users/@me/channels', headers=headerss, json={"recipients":[f"{owner_id}", f"{target_id}"]})
      line = line.replace('\n', '')

def rename():
  r = requests.get("https://canary.discordapp.com/api/v6/users/@me", headers=headerss)
  for line in Lines:
    response = requests.patch(f'https://discord.com/api/v9/channels/'+line, headers=headers, json={'name': random.choice(names)})

def main():
  os.system('cls')
  print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter("\n"+ascii)))
  print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter("\n\n\n\n"+menu)))
  select = input(Colorate.Diagonal(Colors.red_to_yellow, "\n\n\n\n        Select > "))
  if select == "1":
    create()
    main()
  if select == "2":
    usrid = input(Colorate.Diagonal(Colors.red_to_yellow, "\n\n\n\n        User ID > "))
    addUser(usrid)
    main()
  if select == "3":
    rename()
    main()
  if select == "4":
    pass
    main()




main()
