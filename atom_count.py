def count_atoms_in_pdb(pdb_file):
    atom_count = 0
    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith('ATOM'):
                atom_count += 1
    return atom_count



if __name__ == "__main__":
    pdb_file = '7dn3.pdb'  
    num_atoms = count_atoms_in_pdb(pdb_file)
    print("Number of atoms in the PDB file:", num_atoms)