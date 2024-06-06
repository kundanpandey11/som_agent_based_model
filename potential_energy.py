import simtk.openmm as mm
from simtk.openmm.app import PDBFile
from simtk.unit import *

# Load PDB file
pdb = PDBFile('your_pdb_file.pdb')

# Load force field
forcefield = mm.app.ForceField('forcefield.xml')  # Replace 'forcefield.xml' with your force field file

# Create system
system = forcefield.createSystem(pdb.topology, nonbondedMethod=NoCutoff)

# Create integrator
integrator = mm.VerletIntegrator(1.0 * femtoseconds)

# Create context
platform = mm.Platform.getPlatformByName('Reference')  # Use 'OpenCL' or 'CUDA' for GPU acceleration if available
context = mm.Context(system, integrator, platform)

# Set positions
context.setPositions(pdb.positions)

# Compute potential energy
state = context.getState(getEnergy=True)
potential_energy = state.getPotentialEnergy().value_in_unit(kilojoules_per_mole)

print("Potential energy:", potential_energy, "kJ/mol")
