from pygame import *
mixer.init()
by = 5
bx = 5
px = 600
py = 700

pl1 = 0
pl2 = 0


win_h = 700
win_w = 700
FPS = 60
clock = time.Clock()
window = display.set_mode((win_h,win_w))


font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 50)
font3 = font.Font(None, 50)
fon = 'fon.jpg'
platform = 'plat.png'
background = transform.scale(image.load(fon), (700,700))



class sprites(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    


    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Platform(sprites):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_w - 210:
            self.rect.y += self.speed
    def up(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_w - 210:
            self.rect.y += self.speed



platform = Platform(platform, 50,400, 30,200, 5)
platform2 = Platform('plat.png', 630,600, 30,200, 5)
ball = Platform('bal.png', 350,350,60,60,5)
finish = False
game = True
while game:
    events = event.get()
    keys = key.get_pressed()
    for i in events:
        if i.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        platform.reset()
        platform.up()
        platform2.reset()
        platform2.update()
        ball.reset()
        ball.rect.x += bx
        ball.rect.y += by
        window.blit(font1.render(f'{pl1}/5', True, (3, 0, 1)),(0,0))
        window.blit(font2.render(f'{pl2}/5',True, (3, 0, 1)),(650,0))
        if ball.rect.y < 0:
            by *= -1
        if ball.rect.y > 650:
            by *= -1
        if ball.rect.x > 650:
            ball.rect.x = 350
            bx *= -1
            pl1 += 1
        if ball.rect.x < 0 :
            ball.rect.x = 350
            bx *= -1
            pl2 += 1
        if ball.rect.colliderect(platform.rect):
            bx *= -1
        if ball.rect.colliderect(platform2.rect):
            bx *= -1
        if pl1 == 1:
            window.blit(font3.render('игрок 1 победил', True, (3, 0, 1)), (250,350))
            finish = True
        if pl2 == 1:
            window.blit(font3.render('игрок 2 победил', True, (3, 0, 1)), (250,350))
            finish = True
    display.update()
    clock.tick(FPS)
