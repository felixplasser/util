#!/bin/bash

echo "$0 - Clean scratch files from computations"

# OpenMolcas
rmi -name '*Orb.?'
h5r

# Orca
rmi -name '*.gbw'
rmi -name '*.densities'

# Turbomole
rmi -name 'CC*'
rmi -name '*.cao'
