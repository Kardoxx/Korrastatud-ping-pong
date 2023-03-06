#Kardo Tamm
import pygame
import random

# initialiseerib pygame
pygame.init()

# Ekraani suurus
screenWidth = 640 # Ekraani laius
screenHeight = 480 # Ekraani pikkus
screen = pygame.display.set_mode([screenWidth, screenHeight])

# Tausta värv
bgColor = (200, 200, 200) # RGB, esimene on punane, teine sinine ja kolmas arv roheline mis segatakse kokku

# Palli suurus ja kiirus
ballSize = 20 # Palli suurus
ballSpeedX = 5 # Palli kiirus x (Vasakule poole liikumise kiirus)
ballSpeedY = 5 # Palli kiirus Y (Paremale poole liikumise kiirus)

# Aluse suurus ja kiirus
paddleWidth = 120 # Aluse laius
paddleHeight = 20 # Aluse kõrgus
paddleSpeed = 5 #Aluse kiirus

# Laeb mängu pildid
ballImg = pygame.image.load("ball.png").convert_alpha()
ballImg = pygame.transform.scale(ballImg, [ballSize, ballSize])
paddleImg = pygame.image.load("pad.png").convert_alpha()
paddleImg = pygame.transform.scale(paddleImg, [paddleWidth, paddleHeight])

# Laeb mängu helid
hitPaddleSound = pygame.mixer.Sound("hit_paddle.mp3") # Aluse heli effekt
hitGroundSound = pygame.mixer.Sound("hit_ground.mp3") # Põranda heli effekt
scoreSound = pygame.mixer.Sound("score.mp3") # Skoori heli effekt

pygame.mixer.music.load('musicBarely_Small.mp3') # Tausta muusika
pygame.mixer.music.set_volume(0.1)  # Määrab ära kui kõvasti mängu taustal heli käib


# Aluse positsioon
paddleX = screenWidth / 2 - paddleWidth / 2 #Määrab pisklitega kordinaadid alusele
paddleY = screenHeight - paddleHeight - 10 # Määrab pisklitega kordinaadid alusele

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

    # Kokkupõrge alusega
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
    screen.fill(bgColor) # Fillib tausta värvi
    screen.blit(ballImg, (ballX, ballY))
    screen.blit(paddleImg, (paddleX, paddleY))

    # Joonistab skoori
    font = pygame.font.Font(None, 36) # Annab suuruseks 36 ja fonti nimega "None"
    scoreText = font.render("Score: " + str(score), True, (0, 0, 0)) # See koodirida renderdab teksti "Skoor:", millele järgneb muutuja hinde väärtus, kasutades määratud fondi ja värvi.
    screen.blit(scoreText, (10, 10)) # Kasutatakse ScoreText objekti kuvamiseks Pygame'i ekraanil asukohas (10,10).

    # Uuendab ekraani
    pygame.display.flip()

    # Limiteerib mängul Fps'i
    clock.tick(60)

# Lahkub pygamest
pygame.quit()