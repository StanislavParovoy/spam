import pyautogui, time, os, webbrowser
from os import system, name
def clear():
    if os.name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
screenWidth, screenHeight = pyautogui.size()
#replace all '" in files


print("!I AM NOT RESPONSIBLE FOR ANY BAN'S YOU GET!")
print('Only for discord users!')
print('Activate Annoying mode!')
print('You must have the required @everyone and @here permission to do it!')
print('annoy mode doesn"t work at the moment!')
annoying = input('Y/N ')
if annoying.upper() == 'Y':

    print('1. @everyone')
    print('2. @here')
    print('3. [discord tag]')
    who_annoy = int(input('Select option: '))
    annoy = ''
    if who_annoy == 1:
        annoy == '@everyone'
    elif who_annoy == 2:
        annoy == '@here'
    elif who_annoy == 3:
        tag = input('Discord Tag: ')
        tag1 = '@'+tag
        annoy = tag1

    while True:
        print('')
        print('')
        print('Spam bot!')
        print('')
        print('')
        time.sleep(1)
        print('1. Bee movie Script')
        time.sleep(1)
        print('2. Shrek scripts')
        time.sleep(1)
        print('3. Wiki pages!')
        time.sleep(1)
        print('4. Song Scripts')
        time.sleep(1)
        print('5. Inputted Text Repeated')
        time.sleep(1)
        print('6. Change Annoy Target')
        time.sleep(1)
        print('7. Info')
        time.sleep(1)
        print('8. Exit/leave mode')
        time.sleep(1)

        i = int(input('Select option: '))
        if i == 1:
            print('1. Bee movie Script Selected!')
            print(
                '...........................................................................................................................')
            print('')
            print('Leave this running on a Text chat like discord or skype!')
            print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
            time.sleep(1)
            print('')
            print('5 seconds before start!')
            time.sleep(5)
            f = open("Scripts/beemovie.txt", 'r')
            for word in f:
                pyautogui.press("shift" + "enter")
                pyautogui.typewrite(word)
                pyautogui.typewrite(' ')
                pyautogui.typewrite(annoy)
                time.sleep(.1)
                pyautogui.press("enter")
            print('completed!')
        elif i == 2:
            print('2. Shrek Scripts Selected!')
            print(
                '...........................................................................................................................')
            print('')
            print('1. Shrek 1')
            time.sleep(1)
            print('2. Shrek 2')
            time.sleep(1)
            print('3. Shrek 3')
            time.sleep(1)
            print('4. Shrek 4')
            time.sleep(1)
            script_choice_shrek = int(input('Select option: '))
            if script_choice_shrek == 1:
                time.sleep(1)
                print('Shrek 1 Selected!')
                time.sleep(1)
                print('Leave this running on a Text chat like discord or skype!')
                print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
                time.sleep(1)
                print('')
                print('5 seconds before start!')
                time.sleep(5)
                f = open("Scripts/Shrek/shrek_1.txt", 'r')
                for word in f:
                    pyautogui.typewrite(word)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(.1)
                    pyautogui.press("enter")
                print('Completed!')
            elif script_choice_shrek == 2:
                time.sleep(1)
                print('Shrek 2 Selected!')
                time.sleep(1)
                print('Leave this running on a Text chat like discord or skype!')
                print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
                time.sleep(1)
                print('')
                print('5 seconds before start!')
                time.sleep(5)
                f = open("Scripts/Shrek/shrek_2.txt", 'r')
                for word in f:
                    pyautogui.typewrite(word)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(.1)
                    pyautogui.press("enter")
                print('Completed!')

            elif script_choice_shrek == 3:
                time.sleep(1)
                print('Shrek 3 Selected!')
                time.sleep(1)
                print('Leave this running on a Text chat like discord or skype!')
                print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
                time.sleep(1)
                print('')
                print('5 seconds before start!')
                time.sleep(5)
                f = open("Scripts/Shrek/shrek_3.txt", 'r')
                for word in f:
                    pyautogui.typewrite(word)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(.1)
                    pyautogui.press("enter")
                print('Completed!')

            elif script_choice_shrek == 4:
                time.sleep(1)
                print('Shrek 4 Selected!')
                time.sleep(1)
                print('Shrek 4 has no public script, returning!')
            else:
                print('Invalid Choice!')
        elif i == 3:
            print('3. Wiki Pages Selected!')
            print(
                '...........................................................................................................................')
            print('')
            time.sleep(1)
            print("These Wikipedia Scripts are the Base of all of them and more will be added!")
            time.sleep(1)
            print('DM me if you want to add more. Go to info for contacts!')
            print('Or you could make a push on Github!')
            time.sleep(2)
            print("1. Wikipedia script")
            time.sleep(1)
            print("2. Cheese")
            time.sleep(1)
            wiki_selection = int(input('Select Option: '))
            if wiki_selection == 1:
                print('Cheese Selected!')
                time.sleep(1)
                print('Leave this running on a Text chat like discord or skype!')
                print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
                time.sleep(1)
                print('')
                print('5 seconds before start!')
                time.sleep(5)
                f = open("Scripts/Wiki/Wikipedia.txt", 'r', encoding="utf8")
                for word in f:
                    pyautogui.press("shift" + "enter")
                    pyautogui.typewrite(word)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(.1)
                    pyautogui.press("enter")
                print('Completed!')
        elif i == 4:
            print('4. Song scripts selected!')
            print(
                '...........................................................................................................................')
            print('')
            time.sleep(1)
            print("These Song Scripts are the Base of all of them and more will be added!")
            time.sleep(1)
            print('DM me if you want to add more. Go to info for contacts!')
            print('Or you could make a push on Github!')
            time.sleep(1)
            print('1. Rick Roll')
            time.sleep(1)
            print('2. Dat Boi Sus')
            time.sleep(1)
            print('3. Wap')
            time.sleep(1)
            print('4. Black Beatles')
            time.sleep(1)
            song_selection = int(input('Select option: '))
            if song_selection == 1:
                print('1. Rick Roll Selected')
                time.sleep(1)
                print('Starting in 5 seconds')
                time.sleep(5)
                f = open("Scripts/songs/rick_roll.txt", 'r', encoding="utf8")
                for word in f:
                    pyautogui.press("shift" + "enter")
                    pyautogui.typewrite(word)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(1)
                    pyautogui.press("enter")

                print('Completed!')
            elif song_selection == 2:
                print('2. Dat Boi Sus Selected')
                time.sleep(1)
                print('Starting in 5 seconds')
                time.sleep(5)
                f = open("Scripts/songs/hatchback.txt", 'r', encoding="utf8")
                for word in f:
                    pyautogui.press("shift" + "enter")
                    pyautogui.typewrite(word)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(1)
                    pyautogui.press("enter")

            elif song_selection == 3:
                print('3. Wap Selected')
                time.sleep(1)
                print('Starting in 5 seconds')
                time.sleep(5)
                f = open("Scripts/songs/wap.txt", 'r', encoding="utf8")
                for word in f:
                    pyautogui.press("shift" + "enter")
                    pyautogui.typewrite(word)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(1)
                    pyautogui.press("enter")

            elif song_selection == 4:
                print('4. Black Beatles Selected')
                time.sleep(1)
                print('Starting in 5 seconds')
                time.sleep(5)
                f = open("Scripts/songs/blackbeatles.txt", 'r', encoding="utf8")
                for word in f:
                    pyautogui.press("shift" + "enter")
                    pyautogui.typewrite(word)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(1)
                    pyautogui.press("enter")

            else:
                print('Invaild option!')
        elif i == 5:
            print('5. Inputted Text Repeted Selected!')
            print(
                '...........................................................................................................................')
            print('')
            time.sleep(1)
            print('Sending messages below 1.5 seconds on discord Can get you banned!')
            time.sleep(1)
            dangours_mode = input('Would you like to activate dangours mode? Y/N ')
            if dangours_mode.upper() == 'Y':
                time.sleep(1)
                repeat_times = int(input("How many messgaes: "))
                if repeat_times <= 1:
                    print('Invalid answer, It has to be a whole number!')
                time.sleep(1)
                message = input('Message: ')
                time.sleep(5)
                for _ in range(repeat_times):
                    pyautogui.press("shift" + "enter")
                    pyautogui.typewrite(message)
                    pyautogui.typewrite(' ')
                    pyautogui.typewrite(annoy)
                    time.sleep(0.1)
                    pyautogui.press("enter")
                print('Completed!')
                pyautogui.typewrite('Completed!')

            wait_before_r = int(input("Time before next Message Sent: "))
            if wait_before_r <= 1.5:
                print('I AM NOT RESPONSIBLE FOR YOU GETTING BANNED!')
            time.sleep(1)
            repeat_times = int(input("How many messgaes: "))
            if repeat_times <= 1:
                print('Invalid answer, It has to be a whole number!')
            time.sleep(1)
            message = input('Message: ')
            time.sleep(5
                       )
            for _ in range(repeat_times):
                pyautogui.press("shift" + "enter")
                pyautogui.typewrite(message)
                pyautogui.typewrite(' ')
                pyautogui.typewrite(annoy)
                time.sleep(wait_before_r)
                pyautogui.press("enter")
            print('Completed!')
            pyautogui.typewrite('Completed!')
        elif i == 6:
            print('6. Change Annoy Target Selected!')
            print('...........................................................................................................................')
            print('')
            print('1. @everyone')
            print('2. @here')
            print('3. [discord tag]')
            who_annoy = int(input('Select option: '))
            annoy = ''
            if who_annoy == 1:
                annoy == '@everyone'
            elif who_annoy == 2:
                annoy == '@here'
            elif who_annoy == 3:
                tag = input('Discord Tag: ')
                tag1 = '@' + tag
                annoy = tag1

        elif i == 7:
            print('6. Info Selected!')
            print(
                '...........................................................................................................................')
            time.sleep(1)
            print('Built by sɹǝƃƃod#5183')
            time.sleep(1)
            print('Copyright 2020 sɹǝƃƃod#5183/poggers1337')
            print(
                'Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:')
            print(
                'The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.')
            print(
                'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.')
            time.sleep(5)
            discord_server = input('Would you like to join my discord server for more software? Y/N ')
            if discord_server.upper() == 'Y':
                webbrowser.open_new(url='https://discord.gg/FuBjvyR', new=1)
            support = input('Would you like to support me, This is open source and I dont get anything off it! Y/N ')
            if support.upper() == 'Y':
                webbrowser.open(url='paypal.me/james1collum', new=1)
        elif i == 8:
            print('1. Change to normal')
            time.sleep(1)
            print('2. Exit')
            exit_change_mode = int(input('Select option: '))
            if exit_change_mode == 1:
                break
            elif exit_change_mode == 2:
                print('Exitting')
                time.sleep(1)
                exit()
            else:
                print('Invalid answer!')
while True:
    clear()
    print('')
    print('')
    print('Spam bot!')
    print('')
    print('')
    time.sleep(1)
    print('1. Bee movie Script')
    time.sleep(1)
    print('2. Shrek scripts')
    time.sleep(1)
    print('3. Wiki pages!')
    time.sleep(1)
    print('4. Song Scripts')
    time.sleep(1)
    print('5. Inputted Text Repeated')
    time.sleep(1)
    print('6. Info')
    time.sleep(1)
    print('7. Exit')
    time.sleep(1)

    i = int(input('Select option: '))
    if i == 1:
        print('1. Bee movie Script Selected!')
        print('...........................................................................................................................')
        print('')
        print('Leave this running on a Text chat like discord or skype!')
        print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
        time.sleep(1)
        print('')
        print('5 seconds before start!')
        time.sleep(5)
        f = open("Scripts/beemovie.txt", 'r')
        for word in f:
            pyautogui.press("shift"+"enter")
            pyautogui.typewrite(word)
            time.sleep(.1)
            pyautogui.press("enter")
        print('completed!')
    elif i == 2:
        print('2. Shrek Scripts Selected!')
        print(
            '...........................................................................................................................')
        print('')
        print('1. Shrek 1')
        time.sleep(1)
        print('2. Shrek 2')
        time.sleep(1)
        print('3. Shrek 3')
        time.sleep(1)
        print('4. Shrek 4')
        time.sleep(1)
        script_choice_shrek = int(input('Select option: '))
        if script_choice_shrek == 1:
            time.sleep(1)
            print('Shrek 1 Selected!')
            time.sleep(1)
            print('Leave this running on a Text chat like discord or skype!')
            print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
            time.sleep(1)
            print('')
            print('5 seconds before start!')
            time.sleep(5)
            f = open("Scripts/Shrek/shrek_1.txt", 'r')
            for word in f:
                pyautogui.typewrite(word)
                time.sleep(.1)
                pyautogui.press("enter")
            print('Completed!')
        elif script_choice_shrek == 2:
            time.sleep(1)
            print('Shrek 2 Selected!')
            time.sleep(1)
            print('Leave this running on a Text chat like discord or skype!')
            print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
            time.sleep(1)
            print('')
            print('5 seconds before start!')
            time.sleep(5)
            f = open("Scripts/Shrek/shrek_2.txt", 'r')
            for word in f:
                pyautogui.typewrite(word)
                time.sleep(.1)
                pyautogui.press("enter")
            print('Completed!')

        elif script_choice_shrek == 3:
            time.sleep(1)
            print('Shrek 3 Selected!')
            time.sleep(1)
            print('Leave this running on a Text chat like discord or skype!')
            print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
            time.sleep(1)
            print('')
            print('5 seconds before start!')
            time.sleep(5)
            f = open("Scripts/Shrek/shrek_3.txt", 'r')
            for word in f:
                pyautogui.typewrite(word)
                time.sleep(.1)
                pyautogui.press("enter")
            print('Completed!')

        elif script_choice_shrek == 4:
            time.sleep(1)
            print('Shrek 4 Selected!')
            time.sleep(1)
            print('Shrek 4 has no public script, returning!')
        else:
            print('Invalid Choice!')
    elif i == 3:
        print('3. Wiki Pages Selected!')
        print(
            '...........................................................................................................................')
        print('')
        time.sleep(1)
        print("These Wikipedia Scripts are the Base of all of them and more will be added!")
        time.sleep(1)
        print('DM me if you want to add more. Go to info for contacts!')
        print('Or you could make a push on Github!')
        time.sleep(2)
        print("1. Wikipedia script")
        time.sleep(1)
        print("2. Cheese")
        time.sleep(1)
        wiki_selection = int(input('Select Option: '))
        if wiki_selection == 1:
            print('Cheese Selected!')
            time.sleep(1)
            print('Leave this running on a Text chat like discord or skype!')
            print('You must have the the flashing | otherwise it will put the text in where it has been selected!')
            time.sleep(1)
            print('')
            print('5 seconds before start!')
            time.sleep(5)
            f = open("Scripts/Wiki/Wikipedia.txt", 'r', encoding="utf8")
            for word in f:
                pyautogui.press("shift"+"enter")
                pyautogui.typewrite(word)
                time.sleep(.1)
                pyautogui.press("enter")
            print('Completed!')
    elif i == 4:
        print('4. Song scripts selected!')
        print(
            '...........................................................................................................................')
        print('')
        time.sleep(1)
        print("These Song Scripts are the Base of all of them and more will be added!")
        time.sleep(1)
        print('DM me if you want to add more. Go to info for contacts!')
        print('Or you could make a push on Github!')
        time.sleep(1)
        print('1. Rick Roll')
        time.sleep(1)
        print('2. Dat Boi Sus')
        time.sleep(1)
        print('3. Wap')
        time.sleep(1)
        print('4. Black Beatles')
        time.sleep(1)
        song_selection = int(input('Select option: '))
        if song_selection == 1:
            print('1. Rick Roll Selected')
            time.sleep(1)
            print('Starting in 5 seconds')
            time.sleep(5)
            f = open("Scripts/songs/rick_roll.txt", 'r', encoding="utf8")
            for word in f:
                pyautogui.press("shift" + "enter")
                pyautogui.typewrite(word)
                time.sleep(1)
                pyautogui.press("enter")

            print('Completed!')
        elif song_selection == 2:
            print('2. Dat Boi Sus Selected')
            time.sleep(1)
            print('Starting in 5 seconds')
            time.sleep(5)
            f = open("Scripts/songs/hatchback.txt", 'r', encoding="utf8")
            for word in f:
                pyautogui.press("shift" + "enter")
                pyautogui.typewrite(word)
                time.sleep(1)
                pyautogui.press("enter")

        elif song_selection == 3:
            print('3. Wap Selected')
            time.sleep(1)
            print('Starting in 5 seconds')
            time.sleep(5)
            f = open("Scripts/songs/wap.txt", 'r', encoding="utf8")
            for word in f:
                pyautogui.press("shift" + "enter")
                pyautogui.typewrite(word)
                time.sleep(1)
                pyautogui.press("enter")

        elif song_selection == 4:
            print('4. Black Beatles Selected')
            time.sleep(1)
            print('Starting in 5 seconds')
            time.sleep(5)
            f = open("Scripts/songs/blackbeatles.txt", 'r', encoding="utf8")
            for word in f:
                pyautogui.press("shift" + "enter")
                pyautogui.typewrite(word)
                time.sleep(1)
                pyautogui.press("enter")

        else:
            print('Invaild option!')
    elif i == 5:
        print('5. Inputted Text Repeted Selected!')
        print(
            '...........................................................................................................................')
        print('')
        time.sleep(1)
        print('Sending messages below 1.5 seconds on discord Can get you banned!')
        time.sleep(1)
        dangours_mode = input('Would you like to activate dangours mode? Y/N ')
        if dangours_mode.upper() == 'Y':
            time.sleep(1)
            repeat_times = int(input("How many messgaes: "))
            if repeat_times <= 1:
                print('Invalid answer, It has to be a whole number!')
            time.sleep(1)
            message = input('Message: ')
            time.sleep(5)
            for _ in range(repeat_times):
                pyautogui.press("shift" + "enter")
                pyautogui.typewrite(message)
                time.sleep(0.1)
                pyautogui.press("enter")
            print('Completed!')
            pyautogui.typewrite('Completed!')

        wait_before_r = int(input("Time before next Message Sent: "))
        if wait_before_r <= 1.5:
            print('I AM NOT RESPONSIBLE FOR YOU GETTING BANNED!')
        time.sleep(1)
        repeat_times = int(input("How many messgaes: "))
        if repeat_times <= 1:
            print('Invalid answer, It has to be a whole number!')
        time.sleep(1)
        message = input('Message: ')
        time.sleep(5
                   )
        for _ in range(repeat_times):
            pyautogui.press("shift" + "enter")
            pyautogui.typewrite(message)
            time.sleep(wait_before_r)
            pyautogui.press("enter")
        print('Completed!')
        pyautogui.typewrite('Completed!')
    elif i == 6:
        print('6. Info Selected!')
        print('...........................................................................................................................')
        time.sleep(1)
        print('Built by sɹǝƃƃod#5183')
        time.sleep(1)
        print('Copyright 2020 sɹǝƃƃod#5183/poggers1337')
        print('Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:')
        print('The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.')
        print('THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.')
        time.sleep(5)
        discord_server = input('Would you like to join my discord server for more software? Y/N ')
        if discord_server.upper() == 'Y':
            webbrowser.open_new(url= 'https://discord.gg/FuBjvyR', new = 1)
        support = input('Would you like to support me, This is open source and I dont get anything off it! Y/N ')
        if support.upper() == 'Y':
            webbrowser.open(url='paypal.me/james1collum', new = 1)
    elif i == 7:
        print('End')
        break
        exit()





