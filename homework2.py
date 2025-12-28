import pygame, random

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Game with Background, Score & Shapes")
clock = pygame.time.Clock()

# --- Load background image ---
background_image = pygame.image.load("cOMBATA.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# --- Colors ---
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 165, 0), (128, 0, 128)
]

# --- Font ---
font = pygame.font.SysFont("arial", 30, bold=True)

# --- Sprite class ---
class Shape(pygame.sprite.Sprite):
    def __init__(self, x, y, control=False):
        super().__init__()
        self.shape_type = random.choice(["circle", "square", "triangle"])  # random shape type
        self.color = random.choice(COLORS)
        self.size = 40
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)

        # Draw the shape
        self.draw_shape()

        self.rect = self.image.get_rect(center=(x, y))
        self.control = control
        self.dx, self.dy = random.choice([-3, 3]), random.choice([-3, 3])

    def draw_shape(self):
        self.image.fill((0, 0, 0, 0))  # transparent background
        color = random.choice(COLORS)
        if self.shape_type == "circle":
            pygame.draw.circle(self.image, color, (self.size // 2, self.size // 2), self.size // 2)
        elif self.shape_type == "square":
            pygame.draw.rect(self.image, color, (0, 0, self.size, self.size))
        elif self.shape_type == "triangle":
            points = [(self.size // 2, 0), (0, self.size), (self.size, self.size)]
            pygame.draw.polygon(self.image, color, points)

    def update(self, keys=None):
        # Random color flicker
        if random.randint(0, 25) == 0:
            self.draw_shape()

        if self.control:
            # Move player
            if keys[pygame.K_LEFT]:  self.rect.x -= 5
            if keys[pygame.K_RIGHT]: self.rect.x += 5
            if keys[pygame.K_UP]:    self.rect.y -= 5
            if keys[pygame.K_DOWN]:  self.rect.y += 5
        else:
            # Move randomly
            self.rect.x += self.dx
            self.rect.y += self.dy
            if self.rect.left < 0 or self.rect.right > WIDTH:  self.dx *= -1
            if self.rect.top < 0 or self.rect.bottom > HEIGHT: self.dy *= -1

# --- Sprite groups ---
all_sprites = pygame.sprite.Group()
random_shapes = pygame.sprite.Group()

# Player controlled shape (always a square)
player = Shape(WIDTH // 2, HEIGHT // 2, True)
player.shape_type = "square"
player.draw_shape()
all_sprites.add(player)

# Create 8 random shapes
for _ in range(8):
    shape = Shape(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    all_sprites.add(shape)
    random_shapes.add(shape)

# --- Game variables ---
score = 0
game_over = False

# --- Game loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add more random shapes with spacebar
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
            shape = Shape(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
            all_sprites.add(shape)
            random_shapes.add(shape)

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    # Collision: player touches shape → remove + score +1
    collisions = pygame.sprite.spritecollide(player, random_shapes, dokill=True)
    score += len(collisions)

    # If all shapes are gone
    if len(random_shapes) == 0:
        game_over = True

    # --- Draw section ---
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Display "You Win" when game over
    if game_over:
        win_text = font.render("You Win!", True, (255, 255, 255))
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
