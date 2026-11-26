# Assignment 2: Daubechies Wavelet Image Compression

## Overview
Extends multi-level 2D Daubechies wavelet decomposition and reconstruction to image compression experiments, including high-frequency coefficient zeroing, compression ratio inspection, and reconstruction error visualization.

## Key Modifications from Baseline
- Replaced synthetic sine-wave test data (`sin(2*pi*(x+y))`) with image input (`lena.png`).
- Adjusted wavelet order/parameters and added high-frequency zeroing to evaluate compression trade-offs.
- Added reconstruction error visualization alongside decomposition and reconstruction views.

## Files
- `baseline_wavelet.py` — Reconstructed baseline reference script (including the synthetic sine-wave setup and initial decomposition/reconstruction flow).
- `wavelet_image_compression.py` — Modified implementation for wavelet image decomposition, compression, and error comparison.
- `report_wavelet_compression.pdf` — Course presentation slides covering methodology, modifications, and results (in Traditional Chinese).