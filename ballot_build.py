#!/usr/bin/python3
#imports ------------------
from guizero import App, Box, Text, TextBox, TitleBox, ListBox, ButtonGroup, Combo, PushButton, Window
#app---------------------------
app = App(title="Ballot Builder")
app.bg = "white"

#functions--------------------------------------------------------------------------
def add_entry():
	if choice.value == "Presidential" and combo.value == "Independent/3rdParty":
		listbox5.append(name_input.value)
	elif choice.value == "Presidential" and combo.value == "Republican":
		listbox1.append(name_input.value)
	elif choice.value == "Presidential" and combo.value == "Democrat":
		listbox2.append(name_input.value)
	elif choice.value == "Vice-Presidential" and combo.value == "Independent/3rdParty":
		listbox6.append(name_input.value)
	elif choice.value == "Vice-Presidential" and combo.value == "Republican":
		listbox3.append(name_input.value)
	elif choice.value == "Vice-Presidential" and combo.value == "Democrat":
		listbox4.append(name_input.value)

def del_entry():
	if choice.value == "Presidential" and combo.value == "Independent/3rdParty":
		listbox5.remove(name_input.value)
	elif choice.value == "Presidential" and combo.value == "Republican":
		listbox1.remove(name_input.value)
	elif choice.value == "Presidential" and combo.value == "Democrat":
		listbox2.remove(name_input.value)
	elif choice.value == "Vice-Presidential" and combo.value == "Independent/3rdParty":
		listbox6.remove(name_input.value)
	elif choice.value == "Vice-Presidential" and combo.value == "Republican":
		listbox3.remove(name_input.value)
	elif choice.value == "Vice-Presidential" and combo.value == "Democrat":
		listbox4.remove(name_input.value)
		
def save_ballot():
	fileHandle = open('.ballot', 'w')
	fileHandle.write(label2.value + "\n" + label4.value + "\n" + str(listbox1.items) + "\n" + label8.value + "\n" + str(listbox5.items) + "\n" + label5.value + "\n" + str(listbox2.items) + "\n" + label3.value + "\n" + label6.value + "\n" + str(listbox3.items) + "\n" + label9.value + "\n" + str(listbox6.items) + "\n" + label7.value + "\n" + str(listbox4.items) + "\n")
	ballot = Window(app)
	choices1 = ButtonGroup(ballot, options=[])
	choices2 = ButtonGroup(ballot, options=[])
	for item in listbox1.items[1:]:
		name = item
		choices1.append(str(name))
	for item in listbox5.items[1:]:
		name = item
		choices1.append(str(name))
	for item in listbox2.items[1:]:
		name = item
		choices1.append(str(name))
	for item in listbox3.items[1:]:
		name = item
		choices2.append(str(name))
	for item in listbox6.items[1:]:
		name = item
		choices2.append(str(name))
	for item in listbox4.items[1:]:
		name = item
		choices2.append(str(name))
	#fileHandle.close()
	#app.destroy()

def close_app():
	app.destroy()
	
#widgets-----------------------------------
label1 = Text(app, text="Candidates:")
label1.text_size = 20
label1.font = "Times New Roman"

box1 = Box(app)

box2 = Box(box1, align="top")
label2 = Text(box2, text="Presidential:")
label2.text_size = 16
label2.text_color = "gold"

box4 = Box(box2, layout="grid", align="left")
label4 = Text(box4, text="Republican:", grid=[0,0])
label4.text_color = "red"
titlebox1 = TitleBox(box4, "List", grid=[0,1])
listbox1 = ListBox(titlebox1, items=[""], scrollbar=True)

label8 = Text(box4, text="Independent/other:", grid=[1,0])
label8.text_color = "green"
titlebox5 = TitleBox(box4, "List", grid=[1,1])
listbox5 = ListBox(titlebox5, items=[""], scrollbar=True)

label5 = Text(box4, text="Democrat:", grid=[2,0])
label5.text_color = "blue"
titlebox2 = TitleBox(box4, "List", grid=[2,1])
listbox2 = ListBox(titlebox2, items=[""], scrollbar=True)

#buttons_and_Input------------------------------------
box5 = Box(box2, layout="grid", align="right")
choice = ButtonGroup(box5, options=["Presidential", "Vice-Presidential"], selected="Presidential", grid=[0,0])
combo = Combo(box5, options=["Republican", "Independent/3rdParty", "Democrat"], selected="Independent/3rdParty", grid=[0,1])
name_input = TextBox(box5, text="Type NAME here", grid=[0,2], width=20)
button1 = PushButton(box5, text="Add +", grid=[0,3], align="left", command=add_entry)
button2 = PushButton(box5, text="Delete", grid=[0,3], align="right", command=del_entry)

#backToAssignment------------------------------------
box3 = Box(box1, align="bottom")
label3 = Text(box3, text="Vice-Presidential:")
label3.text_size = 16
label3.text_color = "silver"

box6 = Box(box3, layout="grid", align="left")
label6 = Text(box6, text="Republican:", grid=[0,0])
label6.text_color = "red"
titlebox3 = TitleBox(box6, "List", grid=[0,1])
listbox3 = ListBox(titlebox3, items=[""], scrollbar=True)

label9 = Text(box6, text="Independent/other:", grid=[1,0])
label9.text_color = "green"
titlebox6 = TitleBox(box6, "List", grid=[1,1])
listbox6 = ListBox(titlebox6, items=[""], scrollbar=True)

label7 = Text(box6, text="Democrat:", grid=[2,0])
label7.text_color = "blue"
titlebox4 = TitleBox(box6, "List", grid=[2,1])
listbox4 = ListBox(titlebox4, items=[""], scrollbar=True)

#buttonsAndSaveInput----------------------------------------
box7 = Box(box3, align="right")
button3 = PushButton(box7, text="Save", align="left", command=save_ballot)
button4 = PushButton(box7, text="Cancel", align="right", command=close_app)

#display-----------
app.display()
