#!/bin/bash

echo "$0 - Clean scratch files from computations"

# General
rmi -name 'core.[0-9]*'

# Q-Chem
rmi -name 'qarchive.h5'

# OpenMolcas
rmi -name '*Orb.[1-9]*'
rmi -name '*.ChVec?'

# Orca
rmi -name '*.gbw'
rmi -name '*.densities'

# Turbomole
rmi -name 'CC*--*'
rmi -name '*.cao'

# Compress any HDF5 files
#h5r

echo "*** The following big files (+100M) are left ***"
find . -size +100M
