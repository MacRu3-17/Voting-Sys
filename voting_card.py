#!/usr/bin/python3
#imports ------------------
from guizero import App, Box, Text, TitleBox, ButtonGroup, Combo, PushButton, Window, TextBox
import string
from string import *
import csv 

#csv file setup-----------
# field names 
fields = ['Name', 'SSN', 'DLN']
# name of csv file 
with open(".voter_records.csv", 'w') as csvfile:
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile) 
	# writing the fields 
	csvwriter.writerow(fields) 
				    
#count variables for ButtonGroup-choices------------
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
#functions---------------------------------------
#reOpen the Login Window and clear the inputs
def open_login():
	window.show(wait=True)
	name_input.value="Type NAME here"
	SSN_input1.value="###"
	SSN_input2.value="##"
	SSN_input3.value="####"
	DrvLic_input.value="Type DL# here"
#Log voters---------------------------------------
def close_login():
	SSN = str(SSN_input1.value) + str(SSN_input2.value) + str(SSN_input3.value)
	# data rows of csv file 
	rows = [[name_input.value, SSN, DrvLic_input.value]]
	if len(SSN) == 0 and (len(DrvLic_input.value) == 0 or DrvLic_input.value == "Type DL# here"):
		window.warn("No SSN# or DL#!", "You must put in either\n your Social Security Number\n OR your Driver's License Number!")
		if len(SSN) != 9:
			window.warn("SSN# not right number!", "Either your Social Security Number\n has too many characters\n or not enough characters!")
		elif len(DrvLic_input.value) < 7:
			window.warn("DL# Too Short!", "Your Driver's License Number\n can not be shorter\n than 7 characters!")
	else:
		# writing to csv file 
		with open(".voter_records.csv", 'a') as csvfile: 
			# creating a csv writer object 
			csvwriter = csv.writer(csvfile) 
				
			# writing the data rows 
			csvwriter.writerows(rows)
		window.hide()
		choices1.value = ""
		choices2.value = ""
		choices3.value = ""
		choices4.value = ""
		choices5.value = ""
		choices6.value = ""

def close_app():
	open_login()
	
def submit_vote():
	#Each Count-Variable made "Global" for each conditionl choice to Increment------------
	global count1
	global count2
	global count3
	global count4
	global count5
	global count6
	#Prevents Prez multi-vote error-----------
	if choices1.value and choices2.value:
		app.warn("Oops!", "You have selected more than 1 Presidential Candidate, try again.")
		choices1.value = ""
		choices2.value = ""
		choices3.value = ""
	elif choices2.value and choices3.value:
		app.warn("Oops!", "You have selected more than 1 Presidential Candidate, try again.")
		choices1.value = ""
		choices2.value = ""
		choices3.value = ""
	elif choices1.value and choices3.value:
		app.warn("Oops!", "You have selected more than 1 Presidential Candidate, try again.")
		choices1.value = ""
		choices2.value = ""
		choices3.value = ""
	#Prevents VP multi-vote error----------------
	if choices4.value and choices5.value:
		app.warn("Oops!", "You have selected more than 1 VICE-Presidential Candidate, try again.")
		choices4.value = ""
		choices5.value = ""
		choices6.value = ""
	elif choices5.value and choices6.value:
		app.warn("Oops!", "You have selected more than 1 VICE-Presidential Candidate, try again.")
		choices4.value = ""
		choices5.value = ""
		choices6.value = ""
	elif choices4.value and choices6.value:
		app.warn("Oops!", "You have selected more than 1 VICE-Presidential Candidate, try again.")
		choices4.value = ""
		choices5.value = ""
		choices6.value = ""
		
	#writes Prez choice selection to text file with increment vote count-------		
	fileHandle = open('.results', 'a')
	if choices1.value:
		#Incrementals for each count of choices group by value's text------------
		count1 += 1
		fileHandle.write(choices1.value_text +" = "+ str(count1) +"\n")
	elif choices2.value:
		count2 += 1
		fileHandle.write(choices2.value_text +" = "+ str(count2) +"\n")
	elif choices3.value:
		count3 += 1
		fileHandle.write(choices3.value_text +" = "+ str(count3) +"\n")
	#writes VP choice selection to text file with increment vote count-------	
	if choices4.value:
		count4 += 1
		fileHandle.write(choices4.value_text +" = "+ str(count4) +"\n")
	elif choices5.value:
		count5 += 1
		fileHandle.write(choices5.value_text +" = "+ str(count5) +"\n")
	elif choices6.value:
		count6 += 1
		fileHandle.write(choices6.value_text +" = "+ str(count6) +"\n")
	open_login()
	
def save_when_closed():
	#Then write it as string to file!-----------
	if app.yesno("Save", "Do you want to save?"):
		app.destroy()
		
	
#app---------------------------
app = App(title="Ballot", layout="grid")
app.bg = "white"

box1 = Box(app, grid=[0,0])
label1 = Text(box1, text="Presidential Candidates:", color="gold")
titlebox1 = TitleBox(box1, "President")
label3 = Text(titlebox1, text="Republicans:")
label3.bg = "red"
choices1 = ButtonGroup(titlebox1, options=[], selected="")
label4 = Text(titlebox1, text="Independent/3rd Party:")
label4.bg = "green"
choices2 = ButtonGroup(titlebox1, options=[], selected="")
label5 = Text(titlebox1, text="Democrats:")
label5.bg = "blue"
choices3 = ButtonGroup(titlebox1, options=[], selected="")

box2 = Box(app, layout="grid", grid=[1,0])
label2 = Text(box2, text="Vice-Presidential Candidates:", color="silver", grid=[0,0])
titlebox2 = TitleBox(box2, "Vice-President", layout="grid", grid=[0,1])
label6 = Text(titlebox2, text="Republicans:", grid=[0,0])
label6.bg = "red"
choices4 = ButtonGroup(titlebox2, options=[], selected="", grid=[0,1])
label7 = Text(titlebox2, text="Independent/3rd Party:", grid=[0,2])
label7.bg = "green"
choices5 = ButtonGroup(titlebox2, options=[], selected="", grid=[0,3])
label8 = Text(titlebox2, text="Democrats:", grid=[0,4])
label8.bg = "blue"
choices6 = ButtonGroup(titlebox2, options=[], selected="", grid=[0,5])

box3 = Box(box2, layout="grid", grid=[0,2])
button1 = PushButton(box3, text='Submit', command=submit_vote, grid=[0,0])
button2 = PushButton(box3, text='Cancel', command=close_app, grid=[1,0])

with open('.ballot', 'r') as fh:
	specific_lines1 = [2]
	for pos, l_num in enumerate(fh):
		if pos in specific_lines1:
			for a in l_num.split(","):
				if a != "[\'\'":
					if a.rfind(']') != -1:
						choices1.append(a[0:-2])
						choices1.remove("[\'\'")
					else:
						choices1.append(a)
with open('.ballot', 'r') as fh:
	specific_lines2 = [4]
	for pos, l_num in enumerate(fh):
		if pos in specific_lines2:
			for b in l_num.split(","):
				if b != "[\'\'":
					if b.rfind(']') != -1:
						choices2.append(b[0:-2])
						choices2.remove("[\'\'")
					else:
						choices2.append(b)
with open('.ballot', 'r') as fh:
	specific_lines3 = [6]
	for pos, l_num in enumerate(fh):
		if pos in specific_lines3:
			for c in l_num.split(","):
				if c != "[\'\'":
					if c.rfind(']') != -1:
						choices3.append(c[0:-2])
						choices3.remove("[\'\'")
					else:
						choices3.append(c)
with open('.ballot', 'r') as fh:
	specific_lines4 = [9]
	for pos, l_num in enumerate(fh):
		if pos in specific_lines4:
			for d in l_num.split(","):
				if d != "[\'\'":
					if d.rfind(']') != -1:
						choices4.append(d[0:-2])
						choices4.remove("[\'\'")
					else:
						choices4.append(d)
with open('.ballot', 'r') as fh:
	specific_lines5 = [11]
	for pos, l_num in enumerate(fh):
		if pos in specific_lines5:
			for e in l_num.split(","):
				if e != "[\'\'":
					if e.rfind(']') != -1:
						choices5.append(e[0:-2])
						choices5.remove("[\'\'")
					else:
						choices5.append(e)
with open('.ballot', 'r') as fh:
	specific_lines6 = [13]
	for pos, l_num in enumerate(fh):
		if pos in specific_lines6:
			for f in l_num.split(","):
				if f != "[\'\'":
					if f.rfind(']') != -1:
						choices6.append(f[0:-2])
						choices6.remove("[\'\'")
					else:
						choices6.append(f)
#LoginWindow design-------------------------
window = Window(app, "Voter Login")
box4 = Box(window, layout="grid")
nameLabel = Text(box4, text="Your Name:", grid=[0,0], align='left')
name_input = TextBox(box4, text="Type NAME here", width=20, grid=[0,1], align='left')
box5 = Box(box4, layout="grid", grid=[0,2])
infoLabel = Text(box5, text="Input Your\n Social Security\n Number\n or your Driver's\n License Number!:", grid=[0,0])
box6 = Box(box5, layout="grid", grid=[1,0], align='right')
SSN_input1 = TextBox(box6, text="###", width=3, grid=[0,0], align='right', hide_text=True)
SSN_input2 = TextBox(box6, text="##", width=2, grid=[1,0], hide_text=True)
SSN_input3 = TextBox(box6, text="####", width=4, grid=[2,0], align='left')
DivLabel = Text(box6, text="/OR:", grid=[1,1])
DrvLic_input = TextBox(box6, text="Type DL# here", width=14, grid=[2,2])
button3 = PushButton(box4, text='VOTE!', command=close_login, grid=[0,3])

app.when_closed = save_when_closed

app.display()
