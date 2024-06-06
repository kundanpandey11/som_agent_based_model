import simtk.unit as unit
from simtk.openmm.app import PDBFile, Modeller, ForceField

# Load the PDB file
pdb = PDBFile('7dn3.pdb')

# Load the Amber14 force field and water model
ff = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')

# Create a Modeller object
modeller = Modeller(pdb.topology, pdb.positions)

# Get the topology from the modeller
topology = modeller.getTopology()

# Check if GLU residue template is present in the force field
glu_templates = ff.getMatchingTemplates('GLU')
if not glu_templates:
    raise ValueError("GLU residue template is missing in the force field.")

# Add water using the TIP3P model
modeller.addSolvent(ff, model='tip3p', padding=1.0*unit.nanometer)

# Write the force field parameters to a file
ff.write('amber14/tip3pfb.xml')
