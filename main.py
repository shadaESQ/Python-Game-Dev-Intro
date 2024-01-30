#نجهز المكتبات حقت بايثوم

import pygame
import time
import random
pygame.font.init()
# اول شيء  نجهز النافذة حقت اللعبة حقتنا بالارتفاع و العرض 
WIDTH, HEIGHT = 600, 600
#نسوي متغير عشان نستدعيه في الكلاس الاساسي او الفانكشن الاساسية 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#عنوان النافذة
pygame.display.set_caption("Space Dodge")
#هنا نسوي الخلفية حقت النافذة حقتنا ممكن باي لون او صورة 
#نقدر نكتبه ممكن  BG = pygame.image.load("bg.jpeg") لكن عشان نخلي الخلفية الي حطيناها تجي على مقاس النافذة الافضل نكنت الامر كدا 

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
#هنا نزبط خصائص اللاعب حقنا من عرض و ارتفاع راح يكون شكله مستطيل كبداية طبعا ممكن نحط شكل اخر اخر او حتى تصميم لشخصية ولكن للبساطة
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
#هنا اعطينا قيمة لسرعة اللاعب حقنا 
PLAYER_VEL = 5
#ه
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "purple", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
