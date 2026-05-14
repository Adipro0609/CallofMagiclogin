import pygame
import random
import math
from enum import Enum

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (150, 0, 255)
ORANGE = (255, 165, 0)
DARK_RED = (139, 0, 0)

class SpellType(Enum):
    FIREBALL = 1
    FROSTBOLT = 2
    LIGHTNING = 3
    HEAL = 4

class Spell:
    def __init__(self, spell_type, x, y, target_x=None, target_y=None):
        self.spell_type = spell_type
        self.x = x
        self.y = y
        self.target_x = target_x if target_x else x
        self.target_y = target_y if target_y else y
        self.speed = 8
        self.radius = 10
        self.active = True
        self.lifetime = 0
        
        if spell_type == SpellType.FIREBALL:
            self.damage = 25
            self.color = ORANGE
            self.max_lifetime = 120
            self.speed = 7
            self.radius = 12
        elif spell_type == SpellType.FROSTBOLT:
            self.damage = 15
            self.color = CYAN
            self.max_lifetime = 150
            self.speed = 6
            self.radius = 8
        elif spell_type == SpellType.LIGHTNING:
            self.damage = 30
            self.color = YELLOW
            self.max_lifetime = 30
            self.speed = 15
            self.radius = 6
        elif spell_type == SpellType.HEAL:
            self.damage = 0
            self.color = GREEN
            self.max_lifetime = 60
            self.speed = 5
            self.radius = 10
    
    def update(self):
        # Move towards target
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
        
        self.lifetime += 1
        if self.lifetime > self.max_lifetime:
            self.active = False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        # Add glow effect
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 2)

class Enemy:
    def __init__(self, x, y, wave):
        self.x = x
        self.y = y
        self.radius = 15
        self.max_health = 30 + (wave * 5)
        self.health = self.max_health
        self.speed = 1 + (wave * 0.2)
        self.damage = 5 + wave
        self.wave = wave
        self.color = (200 - wave * 10, 50, 50)
    
    def update(self, player_x, player_y):
        # Move towards player
        dx = player_x - self.x
        dy = player_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        # Draw health bar
        bar_width = 30
        bar_height = 5
        bar_x = self.x - bar_width // 2
        bar_y = self.y - self.radius - 10
        
        pygame.draw.rect(screen, RED, (bar_x, bar_y, bar_width, bar_height))
        health_percentage = self.health / self.max_health
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width * health_percentage, bar_height))
    
    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0

class PowerUp:
    def __init__(self, x, y, power_type):
        self.x = x
        self.y = y
        self.radius = 8
        self.power_type = power_type  # "health", "mana", "shield"
        self.lifetime = 0
        self.max_lifetime = 300
        
        if power_type == "health":
            self.color = RED
        elif power_type == "mana":
            self.color = BLUE
        else:  # shield
            self.color = PURPLE
    
    def update(self):
        self.lifetime += 1
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius, 2)
    
    def is_active(self):
        return self.lifetime < self.max_lifetime

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 12
        self.max_health = 100
        self.health = self.max_health
        self.max_mana = 150
        self.mana = self.max_mana
        self.shield = 0
        self.speed = 5
        self.color = BLUE
        self.mana_regen = 0.5
        
        # Spell cooldowns
        self.spell_cooldowns = {
            SpellType.FIREBALL: 0,
            SpellType.FROSTBOLT: 0,
            SpellType.LIGHTNING: 0,
            SpellType.HEAL: 0
        }
        self.spell_costs = {
            SpellType.FIREBALL: 30,
            SpellType.FROSTBOLT: 20,
            SpellType.LIGHTNING: 40,
            SpellType.HEAL: 25
        }
        self.spell_cooldown_max = {
            SpellType.FIREBALL: 10,
            SpellType.FROSTBOLT: 8,
            SpellType.LIGHTNING: 15,
            SpellType.HEAL: 12
        }
    
    def update(self, keys):
        # Movement
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed
        
        # Keep player in bounds
        self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))
        
        # Regenerate mana
        if self.mana < self.max_mana:
            self.mana += self.mana_regen
            self.mana = min(self.mana, self.max_mana)
        
        # Update cooldowns
        for spell in self.spell_cooldowns:
            if self.spell_cooldowns[spell] > 0:
                self.spell_cooldowns[spell] -= 1
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw health bar
        bar_width = 40
        bar_height = 6
        bar_x = self.x - bar_width // 2
        bar_y = self.y - self.radius - 20
        
        pygame.draw.rect(screen, DARK_RED, (bar_x, bar_y, bar_width, bar_height))
        health_percentage = self.health / self.max_health
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width * health_percentage, bar_height))
    
    def can_cast(self, spell_type):
        return (self.spell_cooldowns[spell_type] == 0 and 
                self.mana >= self.spell_costs[spell_type])
    
    def cast_spell(self, spell_type, target_x, target_y):
        if self.can_cast(spell_type):
            self.mana -= self.spell_costs[spell_type]
            self.spell_cooldowns[spell_type] = self.spell_cooldown_max[spell_type]
            return Spell(spell_type, self.x, self.y, target_x, target_y)
        return None
    
    def take_damage(self, damage):
        if self.shield > 0:
            self.shield -= damage
            if self.shield < 0:
                self.health += self.shield
                self.shield = 0
        else:
            self.health -= damage
    
    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)
    
    def add_mana(self, amount):
        self.mana = min(self.mana + amount, self.max_mana)
    
    def add_shield(self, amount):
        self.shield += amount

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Call of Magic ✨🪄")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.enemies = []
        self.spells = []
        self.powerups = []
        
        self.wave = 1
        self.enemies_spawned = 0
        self.enemies_per_wave = 5
        self.wave_timer = 0
        self.spawn_timer = 0
        self.score = 0
        self.game_over = False
        self.mouse_pos = (0, 0)
    
    def spawn_enemy(self):
        angle = random.uniform(0, 2 * math.pi)
        distance = 150
        x = self.player.x + math.cos(angle) * distance
        y = self.player.y + math.sin(angle) * distance
        
        x = max(30, min(SCREEN_WIDTH - 30, x))
        y = max(30, min(SCREEN_HEIGHT - 30, y))
        
        self.enemies.append(Enemy(x, y, self.wave))
        self.enemies_spawned += 1
    
    def spawn_powerup(self, x, y):
        power_type = random.choice(["health", "mana", "shield"])
        self.powerups.append(PowerUp(x, y, power_type))
    
    def check_spell_collisions(self):
        for spell in self.spells[:]:
            for enemy in self.enemies[:]:
                dx = spell.x - enemy.x
                dy = spell.y - enemy.y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance < spell.radius + enemy.radius:
                    if spell.spell_type == SpellType.HEAL:
                        self.player.heal(20)
                    else:
                        if enemy.take_damage(spell.damage):
                            self.enemies.remove(enemy)
                            self.score += 100
                            self.spawn_powerup(enemy.x, enemy.y)
                    
                    if spell in self.spells:
                        self.spells.remove(spell)
                    break
    
    def check_powerup_collisions(self):
        for powerup in self.powerups[:]:
            if not powerup.is_active():
                self.powerups.remove(powerup)
                continue
            
            dx = self.player.x - powerup.x
            dy = self.player.y - powerup.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance < self.player.radius + powerup.radius:
                if powerup.power_type == "health":
                    self.player.heal(30)
                elif powerup.power_type == "mana":
                    self.player.add_mana(50)
                elif powerup.power_type == "shield":
                    self.player.add_shield(20)
                
                self.powerups.remove(powerup)
                self.score += 50
    
    def check_enemy_collisions(self):
        for enemy in self.enemies:
            dx = self.player.x - enemy.x
            dy = self.player.y - enemy.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance < self.player.radius + enemy.radius:
                self.player.take_damage(enemy.damage)
    
    def update(self):
        if self.game_over:
            return
        
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.mouse_pos = pygame.mouse.get_pos()
        
        # Spawn enemies
        self.spawn_timer += 1
        if self.spawn_timer > 60 and self.enemies_spawned < self.enemies_per_wave:
            self.spawn_enemy()
            self.spawn_timer = 0
        
        # Check for wave completion
        if self.enemies_spawned >= self.enemies_per_wave and len(self.enemies) == 0:
            self.wave += 1
            self.enemies_spawned = 0
            self.enemies_per_wave += 2
        
        # Update entities
        for enemy in self.enemies:
            enemy.update(self.player.x, self.player.y)
        
        for spell in self.spells[:]:
            spell.update()
            if not spell.active:
                self.spells.remove(spell)
        
        for powerup in self.powerups:
            powerup.update()
        
        # Collision detection
        self.check_spell_collisions()
        self.check_powerup_collisions()
        self.check_enemy_collisions()
        
        # Check game over
        if self.player.health <= 0:
            self.game_over = True
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw game entities
        self.player.draw(self.screen)
        
        for enemy in self.enemies:
            enemy.draw(self.screen)
        
        for spell in self.spells:
            spell.draw(self.screen)
        
        for powerup in self.powerups:
            if powerup.is_active():
                powerup.draw(self.screen)
        
        # Draw UI
        self.draw_ui()
        
        if self.game_over:
            self.draw_game_over()
        
        pygame.display.flip()
    
    def draw_ui(self):
        # Wave info
        wave_text = self.font.render(f"Wave: {self.wave}", True, WHITE)
        self.screen.blit(wave_text, (20, 20))
        
        # Score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (20, 60))
        
        # Health
        health_text = self.small_font.render(f"Health: {int(self.player.health)}/{int(self.player.max_health)}", True, GREEN)
        self.screen.blit(health_text, (20, SCREEN_HEIGHT - 100))
        
        # Mana
        mana_text = self.small_font.render(f"Mana: {int(self.player.mana)}/{int(self.player.max_mana)}", True, BLUE)
        self.screen.blit(mana_text, (20, SCREEN_HEIGHT - 70))
        
        # Shield
        if self.player.shield > 0:
            shield_text = self.small_font.render(f"Shield: {int(self.player.shield)}", True, PURPLE)
            self.screen.blit(shield_text, (20, SCREEN_HEIGHT - 40))
        
        # Spell info
        spells_info = [
            f"[SPACE] Fireball (Cost: 30) CD: {self.player.spell_cooldowns[SpellType.FIREBALL]}",
            f"[E] Frostbolt (Cost: 20) CD: {self.player.spell_cooldowns[SpellType.FROSTBOLT]}",
            f"[R] Lightning (Cost: 40) CD: {self.player.spell_cooldowns[SpellType.LIGHTNING]}",
            f"[Q] Heal (Cost: 25) CD: {self.player.spell_cooldowns[SpellType.HEAL]}"
        ]
        
        for i, spell_info in enumerate(spells_info):
            text = self.small_font.render(spell_info, True, YELLOW)
            self.screen.blit(text, (SCREEN_WIDTH - 350, 20 + i * 30))
    
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = pygame.font.Font(None, 72).render("GAME OVER", True, RED)
        final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        wave_text = self.font.render(f"Waves Survived: {self.wave}", True, WHITE)
        restart_text = self.small_font.render("Press ESC to quit or R to restart", True, YELLOW)
        
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
        self.screen.blit(wave_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 120))
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                
                if event.key == pygame.K_r and self.game_over:
                    self.__init__()
                
                # Spell casting
                if not self.game_over:
                    if event.key == pygame.K_SPACE:
                        spell = self.player.cast_spell(SpellType.FIREBALL, self.mouse_pos[0], self.mouse_pos[1])
                        if spell:
                            self.spells.append(spell)
                    elif event.key == pygame.K_e:
                        spell = self.player.cast_spell(SpellType.FROSTBOLT, self.mouse_pos[0], self.mouse_pos[1])
                        if spell:
                            self.spells.append(spell)
                    elif event.key == pygame.K_r:
                        spell = self.player.cast_spell(SpellType.LIGHTNING, self.mouse_pos[0], self.mouse_pos[1])
                        if spell:
                            self.spells.append(spell)
                    elif event.key == pygame.K_q:
                        spell = self.player.cast_spell(SpellType.HEAL, self.player.x, self.player.y)
                        if spell:
                            self.spells.append(spell)
        
        return True
    
    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
