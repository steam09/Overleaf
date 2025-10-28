# Academia Expansion Topic / Understanding

## New Question
<span style="color:green">
Can regression-based correction factors derived from LAMMPS simulations improve the predictive accuracy of PROPEP/NASA-CEA2 outputs for catalyzed AP systems?
</span>


##  Enhancements for Rigor

### 1. Statistics Beyond Comparison

- **Applying multivariate regression and/or machine learning models** (e.g., Gaussian process regression or neural nets) to predict prediction error as a function of catalyst properties
- **Feature importance analysis** (e.g., SHAP values) identifying which formulation variables most strongly influence computational reliability
- **Including uncertainty quantifications**: Monte Carlo simulations or bootstrapping to estimate error bars on tool accuracy

### 2. Generating New Computational Data

- Running LAMMPS ReaxFF for a few nanoseconds of AP + CuO, Fe₂O₃, etc. \@ different temperatures
- Outputting reaction intermediates, decomposition rates, or heat release curves
- Fit kinetic models to the MD data (Arrhenius form: k = A·e^(-Ea/RT))
- Compare kinetic constants with the ones assumed by equilibrium models

### 3. Create a Computational Framework

**Python pipeline that can:**
- Pull literature data into a standardized format
- Run all thermochemical tools (NASA-CEA2, PROPEP)
- Calculate statistical comparisons
- Produce visual summaries (heat maps, correlations, etc.)

### 4. Field Contribution

**Example(s) Contribution:**

> "The Computational Reliability Index (CRI): a derived metric quantifying the confidence in predicted propellant performance based on catalyst chemistry, model type, and deviation history."

---

## Comparison Table:

| Current Approach | Developed Approach |
|-----------------|------------------------|
| Validating computational tool accuracy | Developing correction models or hybrid frameworks |
| Literature + meta-analysis | Computational data (LAMMPS results, derived kinetics) |
| Regression metrics | Multivariate modeling, uncertainty quantification |
| Conceptual scale-linking | Quantitative integration of molecular & equilibrium models |
| Proposal or validation | New methodology & framework |

---

## Research Questions: Before & After

### Original Version

**Primary Question:** How accurate are computational thermochemical tools in predicting empirically measured metrics across AP-based formulations containing catalytic metal additives?

**Secondary Questions:**
1. Do predictive errors correlate with specific catalyst types, concentrations, or other formulation discrepancies?
2. Is atomic-scale molecular dynamics simulation (LAMMPS w/ ReaxFF) detailed enough to reveal mechanisms that can explain the variance between equilibrium-based thermochemical predictions and empirical observation?

### Question Rewrite

**Primary Research Question:**

How can a hybrid multiscale modeling framework, integrating equilibrium thermochemistry (NASA-CEA2, PROPEP) with ReaxFF-based molecular dynamics, improve the predictive fidelity of AP-based propellant performance metrics across diverse catalytic systems?

**Secondary Research Objectives:**

1. **Quantify / model** the deviations between equilibrium-based predictions and empirical results for catalyzed AP formulations

2. **Derive kinetic and mechanistic parameters** from atomistic (ReaxFF) simulations to differ non-equilibrium correction factors applicable to thermochemical codes

3. **Develop a predictive correction model or reliability index** (Computational Reliability Index, CRI) that relates formulation characteristics (catalyst identity, concentration, particle size) to computational accuracy

4. **Validate the proposed framework** through multi-source meta-analysis and cross-software benchmarking under standardized conditions (pre-designed)

**Research Aim:**

This research aims to bridge the existing gap between atomistic reaction mechanisms and macroscopic thermochemical predictions in AP-based propellant modeling. By quantitatively linking kinetic data derived from reactive molecular dynamics simulations with equilibrium thermochemistry tools, this study seeks to establish a multiscale correction methodology that enhances predictive accuracy and provides uncertainty quantification for computational propellant design.

---

## Paper Structure

### A Multiscale Correction Framework for Equilibrium Thermochemical Predictions in Catalyzed Ammonium Perchlorate Propellants

### Introduction

1. **Problem:**
   - "Equilibrium thermochemical codes (NASA-CEA2, PROPEP) are integral for propellant design but suffer from systematic, unquantified errors in catalyzed systems due to their neglect of kinetic pathways."

2. **Gap:**
   - "Current research lacks a method to correct these errors based on first-principles chemistry."

3. **Solution:**
   - "This work introduces a hybrid framework that uses ReaxFF molecular dynamics to derive atomistically-informed correction factors, culminating in a Computational Reliability Index (CRI) to guide model trustworthiness."

### Methodology

#### 1: Meta-Data Curation & Benchmarking
Keep original plan

#### 2: Atomistic Simulation for Kinetic Insight
- Detail LAMMPS/ReaxFF protocol
- Be specific about systems (AP+CuO, AP+Fe₂O₃)
- Simulation time (e.g., 2-5 ns, or less if need be)
- Heating rates
- Kinetics
  - Monitoring the decay rate of AP as a function of temperature and fitting to an Arrhenius equation

#### 3: Hybrid Model Development
- A Gaussian Process Regressor will be trained to predict the error in NASA-CEA2's I_sp output
- **Input features:** catalyst identity (encoded), concentration, and kinetic parameters (E_a, A) derived from 2