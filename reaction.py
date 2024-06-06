from simtk.openmm.app import PDBFile, Modeller, ForceField
from simtk.openmm import app
from simtk import unit
import numpy as np

# Step 1: Read PDB Files
pdb1 = PDBFile('1aki.pdb')
pdb2 = PDBFile('7dn3.pdb')

# Create modeller objects
modeller1 = Modeller(pdb1.topology, pdb1.positions)
modeller2 = Modeller(pdb2.topology, pdb2.positions)

# Step 2: Load Force Field
forcefield = ForceField('charmm36.xml')  # Adjust paths as needed

# Apply force field to modeller objects
modeller1.addSolvent(forcefield)
modeller2.addSolvent(forcefield)

# Step 3: Create OpenMM System
pdb1_system = forcefield.createSystem(modeller1.topology, nonbondedMethod=app.NoCutoff)
pdb2_system = forcefield.createSystem(modeller2.topology, nonbondedMethod=app.NoCutoff)

# Create OpenMM context
integrator = app.LangevinIntegrator(300*unit.kelvin, 1/unit.picosecond, 0.002*unit.picoseconds)
platform = app.Platform.getPlatformByName('CPU')
pdb1_context = app.Context(pdb1_system, integrator, platform)
pdb2_context = app.Context(pdb2_system, integrator, platform)

# Set initial positions
pdb1_context.setPositions(modeller1.positions)
pdb2_context.setPositions(modeller2.positions)

# Minimize energy
app.LocalEnergyMinimizer.minimize(pdb1_context)
app.LocalEnergyMinimizer.minimize(pdb2_context)

# Get potential energy
state_1 = pdb1_context.getState(getEnergy=True)
state_2 = pdb2_context.getState(getEnergy=True)
potential_energy_1 = state_1.getPotentialEnergy().value_in_unit(unit.kilojoules_per_mole)
potential_energy_2 = state_2.getPotentialEnergy().value_in_unit(unit.kilojoules_per_mole)

# Step 3: Identify Atoms with Highest and Lowest Potential Energy
# Example: Find atom index with highest potential energy
highest_energy_atom_index_pdb1 = np.argmax(potential_energy_1)
highest_energy_atom_index_pdb2 = np.argmax(potential_energy_2)

# Step 4: React Atoms
# Example: Form a new molecule by combining the highest energy atom from pdb1 with the lowest energy atom from pdb2
# Here, we simply remove the highest energy atom from modeller1 and the lowest energy atom from modeller2
modeller1.delete([highest_energy_atom_index_pdb1])
modeller2.delete([highest_energy_atom_index_pdb2])

# Step 5: Add virtual sites for water models
# This step is needed if you are using four and five-site water models
modeller1.addExtraParticles()
modeller2.addExtraParticles()

# Step 6: Update Molecule Structures
# Example: Update pdb1 and pdb2 structures to reflect the reaction
# We will save the updated structures as new PDB files
with open('updated_protein1.pdb', 'w') as outfile:
    app.PDBFile.writeFile(modeller1.topology, modeller1.positions, outfile)

with open('updated_protein2.pdb', 'w') as outfile:
    app.PDBFile.writeFile(modeller2.topology, modeller2.positions, outfile)
