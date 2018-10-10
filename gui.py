import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import sys
import functions as f

class AddGUI(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('Organize shapefiles')
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.grid()
        self.define_widgets()

    def define_widgets(self):
        # Create labels for source and destination
        lbl_source = tk.Label(self)
        lbl_source['text'] = 'Select a folder'
        lbl_source.grid(row=0, column=0)
        lbl_source['anchor'] = tk.CENTER

        btn_folder = tk.Button(self)
        btn_folder['text'] = 'Browse'
        btn_folder['command'] = lambda :(self.get_folder())
        btn_folder.grid(row = 1, column = 0, sticky='NWES')

        btn_clean = tk.Button(self)
        btn_clean['text'] = 'Clean directory'
        btn_clean['command'] = lambda :(self.clean_folder(self.folder))
        btn_clean.grid(row=2, column=0, sticky='NWES')

        btn_quit = tk.Button(self)
        btn_quit['text'] = 'Quit'
        btn_quit['command'] = lambda :(self.quit())
        btn_quit.grid(row=3, column = 0, sticky='NWES')

        # Create result label
        # lbl_result = tk.Label(self)
        # lbl_result['text'] = ""
        # lbl_result['anchor'] = tk.CENTER
        # lbl_result.grid(row=4, column = 0, columnspan = 1 )

    def get_folder(self):
        self.folder = fd.askdirectory()

    def clean_folder(self, folder):
        shapefile_names = f.read_directory(folder)
        f.create_sub_directory(shapefile_names)
        f.move_shapefiles(shapefile_names)
        # lbl_result['text'] = "The {} shapefiles \n found in: '{}'  have been cleaned.".format(shapefile_names, folder)
        self.pop_up("The {} shapefiles \n found in: '{}'  have been cleaned.".format(shapefile_names, folder))

    def quit(self):
        sys.exit(0)

    def pop_up(self, text):
        showinfo('', text)



# Supply main program
my_gui = AddGUI()
my_gui.mainloop()