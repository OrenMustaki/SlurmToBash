Convert Slurm nodes range expression to a list of nodes
=======================================================

*Takes Slurm nodes range expression and convert it to a python list of nodes or print it as a seperated list of nodes.*

This script was tested using python3 3.6.3

Usage
-----
```
./SlurmToBash.py nodeA[3,12,22-23,27],nodeB[1,3-4,9],nodeD1
```
Will result in
```
nodeA3,nodeA12,nodeA22,nodeA23,nodeA27,nodeB1,nodeB3,nodeB4,nodeB9,nodeD1
```
```
python3 -c 'import SlurmToBash;print(SlurmToBash.convert("nodeA[3,12,22-23,27],nodeB[1,3-4,9],nodeD1"))'
```
Will result in
```
['nodeA3', 'nodeA12', 'nodeA22', 'nodeA23', 'nodeA27', 'nodeB1', 'nodeB3', 'nodeB4', 'nodeB9', 'nodeD1']
```

