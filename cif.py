import gemmi
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def display_cif(file_path):
    try:
        # Read the CIF file
        cif_block = gemmi.cif.read(file_path)[0]
        print(cif_block)
        structure = gemmi.make_small_structure_from_block(cif_block)
    except Exception as e:
        print(f"Error reading CIF file: {e}")
        return
    print("struncture", structure)
    try:
        # Extract atomic coordinates
        atoms = []
        for model in structure:
            for chain in model:
                for residue in chain:
                    for atom in residue:
                        atoms.append([atom.pos.x, atom.pos.y, atom.pos.z])
        
        if not atoms:
            print("No atoms found in the CIF file.")
            return
        
        atoms = np.array(atoms)

        # Plotting the atomic coordinates
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], marker='o')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    except Exception as e:
        print(f"Error processing CIF file: {e}")

# Example usage
file_path = '1100225.cif'
display_cif(file_path)
