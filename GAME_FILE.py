# pygame Library 
import pygame
import time 
import random 
pygame.font.init()

# WINDOW SETTINGS FOR GAME 

WIDTH, HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FIGHTER IN SPACE")

# LOADING IMAGES (BACKGROUND AND SHIP)

BG = pygame.transform.scale(pygame.image.load("img.jpeg"),(WIDTH , HEIGHT))
SHIP_IMG = pygame.transform.scale(pygame.image.load("ship.png"),(40,60))

# VARIABLES CREATED

GAMER_WIDTH = 40
GAMER_HEIGHT = 60
GAMER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20 
STAR_VEL = 3

#FONT STYLE 

FONT = pygame.font.SysFont("comicsans",30)

# DRAWING GAMER(SHIP) , TIME STAMP , STARS(ENEMIES) AND SCORECARD (ENEMIES DODGED)

def draw(gamer , elapsed_time , stars , score) :
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time : {round(elapsed_time)}s" , 1 , "white")
    score_text = FONT.render(f"Score : {score}",1, "white")

    WIN.blit(time_text , (10,10))
    WIN.blit(score_text , (WIDTH - score_text.get_width() - 10, 10))

    WIN.blit(SHIP_IMG , (gamer.x , gamer.y))

    
    for star in stars :
        pygame.draw.rect(WIN , "white" , star)

    pygame.display.update()

# GAME FUNCTIONING 

def main() :
    run = True 
    
    gamer = pygame.Rect(200, HEIGHT - GAMER_HEIGHT, GAMER_WIDTH, GAMER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0 
 
    star_add_increment = 2000
    star_count = 0 

    stars = []
    hit = False 
    score = 0 


    while run :

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment :
            for _ in range(3) :
                star_x = random.randint(0 , WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x , -STAR_HEIGHT , STAR_WIDTH , STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200 , star_add_increment - 50)
            star_count = 0 

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False 
                break

        # GAMER MOVEMENTS 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and gamer.x - GAMER_VEL >= 0:
            gamer.x -= GAMER_VEL 
        if keys[pygame.K_RIGHT] and gamer.x + GAMER_VEL + GAMER_WIDTH  <= WIDTH:
            gamer.x += GAMER_VEL

        for star in stars[:] :
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
                score += 1           # for score (increase when a star is dodged)
            elif star.y + star.height >= gamer.y and star.colliderect(gamer):
                stars.remove(star)
                hit = True 
                break
        
        # WHEN ENEMY KILLS YOU 

        if hit :
            lost_text = FONT.render("YOU ARE FINISHED!", 1, "white")
            score_text = FONT.render(f"YOUR SCORE : {score}", 1, "white")
            WIN.blit(lost_text , (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            WIN.blit(score_text , (WIDTH/2 - score_text.get_width()/2 , HEIGHT/2 - score_text.get_height()/2 + 35))
            pygame.display.update()
            pygame.time.delay(4000)
            break 

        draw(gamer , elapsed_time , stars , score)

    pygame.quit()

if __name__ == "__main__":
    main()


# THANK YOU! THE GAME IS OVER (^_^)