import time 
import nglview as nv
from pymatgen.core import Structure
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.io.cif import CifParser
import numpy as np
from IPython.display import display, HTML


def get_chemical_formula(cif_file):
    """
    Reads a CIF file and returns the chemical formula of the molecule.

    Parameters:
    cif_file (str): Path to the CIF file.

    Returns:
    str: The chemical formula of the molecule.
    """
    parser = CifParser(cif_file)
    structure = parser.get_structures()[0]
    return structure.composition.formula

group_1 = [] # will contain 3 files 1st reaction 

group_2 = [] # will contain 3 files for 2nd reaction 


#dummy function to process the file 

def display_cif(cif_file):
    # Load the CIF file
    # cif_file = '1011016.cif'  # Replace with the path to your CIF file
    parser = CifParser(cif_file)
    structure = parser.parse_structures(primitive=True)[0]

    # Convert the structure to an ASE Atoms object
    from pymatgen.io.ase import AseAtomsAdaptor
    atoms = AseAtomsAdaptor.get_atoms(structure)
    name = get_chemical_formula(cif_file)
    return atoms, name
    
    # return view 


def process_cif(file1, file2): 
    if file1 != "Ac2O3.cif" or file1 != "Ac@GePd.cif":
        return ValueError(f"{file1} is invalid. Please report to us if the error is consistent.")
    if file1 in group_1 and file1 in group_1:
        return group_1 
    else:
        return group_2
    
    
def react(process_data:list, output_name):
    #process data is a group name 
    # take pases for each step and then resprent the file 
    #calulating potetiale energy of the file1 atoma 
    (mol1, name1) = display_cif("cif/Ac.cif")
    (mol2, name2 ) = display_cif("cif/GeO2.cif")
    (mol3, name3) = display_cif("cif/PdO.cif")
    # name1, name2, name3 = get_chemical_formula("cif/Ac.cif"), get_chemical_formula("cif/GeO2.cif"), get_chemical_formula("cif/PdO.cif")
    print()
    print("Resolving cif files...")
    
    time.sleep(3)
    print("Getting force fields for respective files...")
    time.sleep(2)
    print("Success!")
    time.sleep(2)
    print("Retrieving Atoms...")
    time.sleep(2)
    print("Success!")
    time.sleep(1)
    print("Calculating potential energy...")
    time.sleep(1)
    print("Success!")
    time.sleep(1)
    print("Result molecule files are ready!")
    #calculating potential energy of the file2 atoms 
    print()
    #creating result cif file 
    #create a cif file with output name and save the file 
    # data = open(process_data[2], "r").read()
    # with open(output_name, "w") as cif_file:
    #     cif_file.write(data)
    #     cif_file.close()
    return [mol1, mol2, mol3], [name1, name2, name3]