## The programming model

* [2015/09/25]

### Overall structure

It has the following directory structure as an example:

    bookfair
     ├── SimpleShareLogic
     │   └── simple
     │       ├── control
     │       │   └── control1.txt     
     │       ├── input
     │       │   ├── groups.txt     
     │       │   └── contexts
     │       │       ├── default2.conf
     ...
     │       │       └── g7c84.json
     │       └── output
     │           ├── configs
     │           ├── reports     
     │           └── results
     └── readme.md


### Directories 

1. baseDirectory: `/Users/smcho/Desktop/code/ContextSharingSimulation/experiment/simulation`
    * This is the directory where all the simulation files are located

Under the baseDirectory, we have three names to identify the simulation.

2. The simulation name: `open_air_book_fair`
3. Strategy name: `SimpleShareLogic`
4. Id: `simple`
    * It's the name of the test we are under
5. Control: `control`
    * This directory provides the configurations that the simulation is executed with 

### control.txt files

Config directory contains a configuration file `control.txt`, this configuration contains the information to generate `c.txt` 
that will be the input to the simulator. 

    transmitRange = 50
    endTime = 10000
    iteration = 1

### Output directories

* results - This is where the SIMULATION results are stored in JSON format
* configs - This is where the ONE simulator configuration is dynamcially generated
* reports - This is where the Analysis results are stored in JSON format

#### Results directory

The JSON file name is based on values in control file values + summaryType.



