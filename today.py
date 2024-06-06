
from Bio.PDB import *
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            # Do something with the content, for now just print it
            print(content)

root = tk.Tk()
root.title("Zoym Agent Based Modeling")
root.geometry("500x200")  # Setting width to 300 pixels and height to 100 pixels

# Dropdown menu
options = ["PDB FILES", "Pdb 1", "Pdb 2"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack()

# Button to open file dialog
open_button1 = tk.Button(root, text="Open Pdb 1", command=open_file)
open_button2 = tk.Button(root, text="Open Pdb 2", command=open_file)

open_button1.pack()
open_button2.pack()





def display_pdb(pdb_file):
    parser = PDBParser()
    structure = parser.get_structure('protein', pdb_file)
    atoms = []
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    atoms.append(atom.get_coord())
    atoms = np.array(atoms)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

import time 

root.quit()

# file1 = input("Please provide file 1 : ")
# file2 = input("Please provide file 2 : ")
file3 = "7dn3.pdb"
residue = '4zld.pdb'


for i in range(7, 10):
    time.sleep(2)
    print("Empty comment after 2 seconds | count ", i)
    if i == 9:
        display_pdb(file3)

root.mainloop()
