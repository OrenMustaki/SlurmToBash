Convert Slurm nodes range expression to a list of nodes
=======================================================

*Takes Slurm nodes range expression and convert it to a python list of nodes or print it.*

This script was tested using python3 3.6.3

Usage
-----
```
./SlurmToBash.py nodeA[1,3,5,12,22,24-27,29-30,33,37-40],nodeB[1,3-6,9],nodeC[1-3],nodeD1
```
```
nodeA1,nodeA3,nodeA5,nodeA12,nodeA22,nodeA24,nodeA25,nodeA26,nodeA27,nodeA29,nodeA30,nodeA33,nodeA37,nodeA38,nodeA39,nodeA40,nodeB1,nodeB3,nodeB4,nodeB5,nodeB6,nodeB9,nodeC1,nodeC2,nodeC3,nodeD1
```
```
python3 -c 'import SlurmToBash;print(SlurmToBash.convert("nodeA[1,3,5,12,22,24-27,29-30,33,37-40],nodeB[1,3-6,9],nodeC[1-3],nodeD1"))'
```
```
['nodeA1', 'nodeA3', 'nodeA5', 'nodeA12', 'nodeA22', 'nodeA24', 'nodeA25', 'nodeA26', 'nodeA27', 'nodeA29', 'nodeA30', 'nodeA33', 'nodeA37', 'nodeA38', 'nodeA39', 'nodeA40', 'nodeB1', 'nodeB3', 'nodeB4', 'nodeB5', 'nodeB6', 'nodeB9', 'nodeC1', 'nodeC2', 'nodeC3', 'nodeD1']
```

