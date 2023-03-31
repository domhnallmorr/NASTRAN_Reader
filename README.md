# NASTRAN_Reader ![python](https://img.shields.io/badge/python-3.6+-blue)

## Description
Scripts for reading NASTRAN bdf files.

Currently Support Cards:
- CBAR
- CBEAM
- CORD2R
- CTRIA3
- CQUAD
- CROD
- CSHEAR (short field only)
- FORCE
- GRAV (short field only)
- GRID
- MAT1
- MAT2 (short field only)
- MAT8
- PBAR
- PBEAM* (Assumes only 2 intermediate stations)
- PCOMP (short field only)
- PROD (short field only)
- PSHELL (short field only)

## Limitations
- Only tested with short field format
