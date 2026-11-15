import tkinter as tk
import p65a 
from p65a import *
import sys
sys.path.append("../src/") 
import crcmod
import webbrowser
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
crc16 = crcmod.predefined.mkCrcFun('xmodem')
UART_CTRL = Literal(0xa000, type=Addr)
UART_DATA = Literal(0xa001, type=Addr)
cbg='Black'
cfg='Green'
cibg='White'
mui=False

themes=[] #color names coild also just be used here

# Main window
root = tk.Tk()
root.geometry('480x360')
root.resizable(False, False)
root.title('Button Demo')
loadm = False
asm = []
program =[]
root.option_add('*tearOff', False)
text_area = tk.Text(root,bg = cbg , fg = cfg,insertbackground=cibg, wrap='word')
mb = Menu(root)
root.config(menu=mb)

# create a menu

fileM = Menu(mb)
editM = Menu(mb)
assetm = Menu(mb)
assem= Menu(mb)
about= Menu(mb)
custom=Menu(mb)
codea_menu=Menu(mb)
# add a menu item to the menu


# add the File menu to the mb
mb.add_cascade(
    label="File",
    menu=fileM
)
mb.add_cascade(
    label='Edit',
    menu=editM
)
mb.add_cascade(
    label='Assemble',
    menu=assem
)
mb.add_cascade(
    label='Appearence',
    menu=custom
)
mb.add_cascade(
    label='About',
    menu=about
)


text_area.pack(expand=1, fill='both')
name_entry = None
name_label = None
def asmb():
    if True:
        program=text_area.get('1.0',tk.END)
        concrete_prog, labels = concretise(program)
        out = assemble(concrete_prog, labels)
        rom = out[0xc000:]
        text_area.delete(1.0,tk.END)
        text_area.insert(tk.END, rom)
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
    if file_path == None:
    	text_area.delete(1.0, tk.END)
    #cant open .bin files but i guess it should be fine if asm and txt can be opened
def save():
  file_path = filedialog.asksaveasfilename(
      defaultextension=".asm",
      filetypes=[("Assembly Files", "*.asm"), ("All Files", "*.*")],
  )
  if file_path:
    try:
      with open(file_path, "w", encoding="utf-8") as f:
        f.write(text_area.get("1.0", tk.END))
      print(f"File successfully saved to {file_path}")
    except Exception as e:
      print(f"An error occurred while saving: {e}")
def tmui():
   pass
def bow():
   global cbg,cfg
   cbg='White'
   cfg='Black'
   txtupd()
def wob():
	global cbg,cfg
	cbg='Black'
	cfg='White'
	txtupd()
def gob():
	global cbg,cfg
	cbg='Black'
	cfg='Green'
	txtupd()
def yob():
	global cbg,cfg
	cbg='Black'
	cfg='Yellow'
	txtupd()
def bog():
	global cbg,cfg
	cbg='Gray'
	cfg='Brown'
	txtupd()
def txtupd():
    text_area.config(bg = cbg , fg = cfg)
    try:
        text_area.config(insertbackground = cifg)
    except:
        pass
def web():
	pass
	webbrowser.open('https://github.com/Meowds/sdense')
def ccode():
	pass
# Save and Load buttons frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)
wspace_frame = ttk.Frame(root)
wspace_frame.pack(pady=10)

fileM.add_command(
    label='Save to',
    command=save
)
fileM.add_command(
    label='Load from',
    command=open_file
)
assem.add_command(
    label='Assemble',
    command=asmb
)
editM.add_command(
    label='Code',
    command=ccode
)
editM.add_cascade(
    label='Assets',
    menu=assetm
)
custom.add_cascade(
    label='Code editor',
    menu=codea_menu,
)
custom.add_command(
    label='Toggle Mobile UI',
    command=tmui
)
codea_menu.add_command(
    label='White on Black',
    command=wob
)
codea_menu.add_command(
    label='Black on White',
    command=bow
)
codea_menu.add_command(
    label='Green on Black',
    command=gob
)
codea_menu.add_command(
    label='Yellow on Black',
    command=yob
)
codea_menu.add_command(
    label='Brown on Gray',
    command=bog
)
about.add_command(
    label='Creators Github',
    command=web
)
root.mainloop()