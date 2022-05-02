#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Tue Jan 25 14:31:51 2022

Système Solaire

@author: matthis
"""

import pygame 
import math
import time
import np
import button

pygame.init()

L = 1300
H=800
big_screen = pygame.display.set_mode((L, H))

little_screen = pygame.display.set_mode((100, 400))

largeur = 1600
hauteur = 800
screen = pygame.display.set_mode((largeur, hauteur))
middle_screen = (1300/2, 800/2)
img_play = pygame.image.load('Système Solaire/S.jpeg')

BG = (0, 0, 0)
white = (255,255,255)
font = pygame.font.Font(None, 20)
Font = pygame.font.Font(None, 30)
pause  = False

base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(1350, 650, 140, 50)
  

color_active = pygame.Color('lightskyblue3')
  

color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False






data = {'A' :['Mercure', 'poids = 3,33 x 10^23 kg', 'rayon = 4200 km', 'distance soleil = 46 à 70 mm km', 'temps de rotation = 87,969 j', 'température moyenne = 462°C', "Système solaire/MERCURE.jpeg",'A'],
                'B' : ['Venus','poids = 4,867 5x10^24 kg', 'rayon = 6050 km', 'distance soleil = 104 mm km', 'temps de rotation = 243 j', 'température moyenne = 440°C',"Système solaire/VENUS.jpeg"],
                'C' : ['La Terre','poids = 5,973 x 10^24 kg', 'rayon = 6378 km', 'distance soleil = 150 mm km', 'temps de rotation = 365 j', 'température moyenne = 14°C',"Système solaire/TERRE.jpeg"],
                'D' : ['Mars', 'poids = 6,418 x 10^23 kg','rayon = 3 396 km', 'distance soleil = 227 mm km', 'temps de rotation = 696 j', 'température moyenne = -60°C',"Système solaire/MARS.jpeg"],
                'E' : ['Jupyter', 'poids = 1,89 X 10^17 kg', 'rayon = 71 492 km', 'distance soleil = 778 mm km', 'temps de rotation = 11 ans 315 j', 'température moyenne = -163°C',"Système solaire/JUPITER.jpeg"],
                'F' : ['Saturne', 'poids = 5,68 X 10^26 kg', 'rayon = 58 232 km', 'distance soleil = 1,4 md km', 'temps de rotation = 29 ans et 167 j', 'température moyenne = -189°C',"Système solaire/SATURNE.jpeg"],
                'G' : ['Uranus', 'poids = 8,6 X 10^25 kg', 'rayon = 51 118 km','distance soleil = 2,8 md km', 'temps de rotation = 84 ans', 'température moyenne = -218°C',"Système solaire/URANUS.jpg"],
                'H' : ['Neptune', 'poids = 102 X 10^24 kg', 'rayon = 24 764 km', 'distance soleil = 4,5 md km', 'temps de rotation = 165 ans', 'température moyenne = -220°C',"Système solaire/NEPTUNE.jpeg"]}


d=1

Pleinelune = '/Users/matthis/Desktop/lune/01.png'



da= {'03:05:2022' : Pleinelune}

Pleinelune = '/Users/matthis/Desktop/lune/14.png'
Nouvellelune = '/Users/matthis/Desktop/lune/01.png'
croissant_1 = '/Users/matthis/Desktop/lune/04.png'
quartier_1 = '/Users/matthis/Desktop/lune/07.png'
croissant_2 = '/Users/matthis/Desktop/lune/21.png'
quatier_2 = '/Users/matthis/Desktop/lune/19.png' 




lune = False

def dessine_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


import time

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image(Pleinelune))
        self.images.append(load_image('/Users/matthis/Desktop/lune/02.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/03.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/04.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/05.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/06.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/07.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/08.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/09.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/10.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/11.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/12.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/13.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/14.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/15.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/16.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/17.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/18.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/19.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/20.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/21.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/22.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/23.png'))
        self.images.append(load_image('/Users/matthis/Desktop/lune/24.png'))
        # assuming both images are 64x64 pixels
        


        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        time.sleep(0.01)



class ecran():

    def __init__(self) -> None:
     
      def affichage_info(self) -> dict:

        for planete in data:
            if planete == data.key:
                return data.value
        
    def ecriture(self,planète):

        dataget = data[planète]

        text = font.render(dataget[0], 16, (0, 0, 0))

        poids = font.render(dataget[1], 16, (0, 0, 0))
        rayon = font.render(dataget[2], 1, (0, 0, 0))
        distance = font.render(dataget[3], 1, (0, 0, 0))
        rotation = font.render(dataget[4], 1, (0, 0, 0))
        temperature = font.render(dataget[5], 1, (0, 0, 0))

        screen.blit(text, (1320, 300))
        screen.blit(poids, (1320, 350))
        screen.blit(rayon, (1320, 400))
        screen.blit(distance, (1320, 450))
        screen.blit(rotation, (1320,500))
        screen.blit(temperature, (1320,550))

        img = pygame.image.load(dataget[-1])
        img = pygame.transform.scale(img, (280, 275))
        
        screen.blit(img, (1305, 20))
        pass
    
    def page_lune(self):
        pygame.draw.rect(screen, white, ((0, 0), (220, 220)))
        pygame.draw.rect(screen, (0,0,0), ((10, 10), (200, 200)))
        
        
    

def draw_bg():
	screen.fill(BG)

	text1 = "Entre date pour aligner les planete"

	pygame.draw.rect(screen, white, ((1300, 0), (1300, 800)))
	pygame.draw.line(screen, (0,0,0), (1300, 5), (1800, 5), 15)
	pygame.draw.line(screen, (0,0,0), (1300, 600), (1800, 600), 15)
	pygame.draw.line(screen, (0,0,0), (1595, 0), (1595, 800), 15)
	pygame.draw.line(screen, (0,0,0), (1300, 795), (1800, 795), 15)


    
class Soleil(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, name):
        pygame.sprite.Sprite.__init__(self)
        img =pygame.image.load(f'Système solaire/{name}')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.middle_screen = middle_screen
        self.t= 0
        self.x = np.cos(self.t) * 30
        self.y = np.sin(self.t) * 20 	
        self.name = 0
        self.v = 1
        self.a=(x,y)
        
        
    def lune(self, x: float, y: float,v, pos_terre) -> None :
        if pause:
            self.v = 0
        else:
            self.v = v
        self.t += 0.1*self.v*d
        self.x = np.cos(self.t) * 55
        self.y = np.sin(self.t) * 75
		
        self.rect.center = (pos_terre[0]+self.x, pos_terre[1]+self.y)
    
    def compteur_jour(self):
        pass

        

    def phase_lune(self):
        """
        img1 =pygame.image.load(f'Système solaire/{name}')    
        img2 =pygame.image.load(f'Système solaire/{name}')
        img3 =pygame.image.load(f'Système solaire/{name}')
        img4 =pygame.image.load(f'Système solaire/{name}')
        img5 =pygame.image.load(f'Système solaire/{name}')    
        img6 =pygame.image.load(f'Système solaire/{name}')
        img7 =pygame.image.load(f'Système solaire/{name}')
        img8 =pygame.image.load(f'Système solaire/{name}')
        
        

        """
        
        
        
        pass
    def draw(self):
        screen.blit(self.image, self.rect)
        
    def move(self, x: float, y: float, x_cos, x_sin, v,name) -> None :
        if pause:
            self.v = 0
        else:
            self.v = v
        self.t += 0.1*self.v*d
        self.x = np.cos(self.t) * x_cos
        self.y = np.sin(self.t) * x_sin
		
        self.rect.center = (self.middle_screen[0]+self.x, self.middle_screen[1]+self.y)
        self.name = name
        if name == 'C':

            self.a = self.rect.center
            pos_terre = self.a
            return pos_terre
    
            Soleil.lune(self,self.a[0], self.a[1],1)
            

    def clicked(self, mouse_pos: tuple=(0, 0)):
        mouse = pygame.mouse.get_pos()

        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="A":
            print(self.name)
            ecran.ecriture("A")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="B":
            print(self.name)
            ecran.ecriture("B")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="C":
            print(self.name)
            ecran.ecriture("C")       
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="D":
            print(self.name)
            ecran.ecriture("D")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="E":
            print(self.name)
            ecran.ecriture("E")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="F":
            print(self.name)
            ecran.ecriture("F")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="G":
            print(self.name)
            ecran.ecriture("G")
        if ((mouse[0] - self.middle_screen[0] - self.x)**2 + (mouse[1] - self.middle_screen[1] - self.y)**2)**0.5 <= 30 and pygame.mouse.get_pressed()[0] and self.name =="H":
            print(self.name)
            ecran.ecriture("H")

        
def texte_presentation():
    little_screen.fill(white)


#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
    
start_img = pygame.image.load('/Users/matthis/Desktop/Système Solaire/Unknown.png').convert_alpha()
exit_img = pygame.image.load('/Users/matthis/Desktop/Système Solaire/Unknown copie.png').convert_alpha()
pause_img = pygame.image.load('/Users/matthis/Desktop/Système Solaire/Unknown-2.png').convert_alpha()
play_img = pygame.image.load('/Users/matthis/Desktop/Système Solaire/Unknown-3.png').convert_alpha()

#create button instances
start_button = Button(220, 700, start_img, 0.5)
exit_button = Button(10, 700, exit_img, 0.5)
pause_button = Button(80, 700, pause_img, 0.5)
play_button = Button(150, 700, play_img, 0.5)

soleil = Soleil(1300/2, 800/2, 0.2,'S.jpeg')
mercure = Soleil(400, 320, 0.03,'mercure.jpg')
Venus = Soleil(500, 400, 0.04, 'Venus.jpg' )
terre = Soleil(600, 480, 0.04, 'Terre.jpg')
mars = Soleil(700, 560, 0.04, 'Mars.jpg')
Jupiter = Soleil(700, 560, 0.09, 'Jupiter.jpg')
saturne = Soleil(700, 560, 0.08, 'Saturne.jpg')
uranus = Soleil(700, 560, 0.19, 'uranus.jpeg')
neptune = Soleil(700, 560, 0.25, 'neptune.jpeg')
lune  = Soleil(650, 400, 0.02,'lune.jpg')


my_sprite = TestSprite()
my_group = pygame.sprite.Group(my_sprite)


astres = [soleil, mercure, Venus, terre, mars, Jupiter, saturne, uranus, neptune]

pause_l =True 

ecran = ecran()

run = True



print(da.get('03:05:2022'))

draw  = False 


while run:
    
    
    draw_bg()
    
    if start_button.draw(screen):
        d = d+1
    if exit_button.draw(screen):
        d=d-1
    if pause_button.draw(screen):
        pause= True
        pause_l = False
    if play_button.draw(screen):
        pause= False
        pause_l = True
        

    for astre in astres:
        astre.draw()
        astre.clicked()
        

    lune.draw()
    dessine_text('Entrez une date pour aligner les planète', font, BG, 1320, 700)
    dessine_text('Phase de la lune', font,(255,255,255), 50, 230)
    mercure.clicked()
    ecran.page_lune()    
    mercure.move(1, 1, 80, 40,0.6,'A')
    Venus.move(1,1, 140,90,1.6,'B')
    pos_terre = terre.move(1,1, 190, 130,1.2,'C')
    mars.move(1, 1, 250, 170,0.9,'D')
    Jupiter.move(1,1,350,250,0.4,'E')
    saturne.move(1,1,430, 340,0.3,'F')
    uranus.move(1,1, 500, 420,0.2,'G')
    neptune.move(1,1 , 530, 450,0.1,'H')
    lune.lune(1, 1, 2.5, pos_terre)

    time.sleep(0.05)
    
    for event in pygame.event.get():
		#quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            
            
            
            if event.key == pygame.K_a:
                ecran.ecriture("A")
            if event.key == pygame.K_b:
                ecran.ecriture("B")
            if event.key == pygame.K_c:
                ecran.ecriture("C")
            if event.key == pygame.K_d:
                ecran.ecriture("D")               
            if event.key == pygame.K_e:
                ecran.ecriture("E")
            if event.key == pygame.K_f:
                ecran.ecriture("F")
            if event.key == pygame.K_g:
                ecran.ecriture("G")             
            if event.key == pygame.K_h:
                ecran.ecriture("H")
            if event.key == pygame.K_l:
                ecran.page_lune()

                
                
            if event.key == pygame.K_p:
                pause = not pause
                pause_l = not pause_l
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN:
  
            if event.key == pygame.K_BACKSPACE:

                user_text = user_text[:-1]

            else:
                user_text += event.unicode
        if da.get(user_text):
            draw = True 
        if draw:
            screen.blit(pygame.image.load('/Users/matthis/Desktop/lune/07.png'), (100,100))


      
  
    if active:
        color = color_active
    else:
        color = color_passive
    
    if pause_l == True:
        my_group.update()
        my_group.draw(screen)
    else:
        my_group.draw(screen)


    
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(200, text_surface.get_width()+10)
    pygame.display.flip()        
    pygame.display.update()

pygame.quit()