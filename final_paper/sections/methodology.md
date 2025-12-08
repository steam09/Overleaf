
Note to Mr. Stevens: Hey, so this isn't really what the assignment asks for, but I have a reason for that. To write my overall methodology, I still need to make sure I have the time constraints for the LAMMPS testing, and for that will take some more time that I don't have at the current moment (given that I am still trying to get IRB approval for this... again, sorry for the late response). But, this is, hopefully, a satisfactory level of detail that can be understood by a casual academic. As such though, it is not in IEEE format, especially with all the cuts that had to be made to fit within a general word limit. 

# Methodology

This order is determined by which section outputs are needed as prerequisites for sebsequent sections. The primary example being **Literature Collection**, given how most other sections require the formulations and characteristics before proceeding. 

## Section 1 - Literature Collection (December 6th)
**Review** - This section's goal is to aquire empirical lab-tested data as a baseline for further topic exploration. 

<!-- Table for Inputs/Outputs -->
| Input | Output                                                                           |
|-------|----------------------------------------------------------------------------------|
| None  | <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> |

<!-- Table for Databases to be Used-->
| Database                             |
|--------------------------------------|
| Google Scholar                       |
| JSTOR                                |
| ScienceDirect                        |
| (NTRS) NASA Technical Reports Server |
| IEEE Xplore                          |

When sorting through the databases, the following as *keywords* were used: Catalytic Additives, Metal Oxides, Combustion, Ammonium Perchlorate, 

When determining if a piece of literature can be used, the following was checked: 
 - [ ] Ammonium Perchlorate Based
 - [ ] Contains a metal catalyst (exception of pure Ammonium Perchlorate)
 - [ ] Reports a change in enthalpy
 - [ ] A post-1960s publication (up to 2010s for older Technicals)
    - Older data for reduced proprietary restrictions
 - [ ] Peer Reviewed / Technically Verified

For each source in the list, it will be put into a file named <span style="color: #ff6b6b; font-weight: bold;">empiricalDataset.csv</span> 

> [!WARNING]
> This file can be named anything, but from this point forward, any reference to <span style="color: #ff6b6b; font-weight: bold;">empiricalDataset</span> or <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> will be referencing the aforementioned file.

The metrics from the literature review sources being measured are the recorded:

| Inputs                   | Outputs                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| 1) Catalyst Formulation  | 1) High-Temperature Decomposition (HTD)                                 |
| 2) Catalyst wt%          | 2) Low-Temperature Decomposiiton (HTD)                                  |
| 3) Particle Size         | 3) Activation Energy                                                    |
| 4) Oxidizer-Fuel Ratio   | 4) Change in Enthalpy                                                   |
| 5) Extreneous Conditions | 5) Product Yields                                                       |
|                          | 6) Burning Rate                                                         |
|                          | 7) Specific Impulse                                                     |
|                          | 8) Pre-Exponential Factor (Only for formulations being tested in LAMMPS |

## Section 2 - Computational Testing
**Review** - This section is used in testing the 3 key softwares being analyzed for their accuracy, as shown below. Using formulation characteristics and environmental parameters generated from ***Section 1***, a data set of predicted values will be produced. 

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
    - Particle Size
    - Particle Density

> [!NOTE]
> For rocketCEA only, there is no predefined propellant for Ammonium Perchlorate-based composites, with or without catalysts. As such, it will be notated down in the same <span style="color: #ff6b6b; font-weight: bold;">predictedDataset.csv</span> document for the corresponding thermochemical properties. This will be done through: 
> 1) Elemental Composition
> 2) Formation Enthalpy
> 3) Density.
> For the other two aforementioned softwares, this limitation is not included, and as such will not be mentioned furthermore. 

For all tools, the following will be recorded in the file named **predictedDataset.csv**. 

Just as before, the warning still comes into play. 

## Section 3 - Analysis Ver. 1
**Review** -  This section will ONLY take into consideration information by the 3 intended computational tools as well as the empirical data from literature done by qualified scientists. It will be a comparison in two main forms:
1. Software-Based Statistics
   - To be more specific, it will be the comparison between softwares and their individual ability for being accurate. 
2. Formulation-Based Statistics
   - Grouping tests not by software, but by formulation characteristic and seeing if there are any obvious trends. Trends will then be used for determining stand-out formulations for LAMMPS testing. 

<!-- Table for Inputs/Outputs -->
| Input                                                                             | Output                                                                               |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span>  | <span style="color: #45b7d1; font-weight: bold;">LAMMPS Formulations</span>          |
| <span style="color: #4ecdc4; font-weight: bold;">Predictive Benchmark Data</span> | <span style="color: #eb85e6ff; font-weight: bold;">Software Error Statistics </span> |

For individual software testing (rocketCEA, Cantera, and PROPEP), the following is going to be determined:
 - R^2 (Coefficient of Determination): Variance of empirical data. Higher values means more accurate, lower is opposite. 
 - RMSE (Root Mean Square Error): The avg. magnitude of preditive errors in the units of measurements. Can given context within a real design application

For formulation-based comparisons, the following is going to be compared:
 - Catalyst Type: MAPE for the average error as a percentage of overall value. I am using MAPE instead of RMSE for the reasoning of it to normalize range spreads, otherwise one formulation holds the risk of having a higher average error purely due to chemcial characteristics, not by software performance. 
 - Catalyst Concentration: magnitude vs. concentration using the pearson correlation, because I am unstill unfamiliar with the spearman correlation due to insufficient experience. 

Then, ANOVA will be ran to check if it is a statistically significant error across the catalyst type. This will be how LAMMPS formulations are determined. 

With these values, visualizations will be made between the softwares and empirical data through scatter plots showing individual formulation differences grouped to give an overall discrepency value through averaging. Error spread will also be represented by a box-and-whisker plot to show positive or negative overprediction. 

## Section 4 - Molecular Dynamics Simulation
**Review** - The goal of this section is to use a molecular dynamics system to properly predict reaction pathways to use as an additional factor for part 5, machine learning, in determining if certain formulation characteristics hold a significance on predictive ability by the computers. 

<!-- Table for Inputs/Outputs -->
| Input                                                                            | Output                                                                          |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span> | <span style="color: #81ff61ff; font-weight: bold;">Catalysis Comparisons</span> |
| <span style="color: #45b7d1; font-weight: bold;">LAMMPS Formulations</span>      | None                                                                            |

#### What is LAMMPS?
LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) is a software (developed by Sandia National Laboratories) meant to try and replicate atomic motion and chemical reactions in scales that would resemble real life. In this case, the condition ==ReaxFF Force Fields== will be used given its ability to 1) mimic bond restructuring and 2) overall structure formation that normal equilibrium codes are inable to properly model. 

This system also holds preference over previous models (such as ab initio) with the increased timescale of 5k-10k atoms over multi-nanosecond simulations. It is a statistically averaged sample of events while still computationally feasible with the materials provided. 

ReaxFF also holds preference for Ammonium Perchlorate with common metal oxide catalysts, which ignores previous issues with de novo parameterization. 

### Protocols Used

From the formulations chosen within the first analysis, the following workflow will be produced for each of the previously mentioned. 

1. A simulation cell using around 6k-8k atoms for current testing purposes and time constraints. The catalysts will be homogeneously mixed within the crystalline matrix to mimic real purposes. Of course, with the contraints of empirical production, this would not be realistic, but it is to try and replicate perfect scenarios. 
2. A structural relaxtion phase will be set up to then have the more realistic mixture with a constant pressure/temperature model going at standard values (298 K w/ 1 atm). This will be ran for 50-100 picoseconds given previous literature following the same ideals. 
3. The heating ramp will be ran from 298K --> 600K by 1 to 2 kelvin per picosecond ran. This matches previous heating rates in DSC/TGA studies used). For more information on DSC/TGA, that will not be mentioned as it is out of the scope of this study, but the referenced papers can be supplied for context. The sim will run for 2 to 5 nanoseconds depending on results for decomposition cascades. By the standard of the ReaxFF manual, it will be going in 0.25 fs steps to maintain overall stability. 
4. The atomic coordinates and relative ratios of intermediate/outputted products will be documented for an inference of decomposition pathways taken by the formulation. Atomic coordinates will be tracked every 1 picosecond, while species %s recorded every 0.1 ps for accuracy measures. 

### Analysis
The primary output, as stated above, will be the descriptors of decomposition mechanisms for individual formulation features. 

Using OVITO (due to previous experience with the software), this is a way to easily see what is actually happening outside of the graph, and will be part of the later analysis. Things such as the breaking of N-H or Cl-O bonds from the Ammonium Perchlorate breaking, the order in which larger molecular groupds appear, to the overall pathways that the decomposition rate takes (and that what relative frequency). It will be quantified as relative abundance metrics as one of the numerical features to distinguish performance between different formulation categories. 

For futures analysis, the interactions between uncatalyzed Ammonium Perchlorate and the catalyst will be reviewed for the surface adsorption strength (strength between the impact of the catalyst and original uncatalyzed performance). 

These three values will be summed up into more quantitative values, such as the decomposition onset temperature released over the reaction, the amount of time it took, and well as the energy profile in determining if the equilibrium code lined up with the simulation amount of energy outputted. 

## Section 5 - Machine Learning in Developing CRI
**Review** - To set up a function that can output a general accuracy score combining kinetic metrics, decomposition pathways, and formulation characteristics. With a dataset of about 90 formulation pairs (~30 formulations w/ 3 softwares), it will cover catalyst type, concentration, particle sizes, tool type, and any LAMMPS metrics. 

<!-- Table for Inputs/Outputs -->
| Input                                                                                | Output                                                            |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span>     | <span style="color: #ffcd60ff; font-weight: bold;">ML Data</span> |
| <span style="color: #eb85e6ff; font-weight: bold;">Software Error Statistics </span> |                                                                   |
| <span style="color: #4ecdc4; font-weight: bold;">Predictive Benchmark Data</span>    |                                                                   |

The goal, as for the CRI, is to give a predictive error value through the percent error formula found in many forms of science. 

For the choice of model, this research will be using the random forest model for the following reasons:
1. Small datasets (only 90) and the feasibility of still giving good models
2. A mixed categorial and continuous features list
3. Non-linear relationships and potential points of error within individual values, especially in the literature
4. Importance rankings reports in identifying variables that matter the most
5. Experience with the software

The training will go through four main phases: Data prep, parameter tuning, overall evaluation, and feature ranking.
1. The 90 points of data will be randomly selected to be split into two categories. One containing 80% (72 cases), and the other 20% (18 cases). The continuous features will be standardized into one large same scale to reduce individual changes from characteristics of formulations. 
2. A cross-validation test will be used to figure out the number of trees, tree depth, and samples per split node. The reason we are using a 5-point combo is for consistency testing to make sure the model didn't just get lucky with a random set of data. This will, in theory, give a set of parameters that is 1) close to reality, but also 2) works on any future data that matches the previous sets. 
3. An evaluation of the overall model with the same 3 metrics, R^2, RMSE, and MAPE (variance, average prediction error, and percentage-based error respectively). 
4. To use SHAP in ranking what features most influence predictive error (type, concentration, or pathway). 

To give more of an explanation of step 2, here it is:
A 5-fold cross-validation technique is a way to decide what parameter sets we will use upfront. More trees could be better predictions, but very slow. Deeper trees can capture many patters, but overfit to this data, and thus be unusable for future predictions. And splitting trees can cover a larger range, but also lead to tiny points of reference for the model. 

It will be through splitting the 80% into 5 groups (of 14-15). Then, groups 1-4 will be trained and configued for the parameters. Group 5 will be tested on this, and thus an error score. Then, we will train on groups 1, 2, 3, and 5, then use that for testing group 4. We will iterate till all groups have been the tested group once. This is different from the 20% that was unusued earlier, as that is for the final error metric. It is not testing all combinations, as that is overkill for this level of measure. 


## Section 6 - Analysis Ver. 2
**Review** -  To synthesize all outputs from previous sections for the hybrid correlation framework and establishing a Computational Reliability Index for propellant design in the industry. 

<!-- Table for Inputs/Outputs -->
| Input                                                                                | Output                      |
|--------------------------------------------------------------------------------------|-----------------------------|
| <span style="color: #ff6b6b; font-weight: bold;">Empirical Benchmark Data</span>     | CRI Validation              |
| <span style="color: #81ff61ff; font-weight: bold;">Catalysis Comparisons</span>      | Framework Decision Tree     |
| <span style="color: #eb85e6ff; font-weight: bold;">Software Error Statistics </span> | Documentation for Practices |
| <span style="color: #ffcd60ff; font-weight: bold;">ML Data</span>                    |                             |

To develop a CRI value, the random forest error predictions from the machine learning tests will be normalized. As of current, the CRI index will be from the following formula: CRI = 1 - (MAPE Prediction / MAPE Baseline). Baseline values will be the worst-case from the first analysis, while the predicted index will be scaled between a 0 to 1 range for overall consistency. From this, and further research, thresholds will be developed to give relative confidence for future propellant design based upon the importance of certain factors made also from the machine learning data. 

In establishing the difference between atomistic mechanisms and predictive failures, LAMMPS pathways will be cross-referenced with error magnitudes to a statistical significance. Factors such as certain compound changes (proton-transfer vs electron transfer) or certain intermediates correlate with higher code errors from the Pearson correlation value. 

As stated within the ML Data, the random forest model will identify the primary accuracy changes (type, concentration, particle size, or just softwares) that influence the data. Thigns such as interaction effects (catalyst-tool pairs) or threshold effects (concentration values that wildly degraded accuracy) will be compared into quantifiable insights to be documented. 

For the un-used 20% data within the machine learning, this will be the aftermath of the 5-fold cross-verification strategy for making sure the metrics stated by the model are reliable enough. This will also use paired t-tests for comparing corrected vs uncorrect predictions, 95% confidence intervals for CRI values, and sensitivity analysis on the model. 
