# Transition Correlations Analysis

## Overview
This module analyzes changepoint transitions across different brain regions and experimental conditions, focusing on understanding temporal coordination of neural state changes. The analysis investigates how brain regions synchronize their activity transitions during sensory processing and behavioral tasks.

## Core Concepts

### Changepoint Analysis
- **Definition**: Statistical detection of abrupt changes in neural activity patterns
- **Biological Significance**: Represents discrete state transitions in neural population dynamics
- **Temporal Precision**: Identifies exact timing of neural state changes with millisecond resolution

### Transition Correlations
- **Inter-region Correlations**: Coordination of changepoints between different brain areas
- **Intra-region Correlations**: Consistency of transitions within brain regions
- **Cross-trial Variability**: Analysis of transition timing reliability across experimental trials

## Directory Structure

### Main Analysis Framework (`all_tastes/`)
Comprehensive analysis across multiple taste/stimulus conditions:

#### Data Validation and Setup
- `check_data.py`: Comprehensive data integrity validation
  - Verifies spike sorting quality and completeness
  - Validates experimental metadata and timing information
  - Checks region assignments and electrode mappings
  - Generates data quality reports

- `corr_test.py`: Core statistical testing functions
  - Implements correlation significance testing
  - Provides shuffle-based null hypothesis testing
  - Handles multiple comparison corrections

#### Inter-region Analysis (`inter_region/`)
Analysis of changepoint coordination between brain regions:

- `run_inter_corrs.py`: Primary analysis engine
  - Loads changepoint models and extracts transition times
  - Calculates correlations between region transition timings
  - Implements moving window correlation analysis
  - Performs extensive shuffle controls

- `inter_corrs_aggregate.py`: Cross-session aggregation
  - Combines results across multiple recording sessions
  - Generates population-level statistics
  - Creates comprehensive visualization summaries
  - Exports results for publication

- `inter_corrs_plot.py`: Specialized visualization tools
  - Generates changepoint alignment plots
  - Creates correlation heatmaps and time series
  - Produces split-condition comparison plots

#### Split-region Analysis (`split_region/`)
Analysis of within-region transition consistency:

- `run_split_corrs.py`: Split-region correlation calculation
  - Analyzes correlations within artificially split neuron populations
  - Tests for intrinsic correlation structure
  - Provides control for inter-region comparisons

- `split_corrs_aggregate.py`: Comprehensive statistical analysis
  - Advanced statistical testing with multiple comparison correction
  - K-means clustering of correlation patterns
  - Bonferroni correction for family-wise error control
  - Generates publication-ready statistical summaries

- `split_corrs_plot.py`: Visualization of split-region results
  - Creates detailed changepoint alignment visualizations
  - Generates correlation distribution plots
  - Produces statistical significance overlays

#### Specialized Analyses
- `var_vs_corr/corr_strength_vs_tau_var.py`: Relationship between transition variability and correlation strength
- `transition_var_corr/trans_var_corr.py`: Analysis of transition variance correlations
- `intra_alltoall_aggregate.py`: Comprehensive intra-region all-to-all correlation analysis

## Key Features

### Advanced Statistical Methods
- **Changepoint Model Integration**: Compatible with Hidden Markov Models and other changepoint detection methods
- **Robust Correlation Analysis**: Spearman correlations robust to outliers and non-normal distributions
- **Extensive Shuffle Controls**: Multiple shuffle strategies to establish rigorous null hypotheses
- **Multiple Comparison Correction**: Bonferroni and other correction methods for family-wise error control

### Model Parameter Extraction
- **Automated Parameter Parsing**: Extracts model parameters from filename conventions
- **Flexible Model Support**: Compatible with various changepoint detection algorithms
- **Cross-validation Integration**: Supports model selection and validation workflows

### Computational Efficiency
- **Parallel Processing**: Multi-core computation using joblib for large-scale analysis
- **Memory Optimization**: Efficient handling of large correlation matrices
- **Progress Monitoring**: Real-time progress tracking for long-running analyses
- **Caching Support**: Intelligent caching of intermediate results

## Methodology

### Data Preprocessing
1. **Model Loading**: Load pre-computed changepoint models from HDF5 files
2. **Parameter Extraction**: Parse model parameters (states, time windows, bin width)
3. **Transition Extraction**: Extract changepoint timing from model posteriors
4. **Quality Control**: Validate model fits and exclude poor-quality sessions

### Correlation Analysis
1. **Pairwise Correlations**: Compute correlations between all region pairs
2. **Moving Window Analysis**: Time-resolved correlation dynamics
3. **Shuffle Testing**: Generate null distributions via multiple shuffle strategies
4. **Statistical Inference**: Assess significance using empirical p-values

### Advanced Analytics
1. **Clustering Analysis**: K-means clustering of correlation patterns
2. **Variance-Correlation Relationships**: Analyze how transition variability affects correlations
3. **Cross-condition Comparisons**: Statistical comparison across experimental conditions
4. **Population Dynamics**: Aggregate analysis across multiple animals/sessions

## Usage Examples

### Basic Inter-region Analysis
```python
# Validate data quality
python all_tastes/check_data.py

# Run inter-region correlation analysis
python all_tastes/inter_region/run_inter_corrs.py

# Aggregate results across sessions
python all_tastes/inter_region/inter_corrs_aggregate.py

# Generate visualizations
python all_tastes/inter_region/inter_corrs_plot.py
```

### Split-region Control Analysis
```python
# Run split-region analysis
python all_tastes/split_region/run_split_corrs.py

# Comprehensive statistical analysis
python all_tastes/split_region/split_corrs_aggregate.py

# Generate detailed plots
python all_tastes/split_region/split_corrs_plot.py
```

### Variance-Correlation Analysis
```python
# Analyze relationship between variability and correlation
python all_tastes/var_vs_corr/corr_strength_vs_tau_var.py
```

## Configuration and Parameters

### Model Parameters (extracted from filenames)
- **States**: Number of hidden states in changepoint model
- **Time Window**: Analysis window relative to stimulus onset
- **Bin Width**: Temporal resolution of analysis
- **Fit Type**: Type of model fitting procedure used

### Analysis Parameters
- **Shuffle Iterations**: Number of shuffle controls (default: 1000-10000)
- **Correlation Method**: Spearman rank correlation (robust to outliers)
- **Significance Threshold**: Alpha level for statistical testing (default: 0.05)
- **Window Size**: Moving window size for temporal analysis

## Output Products

### Statistical Results
- **Correlation Matrices**: Pairwise correlations between all region combinations
- **P-value Matrices**: Statistical significance of correlations
- **Shuffle Distributions**: Null correlation distributions for significance testing
- **Percentile Rankings**: Empirical percentile ranks of observed correlations

### Visualizations
- **Changepoint Alignment Plots**: Visualization of transition timing across regions
- **Correlation Heatmaps**: Matrix visualization of inter-region correlations
- **Time Series Plots**: Temporal dynamics of correlation strength
- **Statistical Summary Plots**: Distribution plots with significance overlays

### Data Exports
- **HDF5 Files**: Structured storage of correlation results and metadata
- **Pickle Files**: Serialized DataFrames for further analysis
- **CSV Files**: Tabular exports for external statistical software
- **Publication Figures**: High-resolution plots ready for publication

## Dependencies

### Core Scientific Computing
- **NumPy**: Numerical computing and array operations
- **SciPy**: Statistical functions and optimization
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Plotting and visualization
- **Seaborn**: Statistical data visualization

### Specialized Libraries
- **joblib**: Parallel processing and caching
- **scikit-learn**: Machine learning utilities (K-means clustering)
- **tqdm**: Progress bars for long computations
- **h5py**: HDF5 file format support

### Custom Dependencies
- **ephys_data**: Custom electrophysiology data handling
- **Changepoint Models**: Pre-computed changepoint detection results
- **Model Parameter Utilities**: Custom parameter extraction functions

## Advanced Features

### Model Integration
- **HMM Compatibility**: Seamless integration with Hidden Markov Model results
- **Flexible Model Support**: Adaptable to various changepoint detection algorithms
- **Parameter Validation**: Automatic validation of model parameters and fits

### Statistical Robustness
- **Multiple Shuffle Strategies**: Various approaches to null hypothesis generation
- **Outlier Handling**: Robust correlation methods resistant to outliers
- **Cross-validation Support**: Integration with model selection workflows
- **Effect Size Quantification**: Comprehensive effect size reporting

### Scalability
- **Large Dataset Support**: Efficient handling of multi-session, multi-animal datasets
- **Memory Management**: Optimized memory usage for large correlation matrices
- **Distributed Computing**: Support for cluster-based parallel processing
- **Incremental Analysis**: Ability to add new sessions to existing analyses

## Quality Control and Validation

### Data Quality Checks
- **Model Fit Quality**: Validation of changepoint model convergence
- **Temporal Alignment**: Verification of proper trial alignment
- **Region Assignment**: Validation of anatomical region labels
- **Statistical Power**: Assessment of sufficient data for reliable inference

### Result Validation
- **Shuffle Control Validation**: Verification of proper null hypothesis generation
- **Correlation Stability**: Assessment of result stability across subsamples
- **Cross-validation**: Model-independent validation of key findings
- **Biological Plausibility**: Sanity checks against known neurobiological principles

## Troubleshooting

### Common Issues
- **Model Loading Errors**: Verify changepoint model file paths and formats
- **Memory Limitations**: Reduce batch sizes or use chunked processing
- **Statistical Power**: Ensure sufficient trials for reliable correlation estimates
- **Parameter Extraction**: Validate filename conventions for parameter parsing

### Performance Optimization
- **Parallel Processing**: Enable multi-core computation for large analyses
- **Memory Management**: Monitor RAM usage during correlation matrix computation
- **Disk I/O**: Use SSD storage for improved file access performance
- **Caching**: Leverage joblib caching for repeated computations

## Future Developments

### Planned Enhancements
- **Real-time Analysis**: Online changepoint detection and correlation analysis
- **Machine Learning Integration**: Deep learning approaches to transition detection
- **Network Analysis**: Graph theory metrics for transition correlation networks
- **Causal Analysis**: Granger causality and other causal inference methods

### Integration Opportunities
- **Behavioral Correlates**: Link transition correlations to behavioral performance
- **Pharmacological Studies**: Analyze drug effects on transition coordination
- **Development Studies**: Track correlation changes across learning or development
- **Cross-species Comparisons**: Comparative analysis across different animal models

## References

Key methodological references:
- Escola et al. (2011). Hidden Markov models for the stimulus-response relationships of multistate neural systems. Neural Computation.
- Linderman et al. (2016). Bayesian learning and inference in recurrent switching linear dynamical systems. AISTATS.
- Nassar et al. (2019). Rational regulation of learning dynamics by pupil-linked arousal systems. Nature Neuroscience.
- Mahmood et al. (2023). Coupled Dynamics of Stimulus-Evoked Gustatory Cortical and Basolateral Amygdalar Activity. Journal of Neuroscience, 43(3), 386-404. Highlights novel inter-regional coupling and distributed neural network processing during taste stimulation, revealing sudden, coordinated transitions between gustatory cortex and basolateral amygdala.

---

**Module Maintainer**: [Contact information]  
**Last Updated**: November 2025
