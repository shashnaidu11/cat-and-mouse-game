import random
import pgzrun

TITLE="Cat and Mouse game"

HEIGHT=500
WIDTH=600
score=0
gameover=False
        
cat=Actor("cat")
cat.pos=(200,250)


mouse=Actor("mouse")
mouse.pos=(150,200)

def draw():
    screen.blit("bg",(0,0))
    cat.draw()
    mouse.draw()
   

    if gameover:
        screen.fill("red")
        screen.draw.text("times up!! your score is"+str(score),fontsize=40,color="black",center=(200,250))
        




def place_mouse():
    mouse.x=random.randint(70,550)
    mouse.y=random.randint(50,450)

def time_up():
    global gameover
    gameover=True


def update():
    global score

    if keyboard.left:
        cat.x=cat.x-2
    if keyboard.right:
        cat.x=cat.x+2
    if keyboard.up:
        cat.y=cat.y-2
    if keyboard.down:
        cat.y=cat.y+2
    
    if cat.colliderect(mouse):
        score+=10
        place_mouse()

clock.schedule(time_up,60.0)

    








pgzrun.go()
