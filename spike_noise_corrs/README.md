# Spike Noise Correlations Analysis

## Overview
This project investigates noise correlations between neuronal populations across different brain regions, focusing on trial-to-trial variability in spike counts.

## Directory Structure
- `inter_region_noise_corrs_setup.py`: Main script for calculating inter-region noise correlations
- `inter_region_noise_corrs_aggregate.py`: Aggregate analysis across multiple recordings
- `inter_region_noise_corrs_plot.py`: Visualization of noise correlation results
- `rolling/`: Subdirectory for rolling window correlation analyses
  - `inter_region_rolling_noise_corrs_setup.py`: Rolling window correlation calculation
  - `inter_region_rolling_noise_corrs_plots.py`: Plotting rolling window results
- `utils/`: Utility scripts for data processing
- `population_noise_corrs/`: Analysis of population-level noise correlations

## Key Analyses
1. Inter-region noise correlations
2. Intra-region noise correlations
3. Rolling window correlation analysis
4. Shuffled control analyses

## Dependencies
- numpy
- scipy
- pandas
- matplotlib
- xarray
- ephys_data (custom module)

## Usage
1. Prepare input data (spike recordings)
2. Run `inter_region_noise_corrs_setup.py` for initial correlation calculations
3. Use `inter_region_noise_corrs_aggregate.py` to combine results across sessions
4. Visualize results with `inter_region_noise_corrs_plot.py`

## Methodology
- Calculates Spearman correlations between neuronal spike counts
- Performs trial shuffling to establish statistical significance
- Analyzes correlations across different brain regions and tastes

## Contact
For questions, please contact the repository maintainer.
