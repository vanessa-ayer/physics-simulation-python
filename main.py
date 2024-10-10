import pygame, sys, pymunk

def create_apple(space, pos): 
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 53)
    space.add(body, shape)
    return shape

def draw_apples(apples): # Drawn with pygame 
    for apple in apples: 
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x, pos_y))
        screen.blit(apple_surface, apple_rect)

def static_ball(space, pos): 
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_static_ball(balls): # Drawn with pygame 
    for ball in balls: 
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (248, 131, 121), (pos_x, pos_y), 50)

# General Setup 
pygame.init()
screen = pygame.display.set_mode((600,600)) #  Creating display surface 
clock = pygame.time.Clock() 
pygame.display.set_caption('Physics Simulation') 

# Variables (space, apples, and ball)
space = pymunk.Space() # physical space 
space.gravity = (0, 500) # Horizontal and veritcal gravity # (1000, 100) (wind example)

apple_surface = pygame.image.load('apple.png')
apples = [] 

balls = []
balls.append(static_ball(space, (445, 400)))
balls.append(static_ball(space, (225, 320)))


# Game Loop 
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))
    

    screen.fill((217, 217, 217)) # Background color 
    draw_apples(apples) 
    apple_surface = pygame.transform.scale(apple_surface, (300, 300))
    draw_static_ball(balls)
    space.step(1/50) # Update the simulation 
    pygame.display.update() # Rendering the frame 
    clock.tick(120) # Limiting frames per second to 120


