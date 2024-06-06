import nglview as nv
from pymatgen.core import Structure
from pymatgen.io.cif import CifParser

# Load the CIF file
cif_file = '1100225.cif'  # Replace with the path to your CIF file
parser = CifParser(cif_file)
structure = parser.parse_structures(primitive=True)[0]

# Convert the structure to an ASE Atoms object
from pymatgen.io.ase import AseAtomsAdaptor
atoms = AseAtomsAdaptor.get_atoms(structure)
print(atoms)
# Visualize using nglview
view = nv.show_ase(atoms)
view.add_unitcell()
view
