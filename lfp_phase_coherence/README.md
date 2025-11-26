# LFP Phase Coherence Analysis

## Overview
This module provides comprehensive analysis tools for investigating local field potential (LFP) phase coherence and phase relationships across different brain regions. The analysis focuses on understanding oscillatory coupling, information transfer, and coordinated neural dynamics through phase-based measures.

## Core Concepts

### Phase Coherence
- **Definition**: Consistency of phase relationships between LFP signals across brain regions
- **Biological Significance**: Reflects oscillatory coupling and potential information transfer pathways
- **Frequency Specificity**: Analysis across multiple frequency bands to identify band-specific coupling
- **Dynamic Network Interactions**: Exploration of coupled neural dynamics between brain regions
- **Nonlinear Communication**: Investigation of sudden state transitions and epoch-specific coherence
- **Attractor Network Dynamics**: Analysis of distributed neural processing mechanisms

### Phase Differences
- **Inter-region Phase Differences**: Phase relationships between oscillations in different brain areas
- **Phase Distribution Analysis**: Statistical characterization of phase difference distributions
- **Temporal Dynamics**: Time-resolved analysis of phase relationship evolution

### Coherence Metrics
- **Complex Coherence**: Magnitude and phase components of coherence
- **Spectral Coherence**: Frequency-resolved coherence analysis
- **Rolling Coherence**: Time-resolved coherence dynamics

## Directory Structure

### Current Analysis Framework (`updated/`)
Modern, optimized analysis pipeline:

#### Core Coherence Analysis
- `lfp_coherence_aggregate.py`: Primary coherence calculation engine
  - Computes spectral coherence across frequency bands
  - Handles multi-region, multi-session analysis
  - Implements efficient STFT-based coherence calculation
  - Supports parallel processing for large datasets

- `lfp_coherence_sig_test.py`: Statistical significance testing
  - Implements permutation-based significance testing
  - Generates null distributions through trial shuffling
  - Provides multiple comparison correction
  - Identifies significant coherence clusters

#### Specialized Analysis
- `rolling_phase_coherence.py`: Time-resolved coherence analysis
  - Sliding window coherence calculation
  - Temporal dynamics of phase coupling
  - Event-related coherence changes
  - Statistical testing of temporal coherence patterns

- `lfp_gamma_analysis.py`: Gamma-band specific analysis
  - Focused analysis on gamma frequency range (30-100 Hz)
  - High-resolution gamma coherence mapping
  - Gamma-specific statistical testing
  - Integration with spike-gamma coupling analysis

- `lfp_phase_difference_plots.py`: Comprehensive visualization suite
  - Phase difference distribution plots
  - Coherence heatmaps and spectrograms
  - Statistical significance overlays
  - Publication-ready figure generation

### Legacy Analysis Framework (`original/`)
Original analysis pipeline (maintained for compatibility):

- `lfp_coherence_aggregate.py`: Original coherence calculation
- `lfp_coherence_aggregate_laser.py`: Laser stimulation condition analysis
- `lfp_coherence_plot.py`: Legacy visualization tools
- `lfp_coherence_setup.py`: **DEPRECATED** - Original data preprocessing
- `lfp_coherence_sig_test.py`: Original significance testing

### Specialized Investigation Scripts
- `lfp_phase_diff_distribution.py`: Deep analysis of phase difference distributions
  - Investigates phase difference patterns across regions
  - Analyzes representative electrode selection
  - Computes mean regional phase relationships
  - Generates phase difference statistics

- `lfp_phase_diff_illustration.py`: Visualization and illustration tools
  - Rose plots for circular phase data
  - Phase relationship illustrations
  - Custom plotting functions for phase analysis
  - Parallel processing utilities

## Key Features

### Advanced Signal Processing
- **Short-Time Fourier Transform (STFT)**: High-resolution time-frequency analysis
- **Complex Coherence Calculation**: Full coherence spectrum with magnitude and phase
- **Multi-taper Methods**: Robust spectral estimation with reduced variance
- **Artifact Rejection**: Automated detection and removal of electrical artifacts

### Statistical Rigor
- **Permutation Testing**: Non-parametric significance testing through trial shuffling
- **Cluster-based Statistics**: Correction for multiple comparisons across frequency and time
- **Bootstrap Confidence Intervals**: Uncertainty quantification for coherence estimates
- **False Discovery Rate Control**: Advanced multiple comparison correction methods

### Frequency Band Analysis
- **Delta (1-4 Hz)**: Slow oscillations and sleep-related rhythms
- **Theta (4-8 Hz)**: Hippocampal theta and navigation-related oscillations
- **Alpha (8-12 Hz)**: Sensorimotor and attention-related rhythms
- **Beta (12-30 Hz)**: Motor control and cognitive processing
- **Gamma (30-100 Hz)**: High-frequency coupling and local processing
- **High Gamma (100+ Hz)**: Ultra-fast oscillations and spike-field coupling

### Temporal Resolution
- **Event-locked Analysis**: Coherence relative to stimulus or behavioral events
- **Rolling Window Analysis**: Continuous temporal dynamics
- **Pre/Post Comparisons**: Statistical comparison across experimental epochs
- **Long-term Dynamics**: Analysis of coherence changes across extended recordings

## Methodology

### Data Preprocessing
1. **LFP Extraction**: Load continuous LFP data from multi-electrode recordings
2. **Filtering**: Band-pass filtering for specific frequency ranges
3. **Artifact Removal**: Automated detection and interpolation of artifacts
4. **Referencing**: Common average referencing or bipolar derivations
5. **Trial Segmentation**: Epoch data relative to experimental events

### Coherence Calculation
1. **STFT Computation**: Short-time Fourier transform for time-frequency decomposition
2. **Cross-spectral Density**: Calculate cross-power between electrode pairs
3. **Coherence Estimation**: Normalize cross-power by auto-power spectra
4. **Statistical Testing**: Permutation-based significance assessment
5. **Multiple Comparison Correction**: Control for family-wise error rate

### Phase Analysis
1. **Phase Extraction**: Extract instantaneous phase from analytic signal
2. **Phase Difference Calculation**: Compute inter-region phase differences
3. **Circular Statistics**: Apply circular statistical methods for phase data
4. **Phase Coupling Metrics**: Calculate phase-locking value and other coupling measures

## Usage Examples

### Basic Coherence Analysis
```python
# Run primary coherence analysis
python updated/lfp_coherence_aggregate.py

# Statistical significance testing
python updated/lfp_coherence_sig_test.py

# Generate phase difference plots
python updated/lfp_phase_difference_plots.py
```

### Gamma-specific Analysis
```python
# Focused gamma band analysis
python updated/lfp_gamma_analysis.py
```

### Time-resolved Analysis
```python
# Rolling window coherence
python updated/rolling_phase_coherence.py
```

### Phase Distribution Investigation
```python
# Detailed phase difference analysis
python lfp_phase_diff_distribution.py

# Generate phase illustrations
python lfp_phase_diff_illustration.py
```

### Legacy Analysis (if needed)
```python
# Original analysis pipeline
python original/lfp_coherence_aggregate.py

# Laser condition analysis
python original/lfp_coherence_aggregate_laser.py
```

## Configuration Parameters

### Frequency Analysis
- **Frequency Range**: Customizable frequency bands for analysis
- **Frequency Resolution**: STFT parameters for spectral resolution
- **Overlap**: Window overlap for temporal resolution
- **Taper Parameters**: Multi-taper settings for spectral estimation

### Statistical Testing
- **Permutation Count**: Number of shuffle iterations (default: 1000)
- **Significance Threshold**: Alpha level for statistical testing (default: 0.05)
- **Cluster Threshold**: Minimum cluster size for cluster-based correction
- **Multiple Comparison Method**: Choice of correction method (Bonferroni, FDR, etc.)

### Temporal Parameters
- **Window Size**: Analysis window duration (default: 500ms)
- **Step Size**: Sliding window step size (default: 50ms)
- **Baseline Period**: Pre-stimulus baseline for normalization
- **Analysis Epoch**: Post-stimulus analysis window

## Output Products

### Coherence Results
- **Coherence Matrices**: Frequency-resolved coherence between all electrode pairs
- **Phase Matrices**: Phase relationships between electrode pairs
- **Significance Maps**: Statistical significance of coherence values
- **Time-frequency Maps**: Spectrograms of coherence evolution

### Statistical Results
- **P-value Maps**: Statistical significance across frequency and time
- **Confidence Intervals**: Bootstrap confidence bounds for coherence
- **Effect Sizes**: Quantification of coherence strength
- **Cluster Statistics**: Significant coherence clusters with spatial extent

### Visualizations
- **Coherence Heatmaps**: Matrix visualization of inter-region coherence
- **Spectrograms**: Time-frequency coherence evolution
- **Phase Plots**: Rose plots and circular histograms for phase data
- **Statistical Overlays**: Significance masks on coherence plots

### Data Exports
- **HDF5 Files**: Structured storage of coherence results and metadata
- **MAT Files**: MATLAB-compatible exports for further analysis
- **CSV Files**: Tabular exports of summary statistics
- **Figure Files**: High-resolution publication-ready plots

## Dependencies

### Core Scientific Computing
- **NumPy**: Numerical computing and array operations
- **SciPy**: Signal processing and statistical functions
- **Matplotlib**: Plotting and visualization
- **Pandas**: Data manipulation and analysis

### Signal Processing
- **MNE-Python**: Advanced neurophysiology signal processing (optional)
- **Nitime**: Time series analysis for neuroscience (optional)
- **PyWavelets**: Wavelet analysis tools (optional)

### Specialized Libraries
- **joblib**: Parallel processing and caching
- **h5py**: HDF5 file format support
- **tqdm**: Progress bars for long computations

### Custom Dependencies
- **ephys_data**: Custom electrophysiology data handling module
  - Provides LFP data loading and preprocessing
  - Handles multi-electrode array data organization
  - Manages experimental metadata and timing information

## Advanced Features

### Multi-region Analysis
- **All-to-all Coherence**: Comprehensive coherence mapping between all region pairs
- **Network Analysis**: Graph theory metrics for coherence networks
- **Hierarchical Analysis**: Multi-level analysis from electrodes to regions to systems
- **Cross-frequency Coupling**: Analysis of coupling between different frequency bands

### Experimental Condition Comparisons
- **Taste-specific Analysis**: Coherence differences across stimulus conditions
- **Laser Stimulation Effects**: Analysis of optogenetic manipulation effects
- **Behavioral State Comparisons**: Coherence during different behavioral epochs
- **Learning-related Changes**: Coherence evolution across training sessions

### Quality Control
- **Artifact Detection**: Automated identification of electrical and movement artifacts
- **Signal Quality Assessment**: Quantification of signal-to-noise ratio
- **Electrode Validation**: Assessment of electrode impedance and recording quality
- **Statistical Power Analysis**: Determination of sufficient data for reliable estimates

## Performance Considerations

### Computational Efficiency
- **Parallel Processing**: Multi-core computation for large electrode arrays
- **Memory Management**: Efficient handling of large time-frequency matrices
- **Chunked Processing**: Analysis of large datasets in manageable chunks
- **Caching**: Intelligent caching of intermediate results

### Storage Requirements
- **Raw Data**: LFP data can be several GB per session
- **Processed Results**: Coherence matrices scale with electrode count squared
- **Compression**: HDF5 compression for efficient storage
- **Archival**: Long-term storage strategies for large datasets

### Scalability
- **Multi-session Analysis**: Batch processing across multiple recording sessions
- **Cross-animal Studies**: Population-level analysis across multiple subjects
- **Longitudinal Studies**: Analysis of coherence changes over time
- **High-density Arrays**: Support for hundreds of electrodes

## Troubleshooting

### Common Issues
- **Memory Errors**: Reduce frequency resolution or use chunked processing
- **Slow Performance**: Enable parallel processing and optimize STFT parameters
- **Artifact Contamination**: Improve artifact detection and removal procedures
- **Statistical Power**: Ensure sufficient trial count for reliable coherence estimates

### Quality Control Checks
- **Signal Quality**: Verify LFP signal quality and electrode impedances
- **Temporal Alignment**: Ensure proper synchronization across channels
- **Frequency Artifacts**: Check for line noise and other electrical artifacts
- **Statistical Validity**: Validate shuffle procedures and significance testing

## Future Enhancements

### Planned Features
- **Real-time Coherence**: Online coherence calculation for closed-loop experiments
- **Machine Learning Integration**: Deep learning approaches to coherence analysis
- **Cross-species Analysis**: Comparative coherence analysis across animal models
- **Clinical Applications**: Translation to human electrophysiology data

### Integration Opportunities
- **Spike-field Coupling**: Integration with spike train analysis
- **Behavioral Correlates**: Link coherence to behavioral performance measures
- **Pharmacological Studies**: Analysis of drug effects on oscillatory coupling
- **Computational Modeling**: Integration with neural network models

## References

Key methodological references:
- Bastos & Schoffelen (2016). A tutorial review of functional connectivity analysis methods and their interpretational pitfalls. Frontiers in Systems Neuroscience.
- Cohen (2014). Analyzing Neural Time Series Data: Theory and Practice. MIT Press.
- Fries (2015). Rhythms for cognition: communication through coherence. Neuron.
- Vinck et al. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. NeuroImage.

---

**Module Maintainer**: [Contact information]  
**Last Updated**: November 2025
