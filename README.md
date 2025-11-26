# Neural Dynamics Analysis Suite

## Overview
This repository contains a comprehensive suite of analysis tools for investigating neural dynamics across different brain regions using electrophysiological data. The project focuses on three main areas: spike noise correlations, transition correlations, and LFP phase coherence analysis.

## Project Structure

### 📊 Core Analysis Modules

#### `spike_noise_corrs/`
Analysis of noise correlations between neuronal populations across brain regions, focusing on trial-to-trial variability in spike counts.

**Key Features:**
- Inter-region and intra-region noise correlation analysis
- Rolling window correlation analysis
- Statistical significance testing with shuffle controls
- Population-level correlation dynamics

#### `transition_corrs/`
Investigation of changepoint transitions across different brain regions and experimental conditions, analyzing temporal dynamics of neural activity.

**Key Features:**
- Changepoint detection and alignment across regions
- Inter-region transition correlation analysis
- Split-region analysis for within-region dynamics
- Variance-correlation relationship studies

#### `lfp_phase_coherence/`
Analysis of local field potential (LFP) phase coherence and phase relationships across brain regions.

**Key Features:**
- Coupled dynamics between gustatory cortex and basolateral amygdala
- Sudden, coordinated state transitions across brain regions
- Epoch-specific coherence changes
- Frequency-dependent inter-regional communication
- Exploration of attractor network dynamics in taste processing
- Analysis of trial-to-trial variability in neural responses

## Dependencies

### Core Scientific Computing
- **NumPy**: Numerical computations and array operations
- **SciPy**: Statistical analysis and signal processing
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Plotting and visualization
- **Seaborn**: Statistical data visualization

### Specialized Libraries
- **xarray**: Multi-dimensional labeled data arrays
- **joblib**: Parallel processing and caching
- **scikit-learn**: Machine learning utilities (clustering, etc.)
- **tqdm**: Progress bars for long-running computations

### Custom Modules
- **ephys_data**: Custom electrophysiology data handling module
- Provides unified interface for loading and processing neural data
- Handles spike sorting, LFP processing, and metadata management

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd neural-dynamics-analysis
```

2. Install dependencies:
```bash
pip install numpy scipy pandas matplotlib seaborn xarray joblib scikit-learn tqdm
```

3. Ensure the custom `ephys_data` module is available in your Python path.

## Usage

### Quick Start

1. **Spike Noise Correlations**:
   ```python
   # Run basic inter-region noise correlation analysis
   python spike_noise_corrs/inter_region_noise_corrs_setup.py
   
   # Aggregate results across sessions
   python spike_noise_corrs/inter_region_noise_corrs_aggregate.py
   
   # Generate plots
   python spike_noise_corrs/inter_region_noise_corrs_plot.py
   ```

2. **Transition Correlations**:
   ```python
   # Check data integrity
   python transition_corrs/all_tastes/check_data.py
   
   # Run inter-region transition analysis
   python transition_corrs/all_tastes/inter_region/run_inter_corrs.py
   
   # Aggregate and plot results
   python transition_corrs/all_tastes/inter_region/inter_corrs_aggregate.py
   ```

3. **LFP Phase Coherence**:
   ```python
   # Calculate phase coherence
   python lfp_phase_coherence/updated/lfp_coherence_aggregate.py
   
   # Statistical significance testing
   python lfp_phase_coherence/updated/lfp_coherence_sig_test.py
   
   # Generate phase difference plots
   python lfp_phase_coherence/updated/lfp_phase_difference_plots.py
   ```

## Key Analysis Concepts

### Noise Correlations
- **Definition**: Trial-to-trial correlations in spike counts between neurons
- **Significance**: Reflects shared variability and potential functional connectivity
- **Methods**: Spearman correlation with shuffle controls for statistical testing

### Transition Correlations
- **Definition**: Correlations between changepoint timings across brain regions
- **Significance**: Indicates coordinated state transitions in neural dynamics
- **Methods**: Changepoint detection followed by correlation analysis of transition times

### Phase Coherence
- **Definition**: Consistency of phase relationships between LFP signals across regions
- **Significance**: Reflects oscillatory coupling and information transfer
- **Methods**: Complex-valued coherence analysis across frequency bands

## Data Requirements

### Input Data Format
- Electrophysiology recordings with spike sorting and LFP data
- Multi-region recordings with consistent timing
- Trial-based experimental design with taste/stimulus conditions
- Compatible with `ephys_data` module format

### Expected Directory Structure
```
data/
├── session1/
│   ├── spike_data.h5
│   ├── lfp_data.h5
│   └── metadata.json
├── session2/
│   └── ...
└── ...
```

## Output and Results

### Generated Artifacts
- **HDF5 files**: Processed correlation matrices and statistical results
- **Pickle files**: Aggregated DataFrames and analysis summaries
- **PNG/PDF plots**: Visualization of results and statistical summaries
- **CSV files**: Tabular results for further analysis

### Typical Workflow
1. **Data Validation**: Check data integrity and preprocessing requirements
2. **Primary Analysis**: Calculate correlations/coherence for individual sessions
3. **Aggregation**: Combine results across multiple sessions/animals
4. **Statistical Testing**: Assess significance using appropriate controls
5. **Visualization**: Generate publication-ready plots and summaries

## Advanced Features

### Parallel Processing
- Most analysis scripts support parallel processing using `joblib`
- Configurable number of cores for computational efficiency
- Progress tracking with `tqdm` for long-running analyses

### Statistical Controls
- **Shuffle Tests**: Trial shuffling to establish null distributions
- **Multiple Comparisons**: Bonferroni correction for multiple testing
- **Percentile-based Statistics**: Robust statistical inference

### Flexible Analysis Windows
- **Rolling Windows**: Time-resolved analysis of correlations and coherence
- **Custom Time Bins**: Configurable temporal resolution
- **Event-aligned Analysis**: Analysis relative to stimulus/behavioral events

## Contributing

### Code Style
- Follow PEP 8 conventions
- Use descriptive variable names
- Include docstrings for functions and classes
- Add comments for complex analysis steps

### Adding New Analyses
1. Create new subdirectory under appropriate module
2. Follow existing naming conventions
3. Include setup, aggregate, and plot scripts
4. Update relevant README files
5. Add example usage to main README

## Troubleshooting

### Common Issues
- **Memory Errors**: Reduce batch sizes or use chunked processing
- **Missing Dependencies**: Ensure all required packages are installed
- **Data Format Issues**: Verify compatibility with `ephys_data` module
- **Path Errors**: Check file paths and directory structure

### Performance Optimization
- Use parallel processing for computationally intensive analyses
- Consider data chunking for large datasets
- Monitor memory usage during aggregation steps

## Citation

If you use this code in your research, please cite:
```
[Citation information to be added]
```

## License

[License information to be added]

## Contact

For questions, issues, or contributions, please contact:
[Contact information to be added]

---

**Last Updated**: November 2025
