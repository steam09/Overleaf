# Correlation Between Digital Simulations and Empirical Performance in AP-Based Composite Propellants

A computational validation study examining the accuracy of thermochemical prediction tools for solid rocket propellant design.

## 📋 Project Overview

This project investigates how computational tools predict real-world performance in Ammonium Perchlorate (AP)-based solid propellants containing metal catalytic additives. By comparing predictions from multiple simulation packages against published experimental data, this study addresses a critical gap: the lack of systematic validation frameworks for computational propellant screening.

### Research Questions

**Primary:** How accurate are computational thermochemical tools in predicting experimentally measured metrics across AP-based formulations containing various catalytic metal additives?

**Secondary:**
1. Do predictive errors correlate with specific catalyst types, concentrations, or other formulation characteristics?
2. Can atomic-scale molecular dynamics simulations reveal mechanisms that explain variance between equilibrium-based predictions and empirical observations?

## 🎯 Objectives

- **Quantify Simulation Accuracy**: Compare digital predictions (Isp, ΔH°comb) against empirical measurements across 25-40 AP-based formulations
- **Identify Predictive Patterns**: Analyze how metal additives affect prediction accuracy based on catalyst type, concentration, and formulation characteristics
- **Develop Atomic-Scale Insights**: Use LAMMPS molecular dynamics with ReaxFF force fields to model AP decomposition pathways
- **Create Correlative Framework**: Provide guidance for propellant researchers on computational tool trustworthiness

## 🔧 Methodology

### Meta-Analytical Approach
- Systematic extraction of empirical data from peer-reviewed literature
- Benchmark dataset compilation from 30+ distinct AP-based formulations
- Cross-tool validation across multiple computational platforms

### Computational Tools Evaluated
1. **NASA-CEA2** - Gibbs free-energy minimization
2. **PROPEP 3.0** - Equilibrium combustion products
3. **CPROPEP** - GNU-Octave equilibrium calculations
4. **RPA Lite** - Thermochemical analysis with nozzle design
5. **GUIPEP** - Thermochemical equilibrium interface

### Atomic-Scale Simulations
- **Platform**: LAMMPS (Large-Scale Atomic/Molecular Massively Parallel Simulator)
- **Force Field**: ReaxFF reactive potential for AP systems
- **Protocol**: NPT equilibration followed by thermal ramping (298K → 600K)
- **Analysis**: Reaction pathway identification, energy barrier calculations, intermediate species tracking

## 📊 Variables & Metrics

### Independent Variables
- Catalyst type (None, Fe₂O₃, Mg, CuO, NiO, etc.)
- Catalyst concentration (0-10% by weight)
- Computational tool selection

### Dependent Variables
- Specific Impulse (Isp) in seconds
- Heat of Combustion (ΔH°comb) in kJ/kg
- Predictive error metrics (R², RMSE, MAPE)
- Reaction mechanisms from MD simulations

### Controlled Variables
- Chamber pressure, initial temperature, expansion ratio, computational settings

## 📁 Repository Structure

```
├── data/
│   ├── literature_database/     # Compiled empirical datasets
│   ├── computational_outputs/   # Predictions from each tool
│   └── lammps_trajectories/     # MD simulation results
├── scripts/
│   ├── data_extraction/         # Literature data processing
│   ├── computational_runs/      # Tool input/output automation
│   ├── lammps_simulations/      # MD setup and analysis
│   └── statistical_analysis/    # Accuracy metrics and visualizations
├── results/
│   ├── accuracy_metrics/        # R², RMSE, MAPE calculations
│   ├── visualizations/          # Plots and heat maps
│   └── framework/               # Decision guidance documentation
├── docs/
│   ├── proposal/                # Research proposal documents
│   ├── literature_review/       # Key studies and annotations
│   └── methodology/             # Detailed procedures
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ with pandas, scipy, matplotlib
- NASA-CEA2, PROPEP 3.0, CPROPEP, RPA Lite, GUIPEP
- LAMMPS with ReaxFF force field parameters
- VMD or OVITO for trajectory visualization

### Installation
```bash
# Clone repository
git clone https://github.com/[username]/ap-propellant-validation.git
cd ap-propellant-validation

# Install Python dependencies
pip install -r requirements.txt

# Install computational tools (see docs/methodology/tool_setup.md)
```

### Usage
```bash
# Run computational predictions
python scripts/computational_runs/generate_predictions.py

# Execute LAMMPS simulations
python scripts/lammps_simulations/run_md.py

# Generate accuracy metrics
python scripts/statistical_analysis/calculate_metrics.py

# Create visualizations
python scripts/statistical_analysis/generate_plots.py
```

## 📈 Expected Outcomes

### Success Criteria
- Compilation of 30+ distinct AP-based formulations from literature
- Generated predictions for each formulation across all 5 computational tools
- Quantified accuracy metrics for each tool across the dataset
- Completed MD simulations for 3-5 representative AP-catalyst systems
- Decision framework providing quantitative guidance on computational tool reliability

### Hypotheses
1. **Tool Reliability Varies by Age**: Newer packages (RPA, NASA-CEA2) will show stronger correlation with empirical data than older tools (CPROPEP, PROPEP 3.0)
2. **Catalysts Cause Discrepancies**: Higher catalyst concentrations will show larger prediction errors, with MAPE increasing as catalyst loading increases
3. **Atomic Mechanisms Explain Deviations**: LAMMPS simulations will reveal alternative reaction pathways in catalyzed systems that correlate with prediction errors

## 🔬 Data Sources

### Primary Literature
- Journal of Propulsion and Power
- Combustion and Flame
- Propellants, Explosives, Pyrotechnics
- Thermochimica Acta

### Technical Reports
- NASA Technical Reports
- AIAA Conference Proceedings
- AFRL, DRDL Publications

### Databases
- ResearchGate, ScienceDirect, Google Scholar, JSTOR, SpringerMaterials

## 📅 Timeline

| Period | Milestone |
|--------|-----------|
| Oct 2025 | Literature review & database development |
| Nov 2025 | Complete data collection & software setup |
| Dec 2025 | Computational predictions across all tools |
| Jan 2026 | LAMMPS learning & initial simulations |
| Feb 2026 | Production MD runs & preliminary analysis |
| Mar 2026 | Statistical analysis & framework development |
| Apr 2026 | Final documentation & revision |

## 🤝 Contributing

This is a high school research project, but feedback and suggestions are welcome! Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Advisor**: Jayme Knobloch, Great Mills High School
- **Institution**: Great Mills High School STEM/AP Research Program
- **Key Studies**: Azizi et al. (2025), Yadav et al. (2021), Chu et al. (2023)

## 📧 Contact

**Student Researcher**: Trison Li  
**Institution**: Great Mills High School  
**Subject Area**: Chemistry / Materials Science

---

*This research aims to accelerate propellant development by validating computational screening tools, reducing costs, time, and hazardous exposure in solid rocket propellant formulation.*