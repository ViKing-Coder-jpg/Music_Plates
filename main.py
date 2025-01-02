#Created by Pranay, Vinayak , Shaunak and Kunal
#Import:
import pygame #Pygame Module is used to create python based games with various functions
from pygame import mixer #mixer attribute is used to play musics and sound effects during python game
import time # time module is used to get a track on time during python program
import random # Random Module is used to get random choices and number during python program
from mutagen.mp3 import MP3 # MP3 attribute of Mutagen module is used to access information related to mp3 file selected in python program


pygame.init()
# Create Screen:
screen = pygame.display.set_mode((800, 750))
pygame.display.set_caption("Music Plate")  #Title
clock = pygame.time.Clock()

#IMAGES
back_ground = pygame.image.load('bgn.jpg')  #Background
icon = pygame.image.load('music.png')  #Icon
arrow = pygame.image.load('arrow-up.png')
pygame.display.set_icon(icon)

# Sounds and Music:
music = ['Music1.mp3', 'Music2.mp3', 'Music3.mp3', 'Music4.mp3', 'Music5.mp3']

collide_sound = mixer.Sound('click.wav')
cheat_sound = mixer.Sound('Cheat Sound.wav')
cheer_sound = mixer.Sound('cheer.wav')
welcome_sound = mixer.Sound('Welcome song.wav')

# to resize images
plateA = pygame.image.load('Plate_A.png')
plateD = pygame.image.load('Plate_D.png')
plateF = pygame.image.load('Plate_F.png')
plateS = pygame.image.load('Plate_S.png')
textin = pygame.image.load('text.png')
back_arrow = pygame.image.load('back.png')
play_button = pygame.image.load('play  .png')
enter_button = pygame.image.load('enter.png')
keyboard_img = pygame.image.load('keyboard.jpg')
'''stats = pygame.image.load('stats.png')'''

DEFAULT_IMAGE_SIZE = (100, 150)
imageA = pygame.transform.scale(plateA, DEFAULT_IMAGE_SIZE)
imageD = pygame.transform.scale(plateD, DEFAULT_IMAGE_SIZE)
imageF = pygame.transform.scale(plateF, DEFAULT_IMAGE_SIZE)
imageS = pygame.transform.scale(plateS, DEFAULT_IMAGE_SIZE)
enter_button = pygame.transform.scale(enter_button, (40, 40))

#rects
arrow_rect = arrow.get_rect(bottomright=(200, 600))
text_input_box = textin.get_rect(bottomright=(-200, 300))
plate1_rect = imageA.get_rect(bottomright=(200, -150))
plate2_rect = imageS.get_rect(bottomright=(400, -200))
plate3_rect = imageD.get_rect(bottomright=(600, -250))
plate4_rect = imageF.get_rect(bottomright=(800, -300))
back_rect = back_arrow.get_rect(bottomright=(400, 700))
play_rect = play_button.get_rect(bottomright=(400, 700))
enter_rect = enter_button.get_rect(topleft=(756, 82))
'''stats_rect = stats.get_rect(bottomright=(800,750))'''

#Game Loop Conditions


Running = True
player_name_success = False
main_screen = False
score_screen = False
cheat_screen = False
start_screen = True
stat_screen=False
alpha_type = 0
score = 0
a = 1
b = 1
c = 1
d = 1
sa = False
time_record = []
run_once = 1
end_once = 1
start_once = 1
player_name = ''
player_info = {}
player_no = 1

# Main Loop
while Running:
    #Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Keyboard Input
        if event.type == pygame.KEYDOWN:
            if start_screen:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    player_name += player_name
                    player_name = ''
                    player_name_success = True
                    player_info[player_no] = [player_name, score]
                    player_no += 1
                    if len(player_name) < 1:
                        player_name_success = False

                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
            if main_screen:
                if event.key == pygame.K_a or event.key == pygame.K_j:
                    arrow_rect.x = 75
                    alpha_type += 1
                if event.key == pygame.K_s or event.key == pygame.K_k:
                    arrow_rect.x = 275
                    alpha_type += 1
                if event.key == pygame.K_d or event.key == pygame.K_l:
                    arrow_rect.x = 475
                    alpha_type += 1
                if event.key == pygame.K_f or event.key == pygame.K_SEMICOLON:
                    arrow_rect.x = 675
                    alpha_type += 1
        #Mouse Input
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            '''if stats_rect.collidepoint(mouse_pos):
              stat_screen=True
              score_screen=False'''
            if back_rect.collidepoint(mouse_pos):
                score_screen = False
                cheat_screen = False
                start_screen = True
                run_once = 1
                a, b, c, d = 1, 1, 1, 1
                score = 0
                end_once = 1
            if play_rect.collidepoint(mouse_pos):
                start_screen = False
                main_screen = True 
            if enter_rect.collidepoint(mouse_pos):
                player_name += player_name
                f=open('names.txt','a')
                f.write(player_name+'  ')
                f.close()
                player_name = ''
                player_name_success = True
                player_info[player_no] = [player_name, score]
                player_no += 1
                if len(player_name) < 1:
                    player_name_success = False
    #Game Loop Types

    #Start Screen
    if Running:
        if start_screen:
            screen.blit(back_ground, (0, 0))
            if start_once == 1:
                cheer_sound.stop()
                cheat_sound.stop()
                welcome_sound.play(-1)
                start_once += 1
            titlefont = pygame.font.SysFont('Ubantu', 40)
            myfont = pygame.font.SysFont('algerian', 40)
            typefont = pygame.font.SysFont('Redressed', 30)
            infofont = pygame.font.SysFont('Ubantu', 24)
            title = titlefont.render('MUSIC PLATES', False, (32, 230, 193))
            screen.blit(title, (300, 10))

            text_input_box = textin.get_rect(bottomright=(752, 128))
            screen.blit(textin, text_input_box)
            text_name = myfont.render('ENTER YOUR NAME :', False,
                                      (72, 27, 222))
            screen.blit(text_name, (20, 75))

            text_rect = pygame.Rect(416, 83, 350, 55)
            text_input = typefont.render(player_name, False, (0, 0, 0))
            screen.blit(text_input, text_rect)

            
            game_des1 = infofont.render('This game is a unique game which teaches the player how to type with home row keys.',False,(191, 0, 77))
            game_des2 = infofont.render('The game is played such that all the movement of player are controlled by ASDF or ',False,(191, 0, 77))
            game_des3 = infofont.render(' JKL: in the keyboard.If the player hits the plate he gets a point but misses ',False,(191, 0, 77))
            game_des4 = infofont.render('it then looses one.',False,(191, 0, 77))
            screen.blit(game_des1,(100, 200))
            screen.blit(game_des2,(100, 220))
            screen.blit(game_des3,(100, 240))
            screen.blit(game_des4,(100, 260))
            screen.blit(play_button, play_rect)
            screen.blit(enter_button, enter_rect)
            screen.blit(keyboard_img,(200,350))
            if player_name_success:
                text_success = myfont.render(
                    'Name was submitted successfully ', False, (252, 115, 3))
                screen.blit(text_success, (400, 90))
                time.sleep(2)
                player_name_success = False

        #Main Screen
    if main_screen:
        #Music and Time Management
        if run_once == 1:
            start_time = time.time()
            rand_music = random.choice(music)
            music_select = MP3(rand_music)
            music_len = music_select.info.length
            mixer.music.load(rand_music)
            mixer.music.play()  
            run_once += 1
        welcome_sound.stop()

        current_time = time.time()

        #speed of plates that are falling from top of the screen
        plate1_rect.y += a
        plate2_rect.y += b
        plate3_rect.y += c
        plate4_rect.y += d

        #checking plate if collided with arrow
        if arrow_rect.colliderect(plate1_rect):
            a += 0.5
            collide_sound.play()
            score += 1
            plate1_rect.y = -150
        if arrow_rect.colliderect(plate2_rect):
            collide_sound.play()
            score += 1
            b += 0.5
            plate2_rect.y = -200
        if arrow_rect.colliderect(plate3_rect):
            collide_sound.play()
            score += 1
            c += 0.5
            plate3_rect.y = -250
        if arrow_rect.colliderect(plate4_rect):
            score += 1
            collide_sound.play()
            d += 0.5
            plate4_rect.y = -300

        #plate going down the screen to put that in a loop
        if plate1_rect.y > 800:
            plate1_rect.y = -150
            score += -1
        if plate2_rect.y > 800:
            plate2_rect.y = -150 + 50
            score += -1
        if plate3_rect.y > 800:
            plate3_rect.y = -150 + 100
            score += -1
        if plate4_rect.y > 800:
            plate4_rect.y = -150 + 150
            score += -1

        screen.blit(back_ground, (0, 0))
        screen.blit(arrow, arrow_rect)
        screen.blit(imageA, plate1_rect)
        screen.blit(imageS, plate2_rect)
        screen.blit(imageD, plate3_rect)
        screen.blit(imageF, plate4_rect)

        myfont = pygame.font.SysFont('algerian', 30)
        textsurface = myfont.render('SCORE = ' + str(score), False,
                                    (255, 255, 255))
        screen.blit(textsurface, (600, 10))
        #score screen conditions
        if (current_time - start_time) >=float(music_len):
            score_screen = True
            main_screen = False
        #Cheat Screen Conditon
        if (current_time - start_time) >= 50.0 and alpha_type == 0:
            cheat_screen = True

    #Cheat Screen
    if cheat_screen:
        main_screen = False
        if end_once == 1:
            mixer.music.pause()
            cheat_sound.play(-1)
            end_once += 1
        mixer.music.pause()
        screen.blit(back_ground, (0, 0))

        myfont = pygame.font.SysFont('algerian', 50)
        text_title = myfont.render('MUSIC PLATES', False, (32, 230, 193))
        text_cheat = myfont.render('YOU ARE A CHEATER', False, (72, 27, 222))

        screen.blit(text_title, (300, 10))
        screen.blit(text_cheat, (300, 300))
        screen.blit(back_arrow, back_rect)
        player_info[player_no ][1] = 0

    #score screen
    if score_screen:
        if end_once == 1:
            cheer_sound.play(-1)
            end_once += 1
        mixer.music.pause()
        screen.blit(back_ground, (0, 0))
        myfont = pygame.font.SysFont('algerian', 50)
        text_title = myfont.render('MUSIC PLATES', False, (32, 230, 193))
        textscore = myfont.render('Your Score is :  ' + str(score), False,
                                  (72, 27, 222))
        textalpha = myfont.render('You Typed ' + str(alpha_type) + 'Letters',
                                  False, (72, 27, 222))
        text_accuracy = myfont.render(
            'You Typing accuracy is ' + str((alpha_type / 189.0) * 100) + '%',
            False, (72, 27, 222))

        screen.blit(text_title, (300, 10))
        screen.blit(textscore, (50, 200))
        screen.blit(textalpha, (50, 300))
        screen.blit(text_accuracy, (50, 400))
        screen.blit(back_arrow, back_rect)
        '''screen.blit(stats, stats_rect)'''
        player_info[player_no][1] = score

    ''' if stat_screen:
      hk=len(player_info)
      
      myfont = pygame.font.SysFont('algerian', 50)
      text_title = myfont.render('MUSIC PLATES', False, (32, 230, 193))
      textscore = myfont.render('PLAYER 1 '+player_info[1], False,(72, 27, 222))'''

    pygame.display.update()
    clock.tick(100)
