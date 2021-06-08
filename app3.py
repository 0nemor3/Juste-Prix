import tkinter as tk
import random as rd
import threading
import time


global time_up
time_up = False
global essais_max
essais_max = False
global gagne
gagne = False
global counter
counter = 5
global affichage_resultat
affichage_resultat = ""



def generation_prix():
	global number
	number = rd.randint(0, 100)
	print(number)


generation_prix()


def is_a_number(test):
    return test.isnumeric()


def interval_is_correct(test):
    if test >= 1 and test <= 100:
        return True
    return False


def minuteur():
	global affichage_resultat
	seconds = 60
	for _ in range(60):
		seconds -= 1
		time.sleep(1)
		temps.config(text=seconds)
		if essais_max == True or gagne == True:
			break
	if seconds == 0:
	    affichage_resultat = "Le temps est ecoule !"
	    affichage.config(text=affichage_resultat)
	    test_nombre.config(state='disabled')





def main(*args):
	global gagne, counter, essais_max, affichage_resultat
	if time_up == False and essais_max == False and gagne == False:
		test = test_nombre.get()
		if is_a_number(test) == True:
			test = int(test)
			if interval_is_correct(test) == True:
				if counter == 5:
					minuteur_thread = threading.Thread(target=minuteur)
					minuteur_thread.start()
				if test > number:
					affichage_resultat = "Plus petit !"
				elif test < number:
					affichage_resultat = "Plus grand !"
				elif test == number:
					affichage_resultat = "C'est gagne !"
					gagne = True
					test_nombre.config(state='disabled')
				counter -= 1

				affichage_counter.config(text="Nombre d'essais restants : " + str(counter))
			else:
				affichage_resultat = "L'intervale est entre 0 et 100 !"
			if counter <= 0:
				essais_max = True
				affichage_resultat = "Vous n'avez plus d'essais restants !"
				test_nombre.config(state='disabled')
				
		elif test != "":
			affichage_resultat = "Mauvais format !"
	affichage.config(text=affichage_resultat)
	test_nombre.delete(0, 'end')








root = tk.Tk()
root.title("Juste Prix")
root.minsize(720, 480)
root.maxsize(820, 580)
root.iconbitmap("")
root.config(background='#90EE90')


topframe = tk.Frame(root, bg='#90EE90')
titre = tk.Label(topframe, text="Bienvenue sur le célebre jeu du Juste Prix", font=("Arial", 20), bg='#90EE90')
titre.pack()
instructions = tk.Label(topframe, text="Tu dois deviner le prix auquel je pense, il se situe entre 1 et 100", font=("Arial", 16), bg='#90EE90')
instructions.pack()
topframe.pack()

affichage_counter = tk.Label(root, text="Nombre d'essais restants : 5")
frame = tk.Frame(root, bg='#90EE90')

affichage_counter.pack()
left_frame = tk.Frame(frame)
test_nombre = tk.Entry(left_frame, font=("Arial", 16), state='normal')
test_nombre.bind("<Return>", main)
test_nombre.pack()
left_frame.grid(row=0, column=0)
right_frame = tk.Frame(frame)
essai_button = tk.Button(right_frame, text="Tentez votre chance", command=main)
essai_button.pack()
right_frame.grid(row=0, column=1)
frame.pack()
feedback = tk.Frame(root, bg='#90EE90')
affichage = tk.Label(feedback, text=affichage_resultat, bg='#90EE90')
affichage.pack()
temps = tk.Label(feedback, text="60", bg='#90EE90')
temps.pack()
feedback.pack()




root.mainloop()
