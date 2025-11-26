# Spike Noise Correlations Analysis

## Overview
This module investigates noise correlations between neuronal populations across different brain regions, focusing on trial-to-trial variability in spike counts. Noise correlations reflect shared variability between neurons and provide insights into functional connectivity and population dynamics.

## Core Concepts

### Noise Correlations
- **Definition**: Trial-to-trial correlations in spike counts between pairs of neurons
- **Biological Significance**: Indicates shared input, functional connectivity, or common modulation
- **Statistical Method**: Spearman rank correlation to handle non-normal spike count distributions

### Analysis Types
1. **Inter-region Correlations**: Between neurons in different brain regions
2. **Intra-region Correlations**: Between neurons within the same brain region
3. **Rolling Window Analysis**: Time-resolved correlation dynamics
4. **Population-level Analysis**: Aggregate correlation patterns across neuron populations

## Directory Structure

### Core Analysis Scripts
- `inter_region_noise_corrs_setup.py`: Primary correlation calculation engine
  - Computes pairwise correlations between all neuron pairs
  - Implements shuffle controls for statistical significance
  - Saves results in HDF5 format for efficient storage

- `inter_region_noise_corrs_aggregate.py`: Cross-session aggregation
  - Combines correlation results across multiple recording sessions
  - Generates population-level statistics and significance matrices
  - Creates publication-ready summary visualizations

- `inter_region_noise_corrs_plot.py`: Comprehensive visualization suite
  - Correlation heatmaps and distribution plots
  - Statistical significance overlays
  - Region-wise and taste-specific comparisons

### Specialized Analysis
- `serial_correlation_test.py`: Tests for temporal dependencies in correlations
- `rolling/`: Time-resolved correlation analysis
  - `inter_region_rolling_noise_corrs_setup.py`: Rolling window calculations
  - `inter_region_rolling_aggregate.py`: Temporal aggregation and statistics
  - `inter_region_rolling_noise_corrs_plots.py`: Dynamic correlation visualization

### Utilities
- `utils/get_file.py`: Data file management and path utilities
- Helper functions for data loading and preprocessing

## Key Features

### Statistical Rigor
- **Shuffle Controls**: Trial permutation to establish null distributions
- **Multiple Comparison Correction**: Bonferroni correction for family-wise error rate
- **Percentile-based Inference**: Robust statistical testing using empirical distributions
- **Bootstrap Confidence Intervals**: Uncertainty quantification for correlation estimates

### Computational Efficiency
- **Parallel Processing**: Multi-core computation using joblib
- **Memory Management**: Chunked processing for large datasets
- **HDF5 Storage**: Efficient data storage and retrieval
- **Progress Tracking**: Real-time progress monitoring with tqdm

### Flexible Analysis Windows
- **Custom Time Bins**: Configurable temporal resolution (default: 250ms bins)
- **Event Alignment**: Analysis relative to stimulus onset or behavioral events
- **Rolling Windows**: Sliding window analysis for temporal dynamics
- **Taste-specific Analysis**: Separate analysis for different stimulus conditions

## Methodology

### Data Preprocessing
1. **Spike Count Binning**: Convert spike times to binned count data
2. **Trial Alignment**: Align trials to stimulus onset or other events
3. **Quality Control**: Remove low-firing neurons and artifact trials
4. **Region Assignment**: Group neurons by anatomical brain region

### Correlation Calculation
1. **Pairwise Correlations**: Compute Spearman correlation for all neuron pairs
2. **Shuffle Testing**: Generate null distribution via trial permutation
3. **Significance Assessment**: Compare observed correlations to shuffle distribution
4. **Effect Size Calculation**: Quantify correlation strength relative to noise

### Statistical Analysis
1. **Population Statistics**: Mean, median, and distribution of correlations
2. **Region Comparisons**: Statistical tests between brain regions
3. **Taste Effects**: Analysis of stimulus-dependent correlation changes
4. **Temporal Dynamics**: Time-resolved correlation evolution

## Usage Examples

### Basic Inter-region Analysis
```python
# Setup and run correlation analysis
python inter_region_noise_corrs_setup.py

# Aggregate results across sessions
python inter_region_noise_corrs_aggregate.py

# Generate visualization
python inter_region_noise_corrs_plot.py
```

### Rolling Window Analysis
```python
# Time-resolved correlation analysis
python rolling/inter_region_rolling_noise_corrs_setup.py

# Aggregate temporal results
python rolling/inter_region_rolling_aggregate.py

# Plot temporal dynamics
python rolling/inter_region_rolling_noise_corrs_plots.py
```

### Custom Analysis Parameters
Key parameters can be modified in the analysis scripts:
- `bin_width`: Temporal binning resolution (default: 250ms)
- `shuffle_repeats`: Number of shuffle iterations (default: 10,000)
- `time_window`: Analysis window relative to stimulus (default: 0-2000ms)
- `min_firing_rate`: Minimum firing rate threshold for inclusion

## Output Files

### Data Products
- **Correlation Matrices**: Pairwise correlation values (HDF5 format)
- **P-value Matrices**: Statistical significance values
- **Shuffle Distributions**: Null correlation distributions
- **Metadata**: Analysis parameters and session information

### Visualizations
- **Heatmaps**: Correlation matrices with significance overlays
- **Distribution Plots**: Histograms of correlation values
- **Scatter Plots**: Correlation vs. firing rate relationships
- **Time Series**: Rolling correlation dynamics

### Summary Statistics
- **DataFrame Exports**: Tabular results for further analysis (CSV/pickle)
- **Statistical Summaries**: Mean correlations by region and condition
- **Significance Counts**: Number of significant correlations per category

## Dependencies

### Core Scientific Computing
- **NumPy**: Array operations and numerical computing
- **SciPy**: Statistical functions and hypothesis testing
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Static plotting and visualization
- **Seaborn**: Statistical data visualization

### Specialized Libraries
- **xarray**: Multi-dimensional labeled arrays for time series data
- **joblib**: Parallel processing and efficient caching
- **h5py**: HDF5 file format support
- **tqdm**: Progress bars for long computations

### Custom Dependencies
- **ephys_data**: Custom electrophysiology data handling module
  - Provides unified interface for spike and LFP data
  - Handles metadata and experimental parameters
  - Manages multi-region data organization

## Performance Considerations

### Memory Management
- Large correlation matrices can exceed available RAM
- Use chunked processing for datasets with >1000 neurons
- Consider subsampling for exploratory analysis

### Computational Scaling
- Correlation calculation scales as O(n²) with neuron count
- Shuffle testing multiplies computation by shuffle count
- Parallel processing recommended for >100 neuron pairs

### Storage Requirements
- HDF5 files can become large with extensive shuffle testing
- Consider compression options for long-term storage
- Regular cleanup of intermediate files recommended

## Troubleshooting

### Common Issues
- **Memory Errors**: Reduce batch size or number of shuffle iterations
- **Slow Performance**: Enable parallel processing and check CPU utilization
- **Missing Data**: Verify ephys_data module installation and data paths
- **Statistical Power**: Ensure sufficient trials for reliable correlation estimates

### Quality Control
- Check for neurons with extremely low firing rates
- Verify trial alignment and temporal binning
- Inspect shuffle distributions for proper null hypothesis testing
- Validate region assignments and metadata consistency

## Future Enhancements

### Planned Features
- **Network Analysis**: Graph theory metrics for correlation networks
- **Machine Learning**: Dimensionality reduction and clustering of correlation patterns
- **Cross-frequency Coupling**: Integration with LFP phase coherence analysis
- **Real-time Analysis**: Streaming correlation calculation for online experiments

### Integration Opportunities
- **Behavioral Correlates**: Link correlations to behavioral performance
- **Pharmacological Studies**: Analyze drug effects on correlation structure
- **Development Studies**: Track correlation changes across age or learning

## References

Key methodological references:
- Cohen & Kohn (2011). Measuring and interpreting neuronal correlations. Nature Neuroscience.
- Averbeck et al. (2006). Neural correlations, population coding and computation. Nature Reviews Neuroscience.
- Moreno-Bote et al. (2014). Information-limiting correlations. Nature Neuroscience.
- Mahmood et al. (2023). Coupled Dynamics of Stimulus-Evoked Gustatory Cortical and Basolateral Amygdalar Activity. Journal of Neuroscience, 43(3), 386-404. Demonstrates trial-to-trial variability and covariance in neural responses, highlighting the importance of noise correlations in understanding distributed neural network dynamics.

---

**Module Maintainer**: [Contact information]  
**Last Updated**: November 2025
