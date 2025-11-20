
# Methodology

This order is determined by which section outputs are needed as prerequisites for sebsequent sections. The primary example being **Literature Collection**, given how most other sections require the formulations and characteristics before proceeding. 

## Section 1 - Literature Collection (December 6th)
**Review** - This section's goal is to aquire empirical lab-tested data as a baseline for further topic exploration. 

<!-- Table for Inputs/Outputs -->
| Input | Output                                                                           |
|-------|----------------------------------------------------------------------------------|
| None  | <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> |

<!-- Table for Databases to be Used-->
| Database               | Subject | Journal |
|------------------------|---------|---------|
| Google Scholar         |         | N/A     |
| JSTOR                  |         |         |
| ScienceDirect          |         |         |
| NASA Technical Reports |         |         |
| IEEE Xplore            |         |         |

When sorting through the databases, use the following as *keywords*: Catalytic Additives, Metal Oxides, Combustion, Ammonium Perchlorate, 

When determining if a piece of literature can be used, make sure it is: 
 - [x] Ammonium Perchlorate Based
 - [ ] Contains a metal catalyst (unless pure $\text{AP}$)
 - [ ] Reports a change in enthalpy $(\Delta H)$
 - [ ] A post-1980 publication
 - [ ] Peer Reviewed / Technically Verified

For each source in the list, it will be put into a file named <span style="color: #ff6b6b; font-weight: bold;">empiricalDataset.csv</span> 

> [!WARNING]
> This file can be named anything, but from this point forward, any reference to <span style="color: #ff6b6b; font-weight: bold;">empiricalDataset</span> or <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> will be the aforementioned

## Section 2 - Computational Testing
**Review** - This section is used in testing the $4$ key softwares being analyzed for their accuracy, as shown below. Using formulation characteristics and environmental parameters generated from ***Section 1***, a data set of predicted values will be produced. 

<!-- Table for Inputs/Outputs -->
| Input                                                                            | Output                                                                            |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> | <span style="color: #4ecdc4; font-weight: bold;">Predictive Benchmark Data</span> |

| Softwares       | Formulation                                  |
|-----------------|----------------------------------------------|
| Rocket CEA (Py) | a detailed description of the question       |
| RPA Lite        | the methods you used to address the question |
| Cantera (Py)    | the definitions of any relevant terminology  |
| PROPEP 3.0      | any equations that contributed to your work  |

<!-- Psuedocode for Running Simultaneous Input Files -->
```py
import formulations from empiricalDataset
import inputProduction from propep
import inputProduction from rpaLite
import inputProduction from cantera
import inputProduction from rocketCEA



```




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


