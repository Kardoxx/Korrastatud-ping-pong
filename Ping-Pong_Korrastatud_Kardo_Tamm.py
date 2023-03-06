#Kardo Tamm
import pygame
import random

# initialiseerib pygame
pygame.init()

# Ekraani suurus
screenWidth = 640
screenHeight = 480
screen = pygame.display.set_mode([screenWidth, screenHeight])

# Tausta värv
bgColor = (200, 200, 200)

# Palli suurus ja kiirus
ballSize = 20
ballSpeedX = 5
ballSpeedY = 5

# Aluse suurus ja kiirus
paddleWidth = 120
paddleHeight = 20
paddleSpeed = 5

# Laeb mängu pildid
ballImg = pygame.image.load("ball.png").convert_alpha()
ballImg = pygame.transform.scale(ballImg, [ballSize, ballSize])
paddleImg = pygame.image.load("pad.png").convert_alpha()
paddleImg = pygame.transform.scale(paddleImg, [paddleWidth, paddleHeight])

# Laeb mängu helid
hitPaddleSound = pygame.mixer.Sound("hit_paddle.mp3")
hitGroundSound = pygame.mixer.Sound("hit_ground.mp3")
scoreSound = pygame.mixer.Sound("score.mp3")

pygame.mixer.music.load('musicBarely_Small.mp3')
pygame.mixer.music.set_volume(0.1)  # Määrab ära kui kõvasti mängu taustal heli käib


# Aluse positsioon
paddleX = screenWidth / 2 - paddleWidth / 2
paddleY = screenHeight - paddleHeight - 10

# Palli positsioon
ballX = random.randint(0, screenWidth - ballSize)
ballY = 0

# Skoor
score = 0

# Paneb mängu loopi
clock = pygame.time.Clock()
running = True
while running:

    # Muudab eventeid mängus
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Liigutab palli
    ballX += ballSpeedX
    ballY += ballSpeedY

    # Pall põrkab seintel
    if ballX <= 0 or ballX >= screenWidth - ballSize:
        ballSpeedX *= -1
    if ballY <= 0:
        score += 1
        scoreSound.play()  # Mängib skoori heli effekti
        ballX = random.randint(0, screenWidth - ballSize)
        ballY = 0
        ballSpeedY = 5
    if ballY >= screenHeight:
        hitGroundSound.play()  # Mängib palli maha kukkumis heli effekti
        running = False

    # Kokkupõrge aeruga
    if ballY + ballSize >= paddleY and ballX + ballSize >= paddleX and ballX <= paddleX + paddleWidth:
        ballSpeedY *= -1
        score += 1
        hitPaddleSound.play()  # mängib aerulöögi heliefekti

    # Liiguta alust
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddleX > 0:
        paddleX -= paddleSpeed
    if keys[pygame.K_RIGHT] and paddleX < screenWidth - paddleWidth:
        paddleX += paddleSpeed

    # Joonistab kõik ekraanile mis vaja
    screen.fill(bgColor)
    screen.blit(ballImg, (ballX, ballY))
    screen.blit(paddleImg, (paddleX, paddleY))

    # Joonistab skoori
    font = pygame.font.Font(None, 36)
    scoreText = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(scoreText, (10, 10))

    # Uuendab ekraani
    pygame.display.flip()

    # Limiteerib mängul Fps'i
    clock.tick(60)

# Lahkub pygamest
pygame.quit()
