import random
import math

WIDTH = 688
HEIGHT = 645
FLOOR = 440

enemy_start = 688
cloud_start = 688

trex = Actor("idle", (125, FLOOR))
cactus = Actor("cactus1", (544, FLOOR))
cactusture = ["cactus1", "cactus2", "cactus3", "cactus4", "cactus5"]
restart = Actor("1x-restart", center=(WIDTH/2,HEIGHT/2-100))

postures = ["run1", "run2"]
cloud = Actor("1x-cloud", (cloud_start, 100, ))
enemy1 = Actor("enemy1", (enemy_start, 200, ))
fly = ["enemy1", "enemy2"]

trex.above_ground = 0
frames_per_image = 6
x,e = 0,0
score = 1
trex_status = "PLAY"

speed = 10
FALL = 0.4
JUMP = -11
LIVES = 10

def draw():
    screen.clear()
   
    if trex_status=="PLAY" or trex_status=='Hit':
        screen.fill((255, 255, 255))
        screen.blit("floor-1", (45, 456))
        screen.draw.text(
            str(score), (500, 5), fontsize=50, fontname="pixelmix_bold", color="black"
        )
        screen.draw.text(
            str(math.floor(LIVES)), (100, 5), fontsize=50, fontname="pixelmix_bold", color="black"
        )
        trex.draw()
        cactus.draw()
        cloud.draw()
        enemy1.draw()
        
    elif trex_status == "dead":
        screen.fill((255, 255, 255))
        screen.draw.text("Game Over",center=(WIDTH/2,HEIGHT/2),fontsize=50, fontname="pixelmix_bold", color="black")
        restart.draw()
        
def update():
    global x,e, frames_per_image, score, LIVES, trex_status, cloud_start, enemy1, fly, enemy2, enemy_start
    if trex_status =="PLAY" or trex_status=="Hit":
        
        score += 1
        
        cloud_start -= 0.6
        cloud.x = cloud_start
       
        if cloud.x <= 0:
            cloud_start = 688
       
        if cloud.x <= 0:
            enemy_start = 688
        
        cactus.left -= speed
        
        if cactus.right < 59:
            cactus.left = 544
            cactus.image = random.choice(cactusture)
        
        trex.image = postures[x // frames_per_image]
        
        x +=1
        if x // frames_per_image >=len (postures):
            x = 0
        
        trex.above_ground += FALL
        trex.y += trex.above_ground
        if(trex.y > FLOOR):
            trex.y = FLOOR
        elif trex.y < FLOOR-65:
            trex.y = FLOOR-65
        
        enemy_start -= 0.6
        enemy1.x = enemy_start
        
        if enemy1.right < 59:
            enemy1.left = 544
        
        enemy1.image = fly[e // frames_per_image]
        e +=1
        
        if e // frames_per_image >=len (fly):
            e = 0
        
        if trex.colliderect(cactus):
            trex_status = "Hit"
            print(trex_status)
            trex.image = "death"
            score = 0
            print(score)
            LIVES -= 1/7.5
        if LIVES <1:
            trex_status = "dead"

def on_mouse_down(pos):
    global trex_status,LIVES,score
    if restart.collidepoint(pos):
        print("Hit Restart")
        LIVES = 10
        score = 0
        trex_status = "PLAY"

def trex_jump():
    trex.above_ground = JUMP
    
def on_key_down():
    if keyboard.SPACE:
        clock.schedule_unique(trex_jump, 0.2)
        
