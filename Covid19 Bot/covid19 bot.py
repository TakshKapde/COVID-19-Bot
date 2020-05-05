from urllib.request import urlopen
import json
import pygame

url = 'https://api.covid19api.com/summary'
url_open = urlopen(url)

json_data = json.load(url_open)

# Global Data
global_cases = json_data["Global"]["TotalConfirmed"]
global_deaths = json_data["Global"]["TotalDeaths"]

# USA
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'United States of America':
        usa_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        usa_total_deaths = json_data["Countries"][x]["TotalDeaths"]      

# Spain
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Spain':
        spain_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        spain_total_deaths = json_data["Countries"][x]["TotalDeaths"]  
        
# Canada
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Canada':
        canada_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        canada_total_deaths = json_data["Countries"][x]["TotalDeaths"]  

# China
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'China':
        china_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        china_total_deaths = json_data["Countries"][x]["TotalDeaths"]  
        
# Italy
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Italy':
        italy_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        italy_total_deaths = json_data["Countries"][x]["TotalDeaths"]  

# UK
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'United Kingdom':
        uk_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        uk_total_deaths = json_data["Countries"][x]["TotalDeaths"]  

# France
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'France':
        france_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        france_total_deaths = json_data["Countries"][x]["TotalDeaths"]

# Germany
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Germany':
        germany_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        germany_total_deaths = json_data["Countries"][x]["TotalDeaths"]  

# Turkey no flag pic
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Turkey':
        turkey_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        turkey_total_deaths = json_data["Countries"][x]["TotalDeaths"]  

# Iran no flag pic
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Iran, Islamic Republic of':
        iran_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        iran_total_deaths = json_data["Countries"][x]["TotalDeaths"]  

# Russia
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Russian Federation':
        russia_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        russia_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# Brazil
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Brazil':
        brazil_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        brazil_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# Belgium 
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == 'Belgium':
        belgium_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        belgium_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# Switzerland
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Switzerland":
        switzerland_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        switzerland_total_deaths = json_data["Countries"][x]["TotalDeaths"] 
        
# Netherlands
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Netherlands":
        netherlands_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        netherlands_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# Portugal no flag pic
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Portugal":
        portugal_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        portugal_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# India
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "India":
        india_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        india_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# Peru no flag pic
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Peru":
        peru_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        peru_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# Ireland no flag pic
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Ireland":
        ireland_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        ireland_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# Sweden
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Sweden":
        sweden_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        sweden_total_deaths = json_data["Countries"][x]["TotalDeaths"] 
        
# Austria
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Austria":
        austria_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        austria_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

# Israel
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Israel":
        israel_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        israel_total_deaths = json_data["Countries"][x]["TotalDeaths"] 
        
# Japan
for x in range(len(json_data["Countries"])):
    if (json_data["Countries"][x]["Country"]) == "Japan":
        japan_total_cases = json_data["Countries"][x]["TotalConfirmed"]
        japan_total_deaths = json_data["Countries"][x]["TotalDeaths"] 

pygame.init()

#dimensions
width = 800
height = 600

# creating screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("COVID-19 Bot")
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
running = True
# Country flags
def usa_image():
    usa_img = pygame.image.load('usa.png')
    usa_imgX = 50
    usa_imgY = 75
    screen.blit(usa_img, (usa_imgX, usa_imgY))
def spain_image():
    spain_img = pygame.image.load('spain.png')
    spain_imgX = 200
    spain_imgY = 75
    screen.blit(spain_img, (spain_imgX, spain_imgY))
def italy_image():
    italy_img = pygame.image.load('italy.png')
    italy_imgX = 350
    italy_imgY = 75
    screen.blit(italy_img, (italy_imgX, italy_imgY))
def france_image():
    france_img = pygame.image.load('france.png')
    france_imgX = 500
    france_imgY = 75
    screen.blit(france_img, (france_imgX, france_imgY))
def germany_image():
    germany_img = pygame.image.load('germany.png')
    germany_imgX = 650
    germany_imgY = 75
    screen.blit(germany_img, (germany_imgX, germany_imgY))
def uk_image():
    uk_img = pygame.image.load('uk.png')
    uk_imgX = 50
    uk_imgY = 200
    screen.blit(uk_img, (uk_imgX, uk_imgY))
def china_image():
    china_img = pygame.image.load('china.png')
    china_imgX = 200
    china_imgY = 200
    screen.blit(china_img, (china_imgX, china_imgY))
def russia_image():
    russia_img = pygame.image.load('russia.png')
    russia_imgX = 350
    russia_imgY = 200
    screen.blit(russia_img, (russia_imgX, russia_imgY))
def brazil_image():
    brazil_img = pygame.image.load('brazil.png')
    brazil_imgX = 500
    brazil_imgY = 200
    screen.blit(brazil_img, (brazil_imgX, brazil_imgY))
def belgium_image():
    belgium_img = pygame.image.load('belgium.png')
    belgium_imgX = 650
    belgium_imgY = 200
    screen.blit(belgium_img, (belgium_imgX, belgium_imgY))
def canada_image():
    canada_img = pygame.image.load('canada.png')
    canada_imgX = 50
    canada_imgY = 325
    screen.blit(canada_img, (canada_imgX, canada_imgY))
def netherlands_image():
    netherlands_img = pygame.image.load('netherlands.png')
    netherlands_imgX = 200
    netherlands_imgY = 325
    screen.blit(netherlands_img, (netherlands_imgX, netherlands_imgY))
def switzerland_image():
    switzerland_img = pygame.image.load('switzerland.png')
    switzerland_imgX = 350
    switzerland_imgY = 325
    screen.blit(switzerland_img, (switzerland_imgX, switzerland_imgY))
def india_image():
    india_img = pygame.image.load('india.png')
    india_imgX = 500
    india_imgY = 325
    screen.blit(india_img, (india_imgX, india_imgY))
def austria_image():
    austria_img = pygame.image.load('austria.png')
    austria_imgX = 650
    austria_imgY = 325
    screen.blit(austria_img, (austria_imgX, austria_imgY))
def israel_image():
    israel_img = pygame.image.load('israel.png')
    israel_imgX = 50
    israel_imgY = 450
    screen.blit(israel_img, (israel_imgX, israel_imgY))
def japan_image():
    japan_img = pygame.image.load('japan.png')
    japan_imgX = 200
    japan_imgY = 450
    screen.blit(japan_img, (japan_imgX, japan_imgY))

# earth image
def earth_image():
    earth_img = pygame.image.load('earth.png')
    earth_imgX = 85
    earth_imgY = 6
    screen.blit(earth_img, (earth_imgX, earth_imgY))

# letter c
def covid19_text():
    button_font = pygame.font.Font('GOODDP__.TTF', 80)
    rect_display = button_font.render('C', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display, (12, 0))
    button_font1 = pygame.font.Font('GOODDP__.TTF', 100)
    rect_display1 = button_font1.render('O', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display1, (8, 70))
    button_font2 = pygame.font.Font('GOODDP__.TTF', 80)
    rect_display2 = button_font2.render('V', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display2, (12, 170))
    button_font3 = pygame.font.Font('GOODDP__.TTF', 80)
    rect_display3 = button_font3.render('I', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display3, (20, 260))
    button_font4 = pygame.font.Font('GOODDP__.TTF', 80)
    rect_display4 = button_font4.render('D', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display4, (15, 345))
    button_font5 = pygame.font.Font('GOODDP__.TTF', 80)
    rect_display5 = button_font5.render('1', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display5, (20, 425))
    button_font6 = pygame.font.Font('GOODDP__.TTF', 80)
    rect_display6 = button_font6.render('9', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display6, (16, 505))
    

# total cases and death counter
def global_counter_top():
    # create the button
    rect = pygame.Rect(0, 0, width, 102)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 70)
    button_font1 = pygame.font.Font('GOODDP__.TTF', 30)
    # display global total cases
    rect_cases = button_font.render(str(global_cases), True, (255, 255, 255))
    infected_cases = button_font1.render('INFECTED', True, (255, 255, 255))
    screen.blit(rect_cases, (270, 10))
    screen.blit(infected_cases, (325, 65))

def global_counter_side():
    # create the button
    rect = pygame.Rect(0, 0, 60, height)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    rect_display = button_font.render('', True, (255, 255, 255))
    screen.blit(rect_display, (70, 178))

def global_counter_top_outline():
    # create the button
    rect = pygame.Rect(60, 103, 750, 3)
    rect_display = pygame.draw.rect(screen, [255, 255, 255], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 100)
    rect_display = button_font.render(str(), True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display, (270, 48))

def global_counter_side1_outline():
    # create the button
    rect = pygame.Rect(60, 103, 3, 500)
    rect_display = pygame.draw.rect(screen, [255, 255, 255], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 100)
    rect_display = button_font.render('', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display, (270, 198))
    
def global_counter_side2_outline():
    # create the button
    rect = pygame.Rect(60, 597, 750, 3)
    rect_display = pygame.draw.rect(screen, [255, 255, 255], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 100)
    rect_display = button_font.render('', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display, (270, 198))
    
def global_counter_side3_outline():
    # create the button
    rect = pygame.Rect(60, 0, 3, 500)
    rect_display = pygame.draw.rect(screen, [255, 255, 255], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 100)
    rect_display = button_font.render('', True, (255, 255, 255))
    # display global total deaths
    screen.blit(rect_display, (270, 198))
    
def global_counter_bottom_outline():
    # create the button
    rect = pygame.Rect(797, 103, 3, 500)
    rect_display = pygame.draw.rect(screen, [255, 255, 255], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 70)
    button_font1 = pygame.font.Font('GOODDP__.TTF', 30)
    rect_display = button_font.render(str(global_deaths), True, (255, 255, 255))
    # display global total deaths
    dead_cases = button_font1.render('DEAD', True, (255, 255, 255))
    screen.blit(rect_display, (550, 10))
    screen.blit(dead_cases, (600, 65))
    
# country by country cases and death counter
def usa_counter():
    # create the button
    rect = pygame.Rect(63, 183, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display usa total cases
    rect_cases = button_font.render(str(usa_total_cases), True, (255, 255, 255))
    # display usa total deaths
    rect_deaths = button_font.render(str(usa_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (70, 178))
    screen.blit(rect_deaths, (70, 198))

def spain_counter():
    # create the button
    rect = pygame.Rect(212, 183, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total spain cases
    rect_cases = button_font.render(str(spain_total_cases), True, (255, 255, 255))
    # display total spain deaths
    rect_deaths = button_font.render(str(spain_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (220, 178))
    screen.blit(rect_deaths, (220, 198))
    
def italy_counter():
    # create the button
    rect = pygame.Rect(363, 183, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total italy cases
    rect_cases = button_font.render(str(italy_total_cases), True, (255, 255, 255))
    # display total italy deaths
    rect_deaths = button_font.render(str(italy_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (369, 178))
    screen.blit(rect_deaths, (369, 198))
    
def france_counter():
    # create the button
    rect = pygame.Rect(513, 183, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total france cases
    rect_cases = button_font.render(str(france_total_cases), True, (255, 255, 255))
    # display total france deaths
    rect_deaths = button_font.render(str(france_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (518, 178))
    screen.blit(rect_deaths, (518, 198))

def germany_counter():
    # create the button
    rect = pygame.Rect(663, 183, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total germany cases
    rect_cases = button_font.render(str(germany_total_cases), True, (255, 255, 255))
    # display total germany deaths
    rect_deaths = button_font.render(str(germany_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (667, 178))
    screen.blit(rect_deaths, (667, 198))

def uk_counter():
    # create the button
    rect = pygame.Rect(63, 310, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total uk cases
    rect_cases = button_font.render(str(uk_total_cases), True, (255, 255, 255))
    # display total uk deaths
    rect_deaths = button_font.render(str(uk_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (70, 305))
    screen.blit(rect_deaths, (70, 325))

def china_counter():
    # create the button
    rect = pygame.Rect(212, 310, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total china cases
    rect_cases = button_font.render(str(china_total_cases), True, (255, 255, 255))
    # display total china deaths
    rect_deaths = button_font.render(str(china_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (220, 305))
    screen.blit(rect_deaths, (220, 325))

def russia_counter():
    # create the button
    rect = pygame.Rect(364, 302, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total russia cases
    rect_cases = button_font.render(str(russia_total_cases), True, (255, 255, 255))
    # display total russia deaths
    rect_deaths = button_font.render(str(russia_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (371, 297))
    screen.blit(rect_deaths, (371, 317))

def brazil_counter():
    # create the button
    rect = pygame.Rect(513, 310, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total brazil cases
    rect_cases = button_font.render(str(brazil_total_cases), True, (255, 255, 255))
    # display total brazil deaths
    rect_deaths = button_font.render(str(brazil_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (520, 305))
    screen.blit(rect_deaths, (520, 325))

def belgium_counter():
    # create the button
    rect = pygame.Rect(663, 310, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total belgium cases
    rect_cases = button_font.render(str(belgium_total_cases), True, (255, 255, 255))
    # display total belgium deaths
    rect_deaths = button_font.render(str(belgium_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (670, 305))
    screen.blit(rect_deaths, (670, 325))

def canada_counter():
    # create the button
    rect = pygame.Rect(63, 433, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total canada cases
    rect_cases = button_font.render(str(canada_total_cases), True, (255, 255, 255))
    # display total canada deaths
    rect_deaths = button_font.render(str(canada_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (70, 428))
    screen.blit(rect_deaths, (70, 448))

def netherlands_counter():
    # create the button
    rect = pygame.Rect(213, 433, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total netherlands cases
    rect_cases = button_font.render(str(netherlands_total_cases), True, (255, 255, 255))
    # display total netherlands deaths
    rect_deaths = button_font.render(str(netherlands_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (220, 428))
    screen.blit(rect_deaths, (220, 448))

def switzerland_counter():
    # create the button
    rect = pygame.Rect(366, 442, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total switzerland cases
    rect_cases = button_font.render(str(switzerland_total_cases), True, (255, 255, 255))
    # display total switzerland deaths
    rect_deaths = button_font.render(str(switzerland_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (373, 437))
    screen.blit(rect_deaths, (373, 457))

def india_counter():
    # create the button
    rect = pygame.Rect(513, 433, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total india cases
    rect_cases = button_font.render(str(india_total_cases), True, (255, 255, 255))
    # display total india deaths
    rect_deaths = button_font.render(str(india_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (520, 428))
    screen.blit(rect_deaths, (520, 448))

def austria_counter():
    # create the button
    rect = pygame.Rect(663, 433, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total austria cases
    rect_cases = button_font.render(str(austria_total_cases), True, (255, 255, 255))
    # display total austria deaths
    rect_deaths = button_font.render(str(austria_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (670, 428))
    screen.blit(rect_deaths, (670, 448))

def israel_counter():
    # create the button
    rect = pygame.Rect(63, 553, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total israel cases
    rect_cases = button_font.render(str(israel_total_cases), True, (255, 255, 255))
    # display total israel deaths
    rect_deaths = button_font.render(str(israel_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (70, 548))
    screen.blit(rect_deaths, (70, 568))

def japan_counter():
    # create the button
    rect = pygame.Rect(213, 553, 105, 42)
    pygame.draw.rect(screen, [0, 0, 0], rect)
    button_font = pygame.font.Font('GOODDP__.TTF', 30)
    # display total japan cases
    rect_cases = button_font.render(str(japan_total_cases), True, (255, 255, 255))
    # display total japan deaths
    rect_deaths = button_font.render(str(japan_total_deaths), True, (255, 255, 255))
    screen.blit(rect_cases, (220, 548))
    screen.blit(rect_deaths, (220, 568))

# checks if the game is still running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 155, 119))
    usa_image()
    canada_image()
    uk_image()
    china_image()
    brazil_image()
    austria_image()
    belgium_image()
    france_image()
    germany_image()
    india_image()
    israel_image()
    italy_image()
    japan_image()
    netherlands_image()
    russia_image()
    spain_image()
    switzerland_image()
    global_counter_top()
    global_counter_side()
    global_counter_top_outline()
    global_counter_side1_outline()
    global_counter_side2_outline()
    global_counter_side3_outline()
    global_counter_bottom_outline()
    earth_image()
    covid19_text()
    usa_counter()
    spain_counter()
    italy_counter()
    france_counter()
    germany_counter()
    uk_counter()
    china_counter()
    russia_counter()
    brazil_counter()
    belgium_counter()
    canada_counter()
    netherlands_counter()
    switzerland_counter()
    india_counter()
    austria_counter()
    israel_counter()
    japan_counter()
    pygame.display.update()