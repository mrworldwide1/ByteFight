# Name: ByteFight
# Description: ICS4U SDLC summative project, a fun educational computer science game inspired by Math prodigy.
# Date: November 28, 2023
# By: Omar S, Lucas L, Harris V
# some features like soundtrack dont work on replit - check the github
# Name: ByteFight
# Description: ICS4U SDLC summative project, a game inspired by Math prodigy.
# Date: November 28, 2023
# By: Omar S, Lucas L, Harris V
# Some features like the soundtrack may not work on Replit - check the GitHub

import pygame
import sys
import random
from button import Button
from cs_questions import computer_science_questions

class Game:
    def __init__(self): # Screen setup
        pygame.init()
        self.screen_width = 640
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.game_name = "ByteFight"
        pygame.display.set_caption(self.game_name)
        program_icon = pygame.image.load('battle_arena.png').convert_alpha()
        pygame.display.set_icon(program_icon)
        self.clock = pygame.time.Clock()

        # Fonts setup
        self.title_font_size = 72
        self.title_font = pygame.font.Font('Retro Gaming.ttf', self.title_font_size)
        self.button_font_size = 36
        self.button_font = pygame.font.Font('Retro Gaming.ttf', self.button_font_size)
        self.tiny_font_size = 18
        self.tiny_font = pygame.font.Font('Retro Gaming.ttf', self.tiny_font_size)
        self.character_font_size = 14
        self.character_font = pygame.font.Font('Retro Gaming.ttf', self.character_font_size)

        # Health bar colours
        self.health_bar_enemy = ("purple")
        self.health_bar_player = (0, 255, 0)

        # Music setup
        self.battle_soundtracks = [
             "xDeviruchi - Decisive Battle.wav",
             "xDeviruchi - And The Journey Begins .wav",
             "xDeviruchi - The Icy Cave .wav",
             "xDeviruchi - Exploring The Unknown.wav"
         ]
        
        # Enemy/player names
        self.player_name = "Wizard"
        self.enemy_name = "Earth Creature"

        # Retrieve save data file with wins/losses, put each line in list
        self.save_file = open("save.txt", "r+")
        self.lines = self.save_file.readlines()
        self.wins = self.lines[1]
        self.losses = self.lines[4]
        self.save_file.close()

        # Tell player to keep console open
        print("Please don't close this console, you'll need it to answer the questions!")

    def display_text(self, text, font, x, y, colour): # Displays text onto the screen surface
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def display_background(self, image): # Function that fits the background image onto the entire screen
        bg = pygame.image.load(image).convert_alpha()
        bg = pygame.transform.scale(bg, (self.screen_width, self.screen_height))
        self.screen.blit(bg, (0, 0))

    def play_soundtrack(self, file): # Custom function to play soundtracks 
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1, 0, 4000)

    def stop_soundtrack(self): # Custom function that fades out whatever is currently playing
        pygame.mixer.music.fadeout(1000) 

    def title_screen(self):
        # Stop current song, play music
        self.stop_soundtrack()
        self.play_soundtrack("xDeviruchi - Title Theme .wav")
        
        while True:
            # Show title, background, score
            self.display_background('title_screen_bg.jpg')
            self.display_text(self.game_name, self.title_font, self.screen_width / 2, self.screen_height / 6, 'white')
            self.display_text("By: Lucas L, Omar S, Harris V - for ICS4U", self.tiny_font, self.screen_width / 2, self.screen_height / 1.1, 'white') 
            self.display_text(f"Wins: {self.wins}", self.tiny_font, self.screen_width/2, self.screen_height/1.25, 'white')
            self.display_text(f"Losses: {self.losses}", self.tiny_font, self.screen_width/2, self.screen_height/1.18, 'white')
            
            # Menu choices
            computer_science_button = Button("Play", self.button_font, self.screen_width / 14, self.screen_height / 2.5, "green", "white", 120, 50)
            quit_button = Button("Quit", self.button_font, self.screen_width / 14, self.screen_height / 1.8, "red", "white", 120, 50)
            computer_science_button.display()
            quit_button.display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Switch game state if buttons clicked 
                elif event.type == pygame.MOUSEBUTTONUP:
                    if computer_science_button.collide():
                        self.computer_science_arena()
                    elif quit_button.collide():
                        pygame.quit()
                        sys.exit()

            # Updates everything
            pygame.display.update()
            self.clock.tick(60)

    def computer_science_arena(self):
        # Sets enemy and player health points
        player_health = 100
        enemy_health = 100

        # Store previously asked questions to prevent repeats
        asked_questions = []

        # Play random soundtrack
        self.stop_soundtrack()
        self.play_soundtrack(random.choice(self.battle_soundtracks))

        while True:
            # Displays battle arena
            self.display_background('battle_arena.png')

            # Display health bars
            pygame.draw.rect(self.screen, self.health_bar_player, (20, 20, player_health * 2.2, 30))
            pygame.draw.rect(self.screen, self.health_bar_enemy, (400, 20, enemy_health * 2.2, 30))

            # Displays player and enemy names
            self.display_text(self.player_name, self.character_font, 50, 10, 'white')
            self.display_text(self.enemy_name, self.character_font, 465, 10, 'white')

            # Display fight and heal buttons
            fight_button = Button("Fight", self.button_font, self.screen_width / 12, self.screen_height - 100, "brown", "white", 120, 50)
            heal_button = Button("Heal", self.button_font, 3 * self.screen_width / 4.10, self.screen_height - 100, "brown", "white", 120, 50)
            fight_button.display()
            heal_button.display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    # Ask question when fight clicked
                    if fight_button.collide():

                        # Ensures same question is not asked twice
                        while True:
                            question_data = random.choice(computer_science_questions)
                            if question_data["question"] not in asked_questions:
                                asked_questions.append(question_data["question"])  
                                break

                        question = question_data["question"]
                        options = question_data["options"]
                        answer = input(f"{question} ({','.join(options)}\n Answer: ")

                        # Attack enemy if correct answer, otherwise damage player
                        if answer.upper() == question_data["answer"]:
                            enemy_health -= random.randint(10, 20)
                            print("You attacked!")
                        else:
                            damage = random.randint(10, 20)
                            player_health -= damage
                            if damage > 15:
                                print("Enemy lands crit! You missed!") 
                            else:
                                print("Enemy lands hit! You missed!")
                            
                    # Ask questions if heal clicked
                    elif heal_button.collide():
                        
                        # Ensures same question is not asked twice
                        while True:
                            question_data = random.choice(computer_science_questions)
                            if question_data["question"] not in asked_questions:
                                asked_questions.append(question_data["question"])  
                                break

                        question = question_data["question"]
                        options = question_data["options"]
                        answer = input(f"{question} ({','.join(options)}\n Answer: ")

                        # Heal player up to max health of 100 if answer correct, otherwise harm player
                        if answer.upper() == question_data["answer"]:
                            player_health += random.randint(5, 10)
                            player_health = min(100, player_health)
                            if player_health < 100:
                                print("You healed!")
                            elif player_health >= 100:
                                print("You healed and are at max health!")
                        else:
                            damage = random.randint(15, 60)
                            player_health -= damage
                            if damage > 20:
                                print("You missed!") 
                            else:
                                print("Enemy lands Hit! You missed!") 


            # Displays game over or victory screen
            if player_health <= 0:
                self.display_text("Game Over", self.title_font, self.screen_width / 2, self.screen_height / 1.5, 'red')
                pygame.display.update()
                pygame.time.sleep(2)

                # Update save returning list containing each line as an element in read/write mode
                # save_file = open("save.txt", "r+")
                # lines = save_file.readlines()
                # losses += 1
                # lines[4] = losses
                # # update specific line
                # save_file.writelines(lines)
                # save_file.close()
                
                self.stop_soundtrack()
                self.play_soundtrack("xDeviruchi - Title Theme .wav")
                return
            
            elif enemy_health <= 0:
                self.display_text("You Win!", self.title_font, self.screen_width / 2, self.screen_height / 2, 'green')
                pygame.display.update()
                pygame.time.sleep(2)

                # Update save returning list containing each line as an element in read/write mode
                # return list containing each line as an element in read/write mode
                # save_file = open("save.txt", "r+")
                # lines = save_file.readlines()
                # wins += 1
                # lines[1] = losses
                # # update specific line
                # save_file.writelines(lines)
                # save_file.close()

                self.stop_soundtrack()
                self.play_soundtrack("xDeviruchi - Title Theme .wav")
                return

            pygame.display.update()
            self.clock.tick(60)

    
# Starts game
if __name__ == "__main__":
    game_instance = Game()
    game_instance.title_screen()
