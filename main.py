import os
import csv
import random
import sys
from time import sleep
from tkinter import *

class Player:
    def __init__(self, name, score, lives):
        self.name = name
        self.score = score
        self.lives = lives
    
    def increase_score(self, points):
        self.score += points
    
    def decrease_lives(self):
        self.lives -= 1

#create Player object in class Game
class Game:
    def __init__(self):
        name = self.get_name()
        self.player = Player(name, 0, 3)
        self.quiz = Quiz()
    
    def get_name(self):
        name = input("Enter Name: ")
        print("\n")
        return name
    
    def start_game(self):
        os.system("cls")
        print(f"Welcome to the game, {self.player.name}!")
        print(f"You have {self.player.lives} lives, good luck!")
        input("Press Enter To Continue...")

    def pick_diff(self):
        os.system("cls")
        print("PLEASE SELECT DIFFICULTY")
        print("[1] Chill\n[2] Moderate\n[3] Difficult")
        diff = input("You Entered: ")
        if diff == "1":
            self.quiz.easy_diff()
        elif diff == "2":
            self.quiz.mid_diff()
        elif diff == "3":
            self.quiz.hard_diff()
        else:
            print("Only enter 1-3!")
            sleep(1)
            self.pick_diff()

    def game_over(self):
        sleep(2)
        os.system("cls")
        print(f"Game Over! You Scored {self.player.score}")
        #Record Name and Score in leaderboard
        filename = 'Leader_Board.csv'
        if os.path.isfile(filename):
            #open existing file 
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                players = []
                for player in reader:
                    players.append([player[0],int(player[1])])
            players.append([self.player.name, self.player.score])

            #sort highest to lowest
            sorted_players = sorted(players, key=lambda x: x[1], reverse=True)

            #Rewrite data
            with open(filename, 'w', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name, Score"])
                writer.writerows(players)

        else:
            # Create file
            with open(filename, 'w', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name, Score"])
                writer.writerows([self.player.name, self.player.score])
        
        game.try_again()
        
    def try_again(self):
        while True:
            os.system("cls")
            is_try = input("Do you want to try again? [Y/N]\n")
            if is_try == "Y" or is_try == "y":
                self.player.lives = 3
                self.player.score = 0
                self.pick_diff()
                
            elif is_try == "N" or is_try == "n":
                self.player.lives = 3
                self.player.score = 0
                break

            else:
                print("Invalid Input. Select [Y/N]")


    def display_lb(self):
        os.system("cls")
        with open('Leader_Board.csv', 'r') as file:
            reader = csv.reader(file)
            items = list(reader)
        for item in items:
            return item

class Quiz():
    def easy_diff(self):
        os.system("cls")
        file = open('Easy_Questions.csv')
        ez_diff = csv.reader(file)
        #go to items
        next(ez_diff)
        #get all items
        items = []
        for item in ez_diff:
            items.append(item)
        file.close()

        while True:
            os.system("cls")
            n = random.randint(1,50)
            answer = input(f"Find x: {items[n][0]} \n")
            if answer == items[n][1]:
                game.player.increase_score(1)
                print("Correct! plus 1 point...")
            else:
                game.player.decrease_lives()
                print("Incorrect! You have lost a life...")
                print(f"{game.player.lives} left!")
                if game.player.lives == 0:
                    game.game_over()
                    break
            sleep(2)
    
    def mid_diff(self):
        os.system("cls")
        file = open('Medium_Questions.csv')
        mid_diff = csv.reader(file)
        #go to items
        next(mid_diff)
        #get all items
        items = []
        for item in mid_diff:
            items.append(item)
        file.close()

        while True:
            os.system("cls")
            n = random.randint(1,40)
            answer = input(f"Find x: {items[n][0]} \n")
            if answer == items[n][1]:
                game.player.increase_score(2)
                print("Correct! plus 1 point...")
            else:
                game.player.decrease_lives()
                print("Incorrect! You have lost a life...")
                print(f"{game.player.lives} left!")
                if game.player.lives == 0:
                    game.game_over()
                    break
            sleep(2)

    def hard_diff(self):
        os.system("cls")
        file = open('Hard_Questions.csv')
        hard_diff = csv.reader(file)
        #go to items
        next(hard_diff)
        #get all items
        items = []
        for item in hard_diff:
            items.append(item)
        file.close()

        while True:
            os.system("cls")
            n = random.randint(1,20)
            answer = input(f"Find x: {items[n][0]} \n")
            if answer == items[n][1]:
                game.player.increase_score(2)
                print("Correct! plus 1 point...")
            else:
                game.player.decrease_lives()
                print("Incorrect! You have lost a life...")
                print(f"{game.player.lives} left!")
                if game.player.lives == 0:
                    game.game_over()
                    break
            sleep(2)

os.system("cls")


# create a new game
game = Game()

#Menu
while True:
    os.system("cls")
    print("Welcome to Algebra Trainer")
    print("[1] Start")
    print("[2] Check Leaderboard")
    print("[3] Exit")
    select = input("You Entered: ")
    if select == "1":    
        game.start_game()
        game.pick_diff()
    elif select == "2":
        game.display_lb()
    elif select == "3":
        sys.exit()
    else:
        print("Invalid Input!")
        sleep(1)