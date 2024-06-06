from Bio.PDB import PDBParser
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Global variables to store file paths
file1_path = ""
file2_path = ""

def open_file1():
    global file1_path
    file1_path = filedialog.askopenfilename(filetypes=[("PDB files", "*.pdb"), ("All files", "*.*")])
    if file1_path:
        print(f"File 1 selected: {file1_path}")
        check_files()

def open_file2():
    global file2_path
    file2_path = filedialog.askopenfilename(filetypes=[("PDB files", "*.pdb"), ("All files", "*.*")])
    if file2_path:
        print(f"File 2 selected: {file2_path}")
        check_files()

def check_files():
    if file1_path and file2_path:
        print("Both files selected. Proceeding with further processing...")
        display_pdb(file1_path)
        display_pdb(file2_path)

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

root = tk.Tk()
root.title("Zoym Agent Based Modeling")
root.geometry("500x200")  # Setting width to 300 pixels and height to 100 pixels

# Dropdown menu
options = ["PDB FILES", "Pdb 1", "Pdb 2"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack()

# Buttons to open file dialogs
open_button1 = tk.Button(root, text="Open Pdb 1", command=open_file1)
open_button2 = tk.Button(root, text="Open Pdb 2", command=open_file2)

open_button1.pack()
open_button2.pack()

root.mainloop()
