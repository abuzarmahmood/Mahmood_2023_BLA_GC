# Transition Correlations Analysis

## Overview
This project analyzes changepoint transitions across different brain regions and experimental conditions, focusing on understanding temporal dynamics of neural activity.

## Key Components

### Directory Structure
- `all_tastes/`: Main analysis scripts for multi-taste experiments
  - `inter_region/`: Scripts for inter-region correlation analysis
  - `split_region/`: Scripts for analyzing split region data
  - `var_vs_corr/`: Variance and correlation relationship analysis

### Core Functionality
1. **Changepoint Detection**
   - Identify temporal transitions in neural activity
   - Compare changepoint locations across different brain regions
   - Analyze correlation and variability of transitions

2. **Statistical Analysis**
   - Compute Spearman correlations between region transitions
   - Perform shuffle tests to assess statistical significance
   - Analyze transition variability and its impact on correlations

### Key Scripts
- `check_data.py`: Data validation and preprocessing
- `corr_test.py`: Core correlation testing functions
- `inter_corrs_aggregate.py`: Aggregate inter-region correlation analysis
- `split_corrs_aggregate.py`: Analyze correlations in split region data

## Dependencies
- NumPy
- SciPy
- Pandas
- Joblib
- Matplotlib
- Seaborn
- Custom ephys_data module

## Usage
Analyze neural activity transitions across different brain regions and experimental conditions.

## Contact
Developed as part of neural dynamics research.
