##Imports
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "50, 100"

import pgzrun
import random

##Screen
WIDTH = 500
HEIGHT = 440
TITLE = "Flappy Bird"

##Figuren
bird = Actor("vogel.png")
bird.x = 166
bird.y = 250
bird.vy = 0
bird.space_pressed = False

pipe_oben = Actor("roehre_oben1")
pipe_unten = Actor("roehre_unten1")

pipe_oben1 = Actor("roehre_oben1")
pipe_unten1 = Actor("roehre_unten1")
NEXT1 = False
RESET1 = True

pipe_oben2 = Actor("roehre_oben1")
pipe_unten2 = Actor("roehre_unten1")
NEXT2 = False
RESET2 = True

background = Actor("background.png")

Bottom = Rect((0,440), (500, 0))
Top = Rect((0, 0), (500, 0))

##Werte
zwischenraum = 160
gravity = 0.3
points = 0
points_as_str = "0"

speed = 2
Change_Speed = False
speed_check = 2.5

first = "Press"
second = "'SPACE'"
third = "to Start"
fourth = "the Game!" 
go = False

flyzone = WIDTH - bird.x + 50

status = 1

player_name = ""
running = True
new_highscore = False

top_players = {
    "first": ("", 0),
    "second": ("", 0),
    "third": ("", 0)
}

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    
##Definitions
def draw():
    global NEXT1, NEXT2, RESET1, RESET2, player_name, status
    if status == 1:
        screen.clear()
        background.draw()
        screen.draw.text("Tipe in your name and press", (0, HEIGHT / 10 * 2), fontname="ps2pr.ttf", fontsize=18, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
        screen.draw.text("'ENTER'", (WIDTH / 10 * 3.5, HEIGHT / 10 * 3), fontname="ps2pr.ttf", fontsize=18, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
        screen.draw.text(player_name, (WIDTH / 10 * 2, HEIGHT / 10 * 6), fontname="ps2pr.ttf", fontsize=25, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
        
    if status == 2:
        background.draw()
        screen.draw.text(first, (WIDTH / 2.65, HEIGHT / 1.7), fontname="ps2pr.ttf", fontsize=25, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
        screen.draw.text(second, (WIDTH / 4.2, HEIGHT / 1.5), fontname="ps2pr.ttf", fontsize=38, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
        screen.draw.text(third, (WIDTH / 3.5, HEIGHT / 1.3), fontname="ps2pr.ttf", fontsize=25, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
        screen.draw.text(fourth, (WIDTH / 3.6, HEIGHT / 1.2), fontname="ps2pr.ttf", fontsize=25, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")        
        if keyboard.space:
            screen.clear()          
            status = 3
            
    if status == 3:
        background.draw()
        bird.draw()
        screen.draw.rect(Bottom, "black")
        screen.draw.rect(Top, "black")
        pipe_oben.draw()
        pipe_unten.draw()
        if pipe_oben.x == WIDTH - flyzone / 3:
            NEXT1 = True
         
        if NEXT1 == True:
            if RESET1 == True:
                pipe_oben1.x = WIDTH
                pipe_unten1.x = WIDTH
                print("work")
                RESET1 = False
            pipe_oben1.draw()
            pipe_unten1.draw()
            if pipe_oben1.x == WIDTH -flyzone / 3:
                NEXT2 = True
     
        if NEXT2 == True:
            if RESET2 == True:
                pipe_oben2.x = WIDTH
                pipe_unten2.x = WIDTH
                RESET2 = False
            pipe_oben2.draw()
            pipe_unten2.draw()

        screen.draw.text(points_as_str, (10, 10), fontname="ps2pr.ttf", fontsize=25, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")        
        if bird.image == "vogel_tot.png":
            text = "Game Over"
            if new_highscore:
                screen.draw.text("You reached a new highscore!", (0, HEIGHT / 2), fontname="ps2pr.ttf", fontsize=18, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
            screen.draw.text(text, (WIDTH / 6, HEIGHT / 4), fontname="ps2pr.ttf", fontsize=38, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
            screen.draw.text(f"Best: {top_players['first'][0]} - {top_players['first'][1]} points", (0, HEIGHT / 10 * 7), fontname="ps2pr.ttf", fontsize=18, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
            screen.draw.text(f"Second: {top_players['second'][0]} - {top_players['second'][1]} points", (0, HEIGHT / 10 * 8), fontname="ps2pr.ttf", fontsize=18, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")
            screen.draw.text(f"Third: {top_players['third'][0]} - {top_players['third'][1]} points", (0, HEIGHT / 10 * 9), fontname="ps2pr.ttf", fontsize=18, color=(255, 165, 0), shadow=(1.5,1.5), scolor="black")

def build_pipe():
    mitte = random.randrange(zwischenraum, HEIGHT - zwischenraum)
    pipe_oben.bottom = mitte - zwischenraum / 2
    pipe_unten.top = mitte + zwischenraum / 2
    pipe_oben.left = WIDTH
    pipe_unten.left = WIDTH

def build_pipe1():
    mitte1 = random.randrange(zwischenraum, HEIGHT - zwischenraum)
    pipe_oben1.bottom = mitte1 - zwischenraum / 2
    pipe_unten1.top = mitte1 + zwischenraum / 2
    pipe_oben1.left = WIDTH
    pipe_unten1.left = WIDTH

def build_pipe2():
    mitte2 = random.randrange(zwischenraum, HEIGHT - zwischenraum)
    pipe_oben2.bottom = mitte2 - zwischenraum / 2
    pipe_unten2.top = mitte2 + zwischenraum / 2
    pipe_oben2.left = WIDTH
    pipe_unten2.left = WIDTH
    
def build_bird():
    bird.x = 160
    bird.y = 250
    bird.vy = 0
    
def move_pipes():
    global points, Change_Speed, speed, speed_check
    pipe_oben.x = pipe_oben.x - speed
    pipe_unten.x = pipe_unten.x - speed
    
    pipe_oben1.x = pipe_oben1.x - speed
    pipe_unten1.x = pipe_unten1.x - speed
    
    pipe_oben2.x = pipe_oben2.x - speed
    pipe_unten2.x = pipe_unten2.x - speed
    
    if points / speed_check == 2 and Change_Speed == False:
        speed = speed + 0.5
        speed_check = points
        Change_Speed = True

def move_bird():
    bird.vy = bird.vy + gravity
    bird.y = bird.y + bird.vy
    
def controll():
    tot = False
    if keyboard.space and not bird.space_pressed and bird.image != "vogel_tot.png":
        bird.vy = -6
        bird.image = "vogel_flap.png"        
    bird.space_pressed = keyboard.space
    if bird.vy > 0:
        bird.image = "vogel.png"
        
    if bird.colliderect(pipe_oben) or bird.colliderect(pipe_unten):
        print("1")
        bird.image = "vogel_tot.png"
        bird.vy = 0
        tot = True
    if bird.colliderect(pipe_oben1) or bird.colliderect(pipe_unten1):
        print("2")
        bird.image = "vogel_tot.png"
        bird.vy = 0
        tot = True
    if bird.colliderect(pipe_oben2) or bird.colliderect(pipe_unten2):
        print("3")
        bird.image = "vogel_tot.png"
        bird.vy = 0
        tot = True
    if bird.colliderect(Top):
        print("4b")
        bird.image = "vogel_tot.png"
        bird.vy = 0
        tot = True
    if bird.y > HEIGHT:
        print("4a")
        print(bird.y)
        bird.image = "vogel_tot.png"
        bird.vy = 0
        tot = True  

    if tot == True:
        print(pipe_oben.x, pipe_oben1.x, pipe_oben2.x)
        open_highscore()
        save_highscore(points, player_name)
        top_scores()
        
def update():
    global points, Change_Speed, points_as_str
    if status == 3:
        if bird.x >= pipe_oben.x:
            build_pipe()
            points = points + 1
            points_as_str = str(points)
            Change_Speed = False
        if NEXT1 == True:
            if bird.x >= pipe_oben1.x:
                build_pipe1()
                points = points + 1
                points_as_str = str(points)
                Change_Speed = False
        if NEXT2 == True:
            if bird.x >= pipe_oben2.x:
                build_pipe2()
                points = points + 1
                points_as_str = str(points)
                Change_Speed = False
        if bird.image != "vogel_tot.png":
            move_pipes()
            move_bird()
            controll()
            
def start_game():
    global running, status
    running = False
    screen.clear()
    status = 2

def on_key_down(key):
    global player_name, running
    if running:
        if key == keys.RETURN:
            start_game()
        elif key == keys.BACKSPACE:
            player_name = player_name[:-1]
        elif key.name in letters:
            player_name += key.name
        
def open_highscore():
    try:
        with open("highscore.txt", "r") as file:
            highscores = {}
            lines = file.readlines()
            for line in lines:
                try:
                    if line.index(": "):
                        player, score = line.strip().split(": ")
                        highscores[player] = int(score)
                except: ValueError
                
            return highscores             
    except FileNotFoundError:
        return {}
    
def save_highscore(points, player_name):
    global new_highscore
    highscores = open_highscore()
    if player_name in highscores:
        if points > highscores[player_name]:
            highscores[player_name] = points
            new_highscore = True
    else:
        highscores[player_name] = points
        new_highscore = True
    
    with open("highscore.txt", "w") as file:
        for player, score in highscores.items():
            file.write(f"{player}: {score}\n")

def top_scores():
    global top_players
    highscores = open_highscore()
    if highscores:
        sorted_scores = sorted(highscores.items(), key=lambda x: x[1], reverse=True)
        for idx, (player, score) in enumerate(sorted_scores[:3], start=1):
            if idx == 1:
                top_players["first"] = (player, score)
            elif idx == 2:
                top_players["second"] = (player, score)
            elif idx == 3:
                top_players["third"] = (player, score)
    else:
        print("Keine Highscores gefunden.")
    
build_pipe()
build_pipe1()
build_pipe2()

pgzrun.go()