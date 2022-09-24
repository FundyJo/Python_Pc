import ctypes
import os
import sys

import colorama
from colorama import Fore
from pystyle import Colors, Colorate, Write, System, Anime, Center

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
r = Fore.RESET


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n' * 120)
    return


def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"{_str}")
    elif system == 'posix':
        sys.stdout.write(f"{_str}")
    else:
        pass


setTitle("Prophecy")

gang = r'''

  _____                 _                     
 |  __ \               | |                    
 | |__) | __ ___  _ __ | |__   ___  ___ _   _ 
 |  ___/ '__/ _ \| '_ \| '_ \ / _ \/ __| | | |
 | |   | | | (_) | |_) | | | |  __/ (__| |_| |
 |_|   |_|  \___/| .__/|_| |_|\___|\___|\__, |
                 | |                     __/ |
                 |_|                    |___/ 

              Press Enter to start
'''
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.Center(gang), Colors.purple_to_blue, Colorate.Vertical, interval=0.030, enter=True)

System.Clear()

colorama.init()

Write.Print(f'', Colors.blue_to_purple, interval=0.000)
print('')
print('')
Write.Print(
    "                     $$$$$$$\                                $$\                                     \n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                     $$  __$$\                               $$ |                                    \n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                     $$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$$\ $$\   $$\ \n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                     $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$ |  $$ |\n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                     $$  ____/ $$ |  \__|$$ /  $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ /      $$ |  $$ |\n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                     $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      $$ |  $$ |\n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                     $$ |      $$ |      \$$$$$$  |$$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ \$$$$$$$ |\n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                     \__|      \__|       \______/ $$  ____/ \__|  \__| \_______| \_______| \____$$ |\n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                                                   $$ |                                    $$\   $$ |\n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                                                   $$ |                                    \$$$$$$  |\n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "                                                   \__|                                     \______/ \n",
    Colors.blue_to_purple, interval=0.000)
Write.Print(
    "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════",
    Colors.blue_to_purple, interval=0.001)

print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Server Joiner   {b}|{Fore.RESET}{m}[{w}9{Fore.RESET}{m}]{Fore.RESET}  Channel Spammer   {b}|{Fore.RESET}{m}[{w}17{Fore.RESET}{m}]{Fore.RESET} Patch Notes{Fore.RESET}         {b}|{Fore.RESET}{m}[{w}25{Fore.RESET}{m}]{Fore.RESET} Token Generator{Fore.RESET}
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Server Leaver   {b}|{Fore.RESET}{m}[{w}10{Fore.RESET}{m}]{Fore.RESET} DM Spammer        {b}|{Fore.RESET}{m}[{w}18{Fore.RESET}{m}]{Fore.RESET} About/Activity{Fore.RESET}      {b}|{Fore.RESET}{m}[{w}26{Fore.RESET}{m}]{Fore.RESET} Nitro Generator{Fore.RESET}
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Token Checker   {b}|{Fore.RESET}{m}[{w}11{Fore.RESET}{m}]{Fore.RESET} Friend Spammer    {b}|{Fore.RESET}{m}[{w}19{Fore.RESET}{m}]{Fore.RESET} Server Lookup{Fore.RESET}       {b}|{Fore.RESET}{m}[{w}27{Fore.RESET}{m}]{Fore.RESET} QR Token Grabber{Fore.RESET}
{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Token Onliner   {b}|{Fore.RESET}{m}[{w}12{Fore.RESET}{m}]{Fore.RESET} HypeSquad Joiner  {b}|{Fore.RESET}{m}[{w}20{Fore.RESET}{m}]{Fore.RESET} Token Infomation{Fore.RESET}    {b}|{Fore.RESET}{m}[{w}28{Fore.RESET}{m}]{Fore.RESET} Member ID Scraper{Fore.RESET}
{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Token Grabber   {b}|{Fore.RESET}{m}[{w}13{Fore.RESET}{m}]{Fore.RESET} Reaction Spammer  {b}|{Fore.RESET}{m}[{w}21{Fore.RESET}{m}]{Fore.RESET} Status Changer{Fore.RESET}      {b}|{Fore.RESET}{m}[{w}29{Fore.RESET}{m}]{Fore.RESET} PFP Changer{Fore.RESET}
{m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Server MassDM   {b}|{Fore.RESET}{m}[{w}14{Fore.RESET}{m}]{Fore.RESET} NickName Changer  {b}|{Fore.RESET}{m}[{w}22{Fore.RESET}{m}]{Fore.RESET} Group Spammer{Fore.RESET}       {b}|{Fore.RESET}{m}[{w}30{Fore.RESET}{m}]{Fore.RESET} About{Fore.RESET}
{m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Account Nuker   {b}|{Fore.RESET}{m}[{w}15{Fore.RESET}{m}]{Fore.RESET} Webhook Spammer   {b}|{Fore.RESET}{m}[{w}23{Fore.RESET}{m}]{Fore.RESET} Auto Login{Fore.RESET}          {b}|{Fore.RESET}{m}[{w}31{Fore.RESET}{m}]{Fore.RESET}{lr} THREADS{Fore.RESET}
{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} Server Nuker    {b}|{Fore.RESET}{m}[{w}16{Fore.RESET}{m}]{Fore.RESET} VC Spammer        {b}|{Fore.RESET}{m}[{w}24{Fore.RESET}{m}]{Fore.RESET} DM Deleter{Fore.RESET}          {b}|{Fore.RESET}{m}[{w}32{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT{Fore.RESET}''')
Write.Print(
    "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════",
    Colors.blue_to_purple, interval=0.001)

choice = input('\x1B[1m$: >>\x1B[1m ')

#   NITRO GENERATOR
if choice == '1':
    setTitle(f"Nitro Generator    |    ")



#   QR TOKEN GRABBER
elif choice == '2':
    setTitle(f"Nitro Generator    |    ")

