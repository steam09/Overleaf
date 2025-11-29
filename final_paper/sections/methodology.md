
# Methodology

This order is determined by which section outputs are needed as prerequisites for sebsequent sections. The primary example being **Literature Collection**, given how most other sections require the formulations and characteristics before proceeding. 

## Section 1 - Literature Collection (December 6th)
**Review** - This section's goal is to aquire empirical lab-tested data as a baseline for further topic exploration. 

<!-- Table for Inputs/Outputs -->
| Input | Output                                                                           |
|-------|----------------------------------------------------------------------------------|
| None  | <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> |

<!-- Table for Databases to be Used-->
| Database                             | Subject | Journal |
|--------------------------------------|---------|---------|
| Google Scholar                       |         | N/A     |
| JSTOR                                |         |         |
| ScienceDirect                        |         |         |
| (NTRS) NASA Technical Reports Server |         |         |
| IEEE Xplore                          |         |         |

When sorting through the databases, the following as *keywords* were used: Catalytic Additives, Metal Oxides, Combustion, Ammonium Perchlorate, 

When determining if a piece of literature can be used, the following was checked: 
 - [ ] Ammonium Perchlorate Based
 - [ ] Contains a metal catalyst (exception of pure $\text{AP}$)
 - [ ] Reports a change in enthalpy $(\Delta H)$
 - [ ] A post-1960s publication (up to 2010s for older Technicals)
    - Older data for reduced proprietary restrictions
 - [ ] Peer Reviewed / Technically Verified

For each source in the list, it will be put into a file named <span style="color: #ff6b6b; font-weight: bold;">empiricalDataset.csv</span> 

> [!WARNING]
> This file can be named anything, but from this point forward, any reference to <span style="color: #ff6b6b; font-weight: bold;">empiricalDataset</span> or <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> will be referencing the aforementioned file.

One way to format the .csv file is to use the following column structure (this is, of course, not the only way to format, but as stated above, the column references when automating python scripts will reference these names): 

| source | formulations | metrics | conditions | notes |
|--------|--------------|---------|------------|-------|
| N/A    | N/A          | N/A     | N/A        | N/A   |

The metrics from the literature review sources being measured are the following: 
 1) High-Temperature Decomposition (HTD)
    - d
 2) Low-Temperature Decomposiiton (HTD)
    - d
 3) Activation Eenrgy ($E_a$)
    - d
 4) Change in Enthalpy $(\Delta H_c)$
    - d
 5) Product


## Section 2 - Computational Testing
**Review** - This section is used in testing the $3$ key softwares being analyzed for their accuracy, as shown below. Using formulation characteristics and environmental parameters generated from ***Section 1***, a data set of predicted values will be produced. 

<!-- Table for Inputs/Outputs -->
| Input                                                                            | Output                                                                            |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> | <span style="color: #4ecdc4; font-weight: bold;">Predictive Benchmark Data</span> |

| Softwares       | Description                                    |
|-----------------|------------------------------------------------|
| Rocket CEA (Py) | A wrapper for the NASA FORTRAN CEA Code in CLI |
| Cantera (Py)    | the definitions of any relevant terminology    |
| PROPEP 3.0      | any equations that contributed to your work    |

<!-- Psuedocode for Creating & Running Simultaneous Input Files -->
```python
# Importing functions and datasets
import formulations from empiricalDataset
import propep, cantera, rocketCEA

# Setup
STANDARD_CONDITIONS = {
    'initial_temperature': 298,     # Kelvin
    'chamber_pressure': 1000,       # psi
    'expansion_ratio': 0            # IDK MAN
}

TOOLS = {
    'PROPEP': (propepGenerate, propepRun, propepExtract), 
    'Cantera': (canteraGenerate, canteraRun, canteraExtract), 
    'rocketCEA': (ceaGenerate, ceaRun, ceaExtract)
    }

OUTPUT_FILE = 'predictiveDataset.csv'

if __name__ == "__main__":

    for formulation in formulations:
        compound = GET id FROM formulation
        
        for tool, (generate, run, extract) in TOOLS.items():
            inputFile = generate(compound, STANDARD_CONDITIONS)
            output = run(inputFile)
            predictions = extract(output)
            APPEND {compound, tool, predictions} TO OUTPUT_FILE
```
NOTE: The actual file is in the respective folder of the repository. The above is a psuedocode mimic for ease of understanding and replicability. Also, ProPEP is a GUI (Graphical User Interface) style software, which means the command line cannot directly interact. As of writing, it will either be a manual input for all formulations, or setting up a custom application that will interact with the GUI.

To use the tools, the following will be used as inputs (this will be the collective list. Not all inputs listed below will be used for each individual software). 
1. Ingredient / Formulation (Chemical Species w/ wt%)
    - Amount of Ammonium Perchlorate
    - Which catalytic additive
    - Binder/fuel (if applicable, depends on literature review): HTPB, sorbitol, other examples

2. Operation Conditions (Standardized if not Supplied)
    - Chamber Pressure (Pc)
    - Initial Temperature
    - Expansion Ratio
    - Assume sea-level Isp for Ambient Pressure

3. Properties
    - Particle Size $(\mu m)$
    - Particle Density

> [!NOTE]
> For rocketCEA only, there is no predefined propellant for Ammonium Perchlorate-based composites, with or without catalysts. As such, it will be notated down in the same <span style="color: #ff6b6b; font-weight: bold;">predictedDataset.csv</span> document for the corresponding thermochemical properties. This will be done through: 
> 1) Elemental Composition
> 2) Formation Enthalpy
> 3) Density.
> For the other two aforementioned softwares, this limitation is not included, and as such will not be mentioned furthermore. 

For all tools, the following will be recorded in the file named **predictedDataset.csv**. 



Just as before, the warning still comes into play. For future psuedocode references, the file will be set up as the following:

|formulation|


## Section 3 - Analysis Ver. 1
**Review** -  

<!-- Table for Inputs/Outputs -->
| Input                                                                             | Output                                                                               |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span>  | <span style="color: #45b7d1; font-weight: bold;">LAMMPS Formulations</span>          |
| <span style="color: #4ecdc4; font-weight: bold;">Predictive Benchmark Data</span> | <span style="color: #eb85e6ff; font-weight: bold;">Software Error Statistics </span> |


## Section 4 - Molecular Dynamics Simulation
**Review** - To run LAMMPS

<!-- Table for Inputs/Outputs -->
| Input                                                                            | Output                                                                          |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> | <span style="color: #81ff61ff; font-weight: bold;">Catalysis Comparisons</span> |
| <span style="color: #45b7d1; font-weight: bold;">LAMMPS Formulations</span>      | None                                                                            |

#### What is LAMMPS?
LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) is a software meant to try and replicate atomic motion and chemical reactions in scales that would resemble real life. In this case, the condition ==ReaxFF Force Fields== will be used given its ability to $1)$ mimic bond restructuring, and $2)$ TODO. 


## Section 5 - Machine Learning in Developing CRI
**Review** - 

<!-- Table for Inputs/Outputs -->
| Input                                                                                | Output                                                            |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span>     | <span style="color: #ffcd60ff; font-weight: bold;">ML Data</span> |
| <span style="color: #eb85e6ff; font-weight: bold;">Software Error Statistics </span> |                                                                   |


## Section 6 - Analysis Ver. 2
**Review** -  

<!-- Table for Inputs/Outputs -->
| Input                                                                                | Output                                                                     |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span>     | <span style="color: #6e6bffff; font-weight: bold;"> Final Analysis </span> |
| <span style="color: #81ff61ff; font-weight: bold;">Catalysis Comparisons</span>      |                                                                            |
| <span style="color: #eb85e6ff; font-weight: bold;">Software Error Statistics </span> |                                                                            |
| <span style="color: #ffcd60ff; font-weight: bold;">ML Data</span>                    |                                                                            |


