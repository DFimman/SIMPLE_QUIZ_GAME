import tkinter as tk
from tkinter import messagebox
import csv
from time import sleep
import random
import os

class MENU():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.configure(bg='#D8C49F')
        self.root.title("Algebra Trainer! by DICHOSA")

        #Title Label
        self.title = tk.Label(self.root, text="ALGEBRA TRAINER", font=('Arial bold', 16), bg='#F1DBBF', 
        borderwidth=2, relief="solid", width=30, height=2)
        self.title.pack(padx=10, pady=50)

        #Start Button
        self.button1 = tk.Button(self.root, text="START", font=('Arial', 14), width=15, 
        bg='#F1DBBF', height=2, command=self.open_start)
        self.button1.pack(padx=10, pady=(20,30))

        #LeaderBoard Button
        self.button2 = tk.Button(self.root, text="LEADERBOARD", font=('Arial', 14), width=15, 
        bg='#F1DBBF', height=2, command=self.open_leaderboard)
        self.button2.pack(padx=10, pady=(15,30))
        
        #Exit Button
        self.button3 = tk.Button(self.root, text="EXIT", font=('Arial', 14), width=15, 
        bg='#F1DBBF', height=2, command=self.on_closing)
        self.button3.pack(padx=10, pady=(15,30))


        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def open_leaderboard(self):
        self.root.destroy()
        LeaderBoard()

    def open_start(self):
        messagebox.showinfo("Difficulty","Please Select Difficulty")
        self.root.destroy()
        Start()

class LeaderBoard():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.configure(bg='#D8C49F')
        self.root.title("Leader Board")

        #Get Leaderboard csv
        self.Getlb()

        #Title Label
        self.title = tk.Label(self.root, text="LEADER BOARD", font=('Arial bold', 16), bg='#F1DBBF', 
        borderwidth=2, relief="solid", width=30, height=2)
        self.title.pack(padx=10, pady=(30,20))

        #lb frame
        self.frame = tk.LabelFrame(self.root, height=330, width=50, bg="#F1DBBF", relief="solid")
        self.frame.pack(fill="both", padx=30)

        #Name Header
        self.name_header = tk.Label(self.root, text="NAME", font=('Arial bold', 15), bg='#F1DBBF',
         width=14)
        self.name_header.place(x=45, y=120)
        #Score Header
        self.score_header = tk.Label(self.root, text="SCORE", font=('Arial bold', 15), bg='#F1DBBF',
         width=14)
        self.score_header.place(x=285, y=120)

        #Top1 Leader
        self.name_label1 = tk.Label(self.root, text=self.names[0], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.name_label1.place(x=45, y=175)
        #Top1 Score
        self.score_label1 = tk.Label(self.root, text=self.scores[0], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.score_label1.place(x=285, y=175)

        #Top2 Leader
        self.name_label2 = tk.Label(self.root, text=self.names[1], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.name_label2.place(x=45, y=230)
        #Top2 Score
        self.score_label2 = tk.Label(self.root, text=self.scores[1], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.score_label2.place(x=285, y=230)

        #Top3 Leader
        self.name_label3 = tk.Label(self.root, text=self.names[2], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.name_label3.place(x=45, y=285)
        #Top1 Score
        self.score_label3 = tk.Label(self.root, text=self.scores[2], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.score_label3.place(x=285, y=285)

        #Top4 Leader
        self.name_label4 = tk.Label(self.root, text=self.names[3], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.name_label4.place(x=45, y=340)
        #Top4 Score
        self.score_label4 = tk.Label(self.root, text=self.scores[3], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.score_label4.place(x=285, y=340)

        #Top5 Leader
        self.name_label5 = tk.Label(self.root, text=self.names[4], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.name_label5.place(x=45, y=395)
        #Top5 Score
        self.score_label5 = tk.Label(self.root, text=self.scores[4], font=('Arial', 14), bg='#F1DBBF',
         width=15)
        self.score_label5.place(x=285, y=395)

        #Return button
        self.button1 = tk.Button(self.root, text="Return", font=('Arial', 12), width=10, 
        bg='#9F8C76', command=self.Return)
        self.button1.pack(side='bottom', pady=20)


        self.root.mainloop()
    
    def Getlb(self):
        n = 0
        lb = []
        self.names = ["","","","",""]
        self.scores = ["","","","",""]

        #get lb in csv
        with open('Leader_Board.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            items = list(reader)
        for item in items:
            item[1] = int(item[1])
            lb.append(item)

        #sort lb by score
        lb.sort(key=self.score, reverse=True)

        #change base lb
        for data in lb:
            if n<=4:
                self.names[n] = data[0]
                self.scores[n] = int(data[1])
                n += 1
            elif n>4:
                self.names.append(data[0])
                self.scores.append(int(data[1]))
            else:
                break
    

    def score(self,item):
        return item[1]
        
    def Return(self):
        self.root.destroy()
        MENU()

class Start():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.configure(bg='#D8C49F')
        self.root.title("Algebra Trainer! by DICHOSA")

        #Title Label
        self.title = tk.Label(self.root, text="DIFFICULTY", font=('Arial bold', 16), bg='#F1DBBF', 
        borderwidth=2, relief="solid", width=30, height=2)
        self.title.pack(padx=10, pady=(30,30))

        #Easy Button
        self.button1 = tk.Button(self.root, text="EASY", font=('Arial', 14), width=12, 
        bg='#F1DBBF', height=2, command=self.open_easy)
        self.button1.pack(padx=10, pady=(20,30))

        #Medium Button
        self.button2 = tk.Button(self.root, text="MEDIUM", font=('Arial', 14), width=12, 
        bg='#F1DBBF', height=2, command=self.open_medium)
        self.button2.pack(padx=10, pady=(10,25))
        
        #Hard Button
        self.button3 = tk.Button(self.root, text="HARD", font=('Arial', 14), width=12, 
        bg='#F1DBBF', height=2, command=self.open_hard)
        self.button3.pack(padx=10, pady=(10,40))

        #Return button
        self.button4 = tk.Button(self.root, text="Return", font=('Arial', 12), width=8, 
        bg='#9F8C76', command=self.Return)
        self.button4.pack(pady=10)

        self.root.mainloop

    def Return(self):
        self.root.destroy()
        MENU()

    def open_easy(self):
        self.root.destroy()
        messagebox.showinfo("Goodluck!","For each Correct answer is 1 point")
        Easy()

    def open_medium(self):
        self.root.destroy()
        messagebox.showinfo("Goodluck!","For each Correct answer is 2 points")
        Medium()

    def open_hard(self):
        self.root.destroy()
        messagebox.showinfo("Goodluck!","For each Correct answer is 3 points")
        Hard()

class Easy():
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.n = 0

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.configure(bg='#D8C49F')
        self.root.title("Algebra Trainer! by DICHOSA")

        #Title Label
        self.title = tk.Label(self.root, text="EASY", font=('Arial bold', 20), bg='#D8C49F', 
        width=15, height=2)
        self.title.pack(padx=10, pady=(40,30))


        #load questions
        file = open('Easy_Questions.csv')
        ez_diff = csv.reader(file)
        #go to items
        next(ez_diff)
        #get all items
        self.items = []
        for item in ez_diff:
            self.items.append(item)
        file.close()
        
        #Get question
        n = random.randint(1,50)
        self.question = f"Find x: {self.items[n][0]}"
        self.correct_asnwer = self.items[n][1]
        
        #Question Label
        self.question_label = tk.Label(self.root, text=self.question, font=('Arial', 16), 
        bg='#F1DBBF', width=35, height=5, borderwidth=2, relief="solid",)
        self.question_label.pack(padx=20, pady=(30,30))

        #Answer Label
        self.answer_label = tk.Label(self.root, text="Answer:", font=('Arial', 12), 
        bg='#D8C49F')
        self.answer_label.pack(padx=20, pady=(30,5))

        #Answer input
        self.answerVal = tk.StringVar()
        self.text = tk.Entry(self.root, textvariable=self.answerVal)
        self.text.pack(padx=20, pady=(0,10))

        #Submit answer button
        self.submit_button = tk.Button(self.root, text="Submit", font=('Arial', 12), width=8, 
        bg='#9F8C76', command=self.check_answer)
        self.submit_button.pack(pady=10)


        self.root.mainloop

    def check_answer(self):
        
        answer = self.answerVal.get()

        #questions and answers
        if answer == self.correct_asnwer:
            self.score += 1
            messagebox.showinfo("Correct! plus 1 point...", f"Points = {self.score}")
        else:
            self.lives -= 1
            messagebox.showinfo("Incorrect! Minus 1 life!", f"{self.lives} left")
            if self.lives == 0:
                messagebox.showinfo("Game Over!", f"Your final score is {self.score} ")
                self.title.destroy()
                self.question_label.destroy()
                self.answer_label.destroy()
                self.text.destroy()
                self.submit_button.destroy()

                #submit Name

                #Name Label
                self.name_label = tk.Label(self.root, text="Enter Name:", font=('Arial', 12), 
                bg='#D8C49F')
                self.name_label.pack(padx=20, pady=(150,5))

                #Name input
                self.nameVal = tk.StringVar()
                self.text = tk.Entry(self.root, textvariable=self.nameVal)
                self.text.pack(padx=20, pady=(0,10))

                #Submit answer button
                self.submit_button2 = tk.Button(self.root, text="Submit", font=('Arial', 12), width=8, 
                bg='#9F8C76', command=self.record)
                self.submit_button2.pack(pady=10)

        #Genenerator new question /answer
        n = random.randint(1,50)
        self.question_label['text'] = f"Find x: {self.items[n][0]}"
        self.correct_asnwer = self.items[n][1]
        print(self.correct_asnwer)

    def record(self):
        self.name = self.nameVal.get()

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
            players.append([self.name, self.score])

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
                writer.writerows([self.name, self.score])

        self.root.destroy()
        MENU()

class Medium():
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.n = 0

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.configure(bg='#D8C49F')
        self.root.title("Algebra Trainer! by DICHOSA")

        #Title Label
        self.title = tk.Label(self.root, text="MEDIUM", font=('Arial bold', 20), bg='#D8C49F', 
        width=15, height=2)
        self.title.pack(padx=10, pady=(40,30))


        #load questions
        file = open('Medium_Questions.csv')
        ez_diff = csv.reader(file)
        #go to items
        next(ez_diff)
        #get all items
        self.items = []
        for item in ez_diff:
            self.items.append(item)
        file.close()
        
        #Get question
        n = random.randint(1,40)
        self.question = f"Find x: {self.items[n][0]}"
        self.correct_asnwer = self.items[n][1]
        
        #Question Label
        self.question_label = tk.Label(self.root, text=self.question, font=('Arial', 16), 
        bg='#F1DBBF', width=35, height=5, borderwidth=2, relief="solid",)
        self.question_label.pack(padx=20, pady=(30,30))

        #Answer Label
        self.answer_label = tk.Label(self.root, text="Answer:", font=('Arial', 12), 
        bg='#D8C49F')
        self.answer_label.pack(padx=20, pady=(30,5))

        #Answer input
        self.answerVal = tk.StringVar()
        self.text = tk.Entry(self.root, textvariable=self.answerVal)
        self.text.pack(padx=20, pady=(0,10))

        #Submit answer button
        self.submit_button = tk.Button(self.root, text="Submit", font=('Arial', 12), width=8, 
        bg='#9F8C76', command=self.check_answer)
        self.submit_button.pack(pady=10)


        self.root.mainloop

    def check_answer(self):
        
        answer = self.answerVal.get()

        #questions and answers
        if answer == self.correct_asnwer:
            self.score += 2
            messagebox.showinfo("Correct! plus 2 point...", f"Points = {self.score}")
        else:
            self.lives -= 1
            messagebox.showinfo("Incorrect! Minus 1 life!", f"{self.lives} left")
            if self.lives == 0:
                messagebox.showinfo("Game Over!", f"Your final score is {self.score} ")
                self.title.destroy()
                self.question_label.destroy()
                self.answer_label.destroy()
                self.text.destroy()
                self.submit_button.destroy()

                #submit Name

                #Name Label
                self.name_label = tk.Label(self.root, text="Enter Name:", font=('Arial', 12), 
                bg='#D8C49F')
                self.name_label.pack(padx=20, pady=(150,5))

                #Name input
                self.nameVal = tk.StringVar()
                self.text = tk.Entry(self.root, textvariable=self.nameVal)
                self.text.pack(padx=20, pady=(0,10))

                #Submit answer button
                self.submit_button2 = tk.Button(self.root, text="Submit", font=('Arial', 12), width=8, 
                bg='#9F8C76', command=self.record)
                self.submit_button2.pack(pady=10)

        #Genenerator new question /answer
        n = random.randint(1,40)
        self.question_label['text'] = f"Find x: {self.items[n][0]}"
        self.correct_asnwer = self.items[n][1]
        print(self.correct_asnwer)

    def record(self):
        self.name = self.nameVal.get()

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
            players.append([self.name, self.score])

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
                writer.writerows([self.name, self.score])

        self.root.destroy()
        MENU()

class Hard():
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.n = 0

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.configure(bg='#D8C49F')
        self.root.title("Algebra Trainer! by DICHOSA")

        #Title Label
        self.title = tk.Label(self.root, text="HARD", font=('Arial bold', 20), bg='#D8C49F', 
        width=15, height=2)
        self.title.pack(padx=10, pady=(40,30))


        #load questions
        file = open('Hard_Questions.csv')
        ez_diff = csv.reader(file)
        #go to items
        next(ez_diff)
        #get all items
        self.items = []
        for item in ez_diff:
            self.items.append(item)
        file.close()
        
        #Get question
        n = random.randint(1,19)
        self.question = f"Find x: {self.items[n][0]}"
        self.correct_asnwer = self.items[n][1]
        
        #Question Label
        self.question_label = tk.Label(self.root, text=self.question, font=('Arial', 16), 
        bg='#F1DBBF', width=35, height=5, borderwidth=2, relief="solid",)
        self.question_label.pack(padx=20, pady=(30,30))

        #Answer Label
        self.answer_label = tk.Label(self.root, text="Answer:", font=('Arial', 12), 
        bg='#D8C49F')
        self.answer_label.pack(padx=20, pady=(30,5))

        #Answer input
        self.answerVal = tk.StringVar()
        self.text = tk.Entry(self.root, textvariable=self.answerVal)
        self.text.pack(padx=20, pady=(0,10))

        #Submit answer button
        self.submit_button = tk.Button(self.root, text="Submit", font=('Arial', 12), width=8, 
        bg='#9F8C76', command=self.check_answer)
        self.submit_button.pack(pady=10)


        self.root.mainloop

    def check_answer(self):
        
        answer = self.answerVal.get()

        #questions and answers
        if answer == self.correct_asnwer:
            self.score += 3
            messagebox.showinfo("Correct! plus 3 point...", f"Points = {self.score}")
        else:
            self.lives -= 1
            messagebox.showinfo("Incorrect! Minus 1 life!", f"{self.lives} left")
            if self.lives == 0:
                messagebox.showinfo("Game Over!", f"Your final score is {self.score} ")
                self.title.destroy()
                self.question_label.destroy()
                self.answer_label.destroy()
                self.text.destroy()
                self.submit_button.destroy()

                #submit Name

                #Name Label
                self.name_label = tk.Label(self.root, text="Enter Name:", font=('Arial', 12), 
                bg='#D8C49F')
                self.name_label.pack(padx=20, pady=(150,5))

                #Name input
                self.nameVal = tk.StringVar()
                self.text = tk.Entry(self.root, textvariable=self.nameVal)
                self.text.pack(padx=20, pady=(0,10))

                #Submit answer button
                self.submit_button2 = tk.Button(self.root, text="Submit", font=('Arial', 12), width=8, 
                bg='#9F8C76', command=self.record)
                self.submit_button2.pack(pady=10)

        #Genenerator new question /answer
        n = random.randint(1,19)
        self.question_label['text'] = f"Find x: {self.items[n][0]}"
        self.correct_asnwer = self.items[n][1]
        print(self.correct_asnwer)

    def record(self):
        self.name = self.nameVal.get()

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
            players.append([self.name, self.score])

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
                writer.writerows([self.name, self.score])

        self.root.destroy()
        MENU()

MENU()

