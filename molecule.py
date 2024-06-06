from Bio.PDB import PDBParser, PDBIO

# Load the PDB file
parser = PDBParser()
structure = parser.get_structure("original_structure", "4zld.pdb")

# Select the chain or residue range of the molecule you want to extract
# For example, to extract chain A:
chain_id = 'A'
selected_chain = structure[0][chain_id]

# Create a new structure containing only the selected chain
new_structure = selected_chain.get_parent()

# Save the selected molecule to a new PDB file
io = PDBIO()
io.set_structure(new_structure)
io.save("4zld_molecule.pdb")