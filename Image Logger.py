from colorama import Fore, init
from discord_webhook import DiscordEmbed, DiscordWebhook
import requests
import os
import colorama
import sys
import time
colorama.init()

# This is an Fake Image logger
# U can change code and make it ur own image logger to sell to people...

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();time.sleep(0.05)

os.system('cls')
print(colorama.Fore.RED)
print_slow("Welcome to Image Logger Made By Termed!\n")
# Change Title if you want!

init()
os.system("title 𝙏𝙚𝙧𝙢𝙚𝙙 𝙄𝙢𝙖𝙜𝙚 𝙇𝙤𝙜𝙜𝙚𝙧")
os.system("cls")
print(f"""
{Fore.RED} ██▓ ███▄ ▄███▓ ▄▄▄        ▄████ ▓█████ {Fore.BLUE}     ██▓     ▒█████    ▄████   ▄████ ▓█████  ██▀███  
{Fore.RED}▓██▒▓██▒▀█▀ ██▒▒████▄     ██▒ ▀█▒▓█   ▀ {Fore.BLUE}    ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
{Fore.RED}▒██▒▓██    ▓██░▒██  ▀█▄  ▒██░▄▄▄░▒███   {Fore.BLUE}    ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
{Fore.RED}░██░▒██    ▒██ ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ {Fore.BLUE}    ▒██░    ▒██   ██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
{Fore.RED}░██░▒██▒   ░██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒{Fore.BLUE}   ░██████▒░ ████▓▒░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
{Fore.RED}░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░{Fore.BLUE}   ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
{Fore.RED} ▒ ░░  ░      ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░{Fore.BLUE}   ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
{Fore.RED} ▒ ░░      ░     ░   ▒   ░ ░   ░    ░   {Fore.BLUE}     ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░ ░   ░    ░     ░░   ░ 
{Fore.RED} ░         ░         ░  ░      ░    ░  ░{Fore.BLUE}       ░  ░    ░ ░        ░       ░    ░  ░   ░                                                                                                                                                                                  
{Fore.RED}[Image Logger]{Fore.WHITE} Made By Termed$#0001
""")
# Change Title if you want..

print(
    f"{Fore.BLUE}[1]{Fore.WHITE} Image Logger")
print(
    f"{Fore.BLUE}[2]{Fore.WHITE} Webhook Tester")


Termed = input(f"{Fore.WHITE}[>>] ")

if Termed == "1":
        menu = 1

if Termed == "2":
    menu = 2


if menu ==1:
  os.system("cls")
  print_slow(f"{Fore.WHITE}Welcome to Image Logger Tool! ")
  input("Click Enter to Continue! ")
  os.system("cls")
  image = input(f"{Fore.WHITE}Input Image: ")
  os.system("cls")
  TermedName = input(f"{Fore.WHITE}Input Malicious File name: ")
  os.system("cls")
  Termedwebhook = input("input webhook: ")
  os.system("cls")
  print("loading...")
  time.sleep(2)
  os.system("cls")
  print("installing requirements...")
  time.sleep(2)
  os.system("cls")
  print(f"Turning {TermedName} into Image...")
  time.sleep(2)
  # This is just to make the image logger a bit more real!
  os.system('cls' if os.name == 'nt' else 'clear')
  print("loading...")
  time.sleep(2)
  os.system("cls")
  webhook = DiscordWebhook(url={Termedwebhook}, username="Image Logger",
  avatar_url="https://media.discordapp.net/attachments/755961047327703130/995950145734713354/IMG_0608.jpg?width=476&height=586",)
  embed = DiscordEmbed(title='Image Logger', description='Ur Image is here!', color='000000')
  embed.set_footer(text='Image Logger made by Termed$#0001 (c)',)
  embed.set_image(url=f'{image}', inline=False)
  webhook.add_embed(embed)
  response = webhook.execute()
  print(f"{Fore.WHITE}Ur Image is done! ")
  time.sleep(1)
  print(F"{Fore.WHITE}Check ur Discord Channel! ")
  time.sleep(1)
  input(F"{Fore.WHITE}Click Enter to Exit: ")
  exit()

if menu ==2:
  os.system("cls")

webhook = input("input webhook: ")
print("loading...")
webhook = DiscordWebhook(url={webhook}, username="Image Logger",
avatar_url="https://media.discordapp.net/attachments/755961047327703130/995950145734713354/IMG_0608.jpg?width=476&height=586",)
embed = DiscordEmbed(title='Image Logger', description='Webhook Working!', color='000000')
webhook.add_embed(embed)
response = webhook.execute()
input(f"{Fore.GREEN}Webhook is valid!")
os.system("cls")
input(f"{Fore.WHITE}Click enter to exit: ")
exit()
