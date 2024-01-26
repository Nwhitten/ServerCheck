#!/usr/bin/env python3
import time

from datetime import datetime

import json
import urllib.request, urllib.error, urllib.parse#!/usr/bin/env python3

from displayhatmini import DisplayHATMini

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("""This example requires PIL/Pillow, try:

sudo apt install python3-pil

""")

#from font_fredoka_one import FredokaOne

import signal
import requests
def website_up(url):
    try:
        r = requests.get(url)
        return r.ok
    except:
        return False

import subprocess, platform

def pingOk(sHost):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)

    except Exception as e:
        return False

    return True

def getsize(font, text):
    _, _, right, bottom = font.getbbox(text)
    return (right, bottom)

def strwidth(font, text):
    _, _, right, bottom = font.getbbox(text)
    return (right)


def strheight(font, text):
    _, _, right, bottom = font.getbbox(text)
    return (bottom)




img = Image.open("/usr/local/bin/DHM_pihole_dark.jpg")

width = DisplayHATMini.WIDTH
height = DisplayHATMini.HEIGHT
buffer = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(buffer)

displayhatmini = DisplayHATMini(buffer, backlight_pwm=True)



font = ImageFont.load_default()



font_ArialB = ImageFont.truetype("/usr/local/bin/ArialBold.ttf",30)
fontti_ArialB = ImageFont.truetype("/usr/local/bin/ArialBold.ttf",25)
fontex_ArialB = ImageFont.truetype("/usr/local/bin/ArialBold.ttf",20)

fontPibo8 = ImageFont.truetype("/usr/share/fonts/truetype/piboto/Piboto-Bold.ttf",14)

fontPibo20 = ImageFont.truetype("/usr/share/fonts/truetype/piboto/Piboto-Regular.ttf",20)


brightness = 0.25

Cr,Cg,Cb = 255,127,0
Gr,Gg,Gb = 0,70,0
Ar,Ag,Ab = 130,60,0
Rr,Rg,Rb = 255,0,0
RrX,RgX,RbX = 130,0,0

listfont = fontti_ArialB

textheight = strheight(listfont,"PI")

Gappix = textheight + 6


dotrad = 14
dotcorr = 6
Vpix = 10


draw.text((0,0), "IP",font=font,fill=(200,200,200))
draw.text((20,0), "Ser",font=font,fill=(200,200,200))

V0 = Vpix
V1 = Vpix+(Gappix*1)
V2 = Vpix+(Gappix*2)
V3 = Vpix+(Gappix*3)
V4 = Vpix+(Gappix*4)
V5 = Vpix+(Gappix*5)
V6 = Vpix+(Gappix*6)
V7 = Vpix+(Gappix*7)








draw.text((45,V0), "PiHole", font=listfont, fill=(255,255,255))
draw.text((45,V1), "", font=listfont, fill=(255,255,255))
draw.text((45,V2), "", font=listfont, fill=(255,255,255))
draw.text((45,V3), "Homebridge", font=listfont, fill=(255,255,255))
draw.text((45,V4), "CODEX", font=listfont, fill=(255,255,255))
draw.text((45,V5), "WhitFLIX", font=listfont, fill=(255,255,255))
draw.text((45,V6), "MacMini PLEX", font=listfont, fill=(255,255,255))
draw.text((45,V7), "WAN Connection", font=listfont, fill=(255,255,255))




blockedstringwidth = 320
blockedstring = "0%"
tempC = 0
current_time = ""

while True:

    #PiHole

    Hpix = 0
    Vpix = V0+dotcorr

    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(0,255,0),width=1)
    displayhatmini.display()
    if pingOk('192.168.11.125'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()



    #Vpix = 10
    Hpix = Hpix+23
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()

    if website_up('http://192.168.11.125/admin/'):
        f = urllib.request.urlopen('http://192.168.11.125/admin/api.php?summaryRaw&auth=bf24d2aa74054bb73b640c7bcbb111255e1a573fb308f9e0deaade9017e4f0b2')
        json_string = f.read()
        parsed_json = json.loads(json_string)

        adsblocked = parsed_json['ads_blocked_today']
        ratioblocked = parsed_json['ads_percentage_today']
        holestatus = parsed_json['status']

        dns_queries_today = parsed_json['dns_queries_today']
        unique_clients  = parsed_json['unique_clients']
        dns_queries  = parsed_json['dns_queries_all_types']
        blocked_domains  = parsed_json['domains_being_blocked']

        f.close()
        if holestatus == "enabled":
            draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
            draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
        else:
            draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    else:
        adsblocked = 0
        ratioblocked = 0
        holestatus = "Unavailable"

        dns_queries_today = 0
        unique_clients  = 0
        dns_queries  = 0
        blocked_domains  = 0

        draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,0,255))
    displayhatmini.display()



#Pihole Stats
    sr,sg,sb = 255,255,255
    hr,hg,hb = 200,200,200
    Statfont = fontPibo8

    draw.rectangle((0,V1,229,V3-1),(0,0,0))



    draw.text((0,39), 'Total queries (' + str(unique_clients) + ' clients)' , (hr,hg,hb), font=Statfont)
    draw.text((170,39), str(dns_queries) , (sr,sg,sb), font=Statfont)

    draw.text((0,52), 'Queries Blocked' , (hr,hg,hb), font=Statfont)
    draw.text((170,52), str(adsblocked) , (sr,sg,sb), font=Statfont)

    draw.text((0,65), 'Percent Blocked' , (hr,hg,hb), font=Statfont)
    draw.text((170,65), str("%.1f" % round(ratioblocked,2)) + "% ", (sr,sg,sb), font=Statfont)

    draw.text((0,78), 'Domains on Blocklist' , (hr,hg,hb), font=Statfont)
    draw.text((170,78), str(blocked_domains), (sr,sg,sb), font=Statfont)

    displayhatmini.display()










#Pihole Graph

 #   draw.text((width-blockedstringwidth,V4), blockedstring, (0,0,0), listfont)

#    blockedstring = str("%.1f" % round(ratioblocked,2)) + "%"
#    blockedstringwidth,blockedstringheight = getsize(listfont, blockedstring)


 #   draw.text((width-blockedstringwidth,V4), blockedstring, (200,200,200), listfont)

    piestart = 270
    pieone = 270+(ratioblocked*3.6)

    PieDiam = 55
    PieVpix = 39
    PieHpix = 230
    #PieHpix = width-PieDiam

    draw.ellipse((PieHpix,PieVpix,PieHpix+PieDiam,PieVpix+PieDiam),fill=(0,0,0),width=1,outline=(0,255,0))
    #draw.pieslice((PieHpix,PieVpix,PieHpix+PieDiam,PieVpix+PieDiam),start=pieone,end=piestart,width=2,outline=(0,255,0))
    draw.pieslice((PieHpix,PieVpix,PieHpix+PieDiam,PieVpix+PieDiam),start=piestart,end=pieone,width=0,fill=(255,0,0))

    displayhatmini.display()



#HomeBridge Admin 34
    Vpix = V3+dotcorr
    Hpix = 0
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if pingOk('192.168.11.160'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()


    #Vpix = 10
    Hpix = Hpix+23
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if website_up('http://192.168.11.160:8581/login/'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()



#CODEX 54
    Vpix = V4+dotcorr
    Hpix = 0
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if pingOk('192.168.11.190'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()


    #Vpix = 10
    Hpix = Hpix+23
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if website_up('http://192.168.11.190:3755/cgi-bin/'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()




#WHITFLIX 74
    Vpix = V5+dotcorr
    Hpix = 0
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if pingOk('192.168.11.190'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()

    #Vpix = 10
    Hpix = Hpix+23
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if website_up('http://192.168.11.190:32400/web/'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+10,Vpix+10),(255,0,0))
    displayhatmini.display()




#MacMini Admin 94
    Vpix = V6+dotcorr
    Hpix = 0
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if pingOk('192.168.11.100'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()


    #Vpix = 10
    Hpix = Hpix+23
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if website_up('http://192.168.11.100:32400/web/'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()



#Internet Check 220
    Vpix = V7+dotcorr
    Hpix = 0
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if pingOk('192.168.11.100'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()


    Hpix = 23
    draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),fill=(0,0,0),outline=(Cr,Cg,Cb),width=1)
    displayhatmini.display()
    if website_up('http://captive.apple.com'):
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(0,255,0))
    else:
         draw.ellipse((Hpix,Vpix,Hpix+dotrad,Vpix+dotrad),(255,0,0))
    displayhatmini.display()


#Temp Check228
    Vpix = V7
    Hpix = 280

    draw.text((Hpix,Vpix), str(tempC) + chr(176) + "c", font=listfont, fill=(0,0,0))

    cmd ="cat /sys/class/thermal/thermal_zone0/temp"
    thermal = subprocess.check_output(cmd, shell=True).decode("utf8")
    tempC =  int(round(float(thermal) / 1e3,1))


    if tempC <40:
        tr,tg,tb = 0,0,255
    elif tempC <50:
        tr,tg,tb = 0,255,0
    elif tempC >60:
        tr,tg,tb = 255,0,0
    else:
        tr,tg,tb = 255,255,255

    draw.text((Hpix,Vpix), str(tempC) + chr(176) + "c", font=listfont, fill=(tr,tg,tb))




    draw.text((245,0),str(current_time), (0,0,0), fontti_ArialB)

    now = datetime.now()
    current_time = str(now.strftime("%H:%M"))
    draw.text((245,0),str(current_time), (200,200,255), fontti_ArialB)


    displayhatmini.display()



    displayhatmini.set_backlight(brightness)


    time.sleep(5)

