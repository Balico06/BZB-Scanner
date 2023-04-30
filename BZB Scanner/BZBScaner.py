
from asyncore import write
from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')


print(f"""{Fore.LIGHTBLUE_EX}

  ________  ________  ________          ________  ________  ________  ________  ________  _______   ________     
|\   __  \|\_____  \|\   __  \        |\   ____\|\   __  \|\   __  \|\   __  \|\   __  \|\  ___ \ |\   __  \    
\ \  \|\ /_\|___/  /\ \  \|\ /_       \ \  \___|\ \  \|\  \ \  \|\  \ \  \|\ /\ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \   __  \   /  / /\ \   __  \       \ \  \  __\ \   _  _\ \   __  \ \   __  \ \   __  \ \  \_|/_\ \   _  _\   𝐵𝓎 𝐵𝒶𝓁𝒾𝒸𝑜 𝒶𝓃𝒹 𝒵𝑒𝓎𝓇𝑜𝓍 𝒶𝓃𝒹 𝐵𝒾𝑔𝒦𝓊𝓇𝒶
  \ \  \|\  \ /  /_/__\ \  \|\  \       \ \  \|\  \ \  \\  \\ \  \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\\________\ \_______\       \ \_______\ \__\\ _\\ \__\ \__\ \_______\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|        \|_______|\|__|\|__|\|__|\|__|\|_______|\|_______|\|_______|\|__|\|__|
                                                                                                                   

            Welcome to builder

""")

import asyncio
import aiohttp
import time
import os


Write.Print("\nIP: ", Colors.purple_to_blue)
async def ip():
   os.system("cls")
   arg1 = input ("ip:")
   if arg1 == "":
       print("invalid ip")
   else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"http://ip-api.com/json/{arg1}?fields=66846719") as r:
                    js = await r.json()
                    myip = ('')

                    status = (js["status"])
                    if "fail" == status:
                        message = (js["message"])
                        print(message)
                    else:
                        continent = (js["continent"])
                        country = (js["country"])
                        region = (js["regionName"])
                        city = (js["city"])
                        rue = (js["district"])
                        zipcode = (js["zip"])
                        lat = (js["lat"])
                        lon = (js["lon"])
                        timezone = (js["timezone"])
                        offset = (js["offset"])
                        iso = (js["isp"])
                        org = (js["org"])
                        reverse = (js["reverse"])
                        mobile = (js["mobile"])
                        proxy = (js["proxy"])
                        hosting = (js["hosting"])
                       #################
                        if continent == "":
                            continent = "None"
                        else:
                            continent = (js["continent"])
                            #
                        if country == "":
                            country == "None"
                        else:
                            country = (js["country"])
                            #
                        if region == "":
                            region = "None"
                        else:
                            region = (js["regionName"])
                            #
                        if city == "":
                            city = "None"
                        else:
                            city = (js["city"])
                            #
                        if rue == "":
                            rue = "None"
                        else:
                            rue = (js["district"])
                            #
                        if zipcode == "":
                            zipcode = "None"
                        else :
                            zipcode = (js["zip"])
                            #
                        if lat == "":
                            lat = "None"
                        else:
                            lat = (js["lat"])
                            #
                        if lon == "":
                            lon = "None"
                        else:
                            lon = (js["lon"])
                            #
                        if timezone == "":
                            timezone = "None"
                        else:
                            timezone = (js["timezone"])
                            #
                        if offset == "":
                            offset = "None"
                        else:
                            offset = (js["offset"])
                            #
                        if iso == "":
                            iso = "None"
                        else:
                           iso = (js["isp"])
			#
                        if org == "":
                            org = "None"
                        else:
                           org = (js["org"])
			#
                        if reverse == "":
                           reverse = "None"
                        else:
                           reverse = (js["reverse"])
			#
                        if mobile == "":
                            mobile = "None"
                        else:
                           mobile = (js["mobile"])
			#
                        if proxy == "":
                            proxy = "None"
                        else:
                           proxy = (js["proxy"])
			#
                        if hosting == "":
                            hosting = "None"
                        else:
                           hosting = (js["hosting"])
                           log = f"""
continent: {str(continent)}
country: {str(country)}
region: {str(region)}
city: {str(city)}
district: {str(rue)}
zipcode: {str(zipcode)}
latitude: {str(lat)}
longitude: {str(lon)}
timezone: {str(timezone)}
offset: {str(offset)}
isp: {str(iso)}
organisation: {str(org)}
reverse: {str(reverse)}
mobile: {str(mobile)}
proxy: {str(proxy)}
hosting: {str(hosting)}
"""
                        print(log)
                        file = input ("do you want txt file to save data [y/n]:")
                        if file == "y" or file == "yes":
                            with open(str(arg1)+'.txt', 'w') as f:
                                f.write(str(log))
                                time.sleep(5)
while True:
   asyncio.run(ip())
