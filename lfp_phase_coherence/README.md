# LFP Phase Coherence Analysis

## Overview
This directory contains scripts for analyzing local field potential (LFP) phase coherence across different brain regions.

## Key Scripts

### Processing and Setup
- `lfp_coherence_setup.py` (DEPRECATED): Previously used for initial LFP data processing
- Current processing now handled by `lfp_processing` in `ephys_data`

### Coherence Analysis
- `updated/lfp_coherence_aggregate.py`: Main script for calculating phase coherence
- `updated/lfp_coherence_sig_test.py`: Statistical testing of phase coherence
- `updated/rolling_phase_coherence.py`: Rolling window phase coherence analysis
- `updated/lfp_gamma_analysis.py`: Specific analysis for gamma frequency band

### Visualization
- `updated/lfp_phase_difference_plots.py`: Plotting phase difference distributions
- `original/lfp_coherence_plot.py`: Legacy plotting script

### Supplementary Scripts
- `lfp_phase_diff_distribution.py`: Investigating phase difference distributions
- `lfp_phase_diff_illustration.py`: Visualizing phase difference mechanisms

## Key Analysis Techniques
- Phase difference calculation
- Coherence across frequency bands
- Statistical significance testing
- Laser condition comparisons
- Rolling window analysis

## Dependencies
- NumPy
- SciPy
- Matplotlib
- Pandas
- Joblib
- Custom `ephys_data` module

## Notes
- Focuses on inter-region LFP phase dynamics
- Supports multi-region, multi-frequency analysis
- Includes both original and updated analysis approaches
