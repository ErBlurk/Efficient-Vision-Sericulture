# 1. Environment-prior pipeline

## heuristic\_self\_supervised\_semantic\_segmentation.ipynb

This notebook produces heuristic self supervised segmentation masks for three classes: **silkworm, mulberry leaves, background**.

### Inputs and outputs
The notebook expects a folder of RGB images showing silkworms on mulberry leaves with visible background. Run all cells to produce per image three class masks saved alongside the originals. Output masks are single channel images where values encode classes.

### How to use and tune
Open the notebook, set the input and output paths and run cells. Parameter values such as color thresholds, minimum object size and more are defined at the top and easy to adjust. Inspect the overlay visuals to tune thresholds for your lighting and camera setup.
