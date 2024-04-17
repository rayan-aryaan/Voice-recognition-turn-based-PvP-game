import pygame
import random
import os

bridge_images = ["sky bridge.png", "castle bridge.png", "forest bridge.png", "bamboo bridge.png"]

# Randomly select one of the bridge images
selected_bridge = random.choice(bridge_images)

# Load the selected bridge image
background_arena = pygame.image.load(os.path.join("arenas", selected_bridge))

king_attack = [pygame.image.load(f"king/attack/image_0-{i}.png").convert_alpha() for i in range(0, 12)]
king_death = [pygame.image.load(f"king/death/image_0-{i}.png").convert_alpha() for i in range(0, 6)]
king_idle = [pygame.image.load(f"king/idle/image_0-{i}.png").convert_alpha() for i in range(0, 8)]
king_take_hit = [pygame.image.load(f"king/take hit/image_0-{i}.png").convert_alpha() for i in range(0, 4)]

shogun_attack = [pygame.image.load(f"shogun/attack/image_0-{i}.png").convert_alpha() for i in range(0, 12)]
shogun_death = [pygame.image.load(f"shogun/death/image_0-{i}.png").convert_alpha() for i in range(0, 6)]
shogun_idle = [pygame.image.load(f"shogun/idle/image_0-{i}.png").convert_alpha() for i in range(0, 8)]
shogun_take_hit = [pygame.image.load(f"shogun/take hit/image_0-{i}.png").convert_alpha() for i in range(0, 4)]

current_frame_king = 0
current_frame_shogun = 0

king_is_attacking = False
shogun_is_attacking = False
king_attack_frames = 0
shogun_takehit_frame = 0
shogun_attack_frames = 0
king_takehit_frame = 0


def animate_characters(screen):
    global king_is_attacking, shogun_is_attacking, king_attack_frames, shogun_takehit_frame, shogun_attack_frames, king_takehit_frame, current_frame_king, current_frame_shogun

    if king_is_attacking:
        king_is_attacking, king_attack_frames, shogun_takehit_frame, current_frame_king, current_frame_shogun = king_attack_animation(
            screen, king_attack_frames, shogun_takehit_frame, current_frame_king, current_frame_shogun)

    elif shogun_is_attacking:
        shogun_is_attacking, shogun_attack_frames, king_takehit_frame, current_frame_king, current_frame_shogun = shogun_attack_animation(
            screen, shogun_attack_frames, king_takehit_frame, current_frame_king, current_frame_shogun)

    else:
        screen.blit(king_idle[current_frame_king], (0, 70))
        current_frame_king = (current_frame_king + 1) % len(king_idle)
        screen.blit(shogun_idle[current_frame_shogun], (400, 50))
        current_frame_shogun = (current_frame_shogun + 1) % len(shogun_idle)


def king_attack_animation(screen, king_attack_frames, shogun_takehit_frame, current_frame_king, current_frame_shogun):
    if king_attack_frames < len(king_attack):
        screen.blit(king_attack[king_attack_frames], (0, 70))
        king_attack_frames += 1
        if king_attack_frames % 3 == 0:
            screen.blit(shogun_take_hit[shogun_takehit_frame], (400, 50))
            shogun_takehit_frame += 1
            if shogun_takehit_frame == len(shogun_take_hit):
                shogun_takehit_frame = 2
        if king_attack_frames == len(king_attack):
            return False, 0, 0, 0, 0  # Attack animation finished, reset variables
    else:
        screen.blit(king_idle[current_frame_king], (0, 70))
        current_frame_king = (current_frame_king + 1) % len(king_idle)
        screen.blit(shogun_idle[current_frame_shogun], (400, 50))
        current_frame_shogun = (current_frame_shogun + 1) % len(shogun_idle)
    return True, king_attack_frames, shogun_takehit_frame, current_frame_king, current_frame_shogun


def shogun_attack_animation(screen, shogun_attack_frames, king_takehit_frame, current_frame_king, current_frame_shogun):
    if shogun_attack_frames < len(shogun_attack):
        screen.blit(shogun_attack[shogun_attack_frames], (400, 50))
        shogun_attack_frames += 1
        if shogun_attack_frames % 3 == 0:
            screen.blit(king_take_hit[king_takehit_frame], (0, 70))
            king_takehit_frame += 1
            if king_takehit_frame == len(king_take_hit):
                king_takehit_frame = 0
        if shogun_attack_frames == len(shogun_attack):
            return False, 0, 0, 0, 0  # Attack animation finished, reset variables
    else:
        screen.blit(king_idle[current_frame_king], (0, 70))
        current_frame_king = (current_frame_king + 1) % len(king_idle)
        screen.blit(shogun_idle[current_frame_shogun], (400, 50))
        current_frame_shogun = (current_frame_shogun + 1) % len(shogun_idle)
    return True, shogun_attack_frames, king_takehit_frame, current_frame_king, current_frame_shogun
