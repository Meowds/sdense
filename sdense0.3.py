import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu

# Main window
root = tk.Tk()
root.geometry('480x360')
root.resizable(False, False)
root.title('Button Demo')
loadm = False
asm = []
curx=0
cury=0
root.option_add('*tearOff', False)
text_area = tk.Text(root,bg = 'Black' , fg = 'White',insertbackground='Pink', wrap='word')
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
edit_menu = Menu(menubar)
assetm = Menu(menubar)
# add a menu item to the menu


# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)
menubar.add_cascade(
    label='Edit',
    menu=edit_menu
)

text_area.pack(expand=1, fill='both')
name_entry = None
name_label = None
def open_file():

    file_path = filedialog.askopenfilename()

    if file_path:

        with open(file_path, 'r') as file:

            content = file.read()

            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
def show_info():
    print('')
def click(event):
	print('')
def save():
    try:
        with open("main.asm", "w", encoding="utf-8") as f:
            f.write(text_area.get('1.0',tk.END))
        print("File saved successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

#def load():
#    global loadm, name_entry, name_label, result_label, asm
#    
#    if not loadm:
#        # Step 1: Create input controls
#        name_label = ttk.Label(root, text='Load directory from ... (press load again to load)')
#        name_label.pack(pady=4, after=button_frame)
#        
#        name_entry = ttk.Entry(root, width=10)
#        name_entry.pack(pady=5, after=name_label)
#        
#        loadm = True
#    else:
#        # Step 2: Read the entry value FIRST before destroying the widget
#        file_path = name_entry.get().strip()
#        
#        # Clean up input controls
#        if name_entry:
#            name_entry.destroy()
#            name_entry = None
#        if name_label:
#            name_label.destroy()
#            name_label = None
#            
#        loadm = False
#        
#        # Step 3: Attempt to load the file
#        if file_path:
#            try:
#                with open(file_path, "r", encoding="utf-8") as f:
#                    content = f.read()
#                    
#                asm = content.splitlines()  # Store lines in the global list
#                
#                # Clear previous result label if one exists
#                listbox.delete(0, tk.END)
#                for line in asm:
#                    listbox.insert(tk.END, line)
#            except Exception as e:
#                print(f"Error reading file: {e}")


# Save and Load buttons frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)
wspace_frame = ttk.Frame(root)
wspace_frame.pack(pady=10)

file_menu.add_command(
    label='Save to',
    command=save
)
file_menu.add_command(
    label='Load from',
    command=open_file
)
edit_menu.add_command(
    label='Code',
    command=save
)
edit_menu.add_cascade(
    label='Assets',
    menu=assetm
)
root.mainloop()