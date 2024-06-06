from Bio.PDB import PDBParser, PDBIO
import py3Dmol

# Load the PDB file
parser = PDBParser()
structure = parser.get_structure("structure", "7dn3.pdb")

# Write the structure to a temporary PDB file
pdb_file = "temp_structure.pdb"
io = PDBIO()
io.set_structure(structure)
io.save(pdb_file)

# Initialize viewer
viewer = py3Dmol.view()

# Read the structure from the temporary PDB file
with open(pdb_file, "r") as f:
    model_data = f.read()

# Add the structure to the viewer
viewer.addModel(model_data, "pdb")

# Set the style and display options (optional)
viewer.setStyle({"cartoon": {"color": "spectrum"}})
viewer.zoomTo()
with open("protein_structure.html", "w") as html_out:
    html_out.write(viewer.render())
# Save the visualization to an HTML file
viewer.zoomTo()
viewer.show()

