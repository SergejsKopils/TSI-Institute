This reposity contains homework for the python-based "Data Mining" course, presented for master students of Transport and Telecommunication Institute through collaboration with the University of the West of England (UWE Bristol).

# Computer Practice 2. California Housing Clustering Analysis


## Overview
This project performs clustering analysis on the California housing dataset to identify distinct market segments based on housing characteristics and economic factors. Both hierarchical and K-means clustering methods were applied on original and scaled data to explore the natural groupings in the dataset.

## Data
- Dataset: California Housing Dataset (housing metrics such as total rooms, median income, median house value, population, households, etc.)
- Preprocessing: Features were standardized (zero mean, unit variance) for improved clustering performance.

## Methods
- Clustering Algorithms:
  - K-Means clustering with k = 2, 3, 4
  - Hierarchical clustering (Ward, average linkage)
- Evaluation:
  - Elbow method (Sum of Squared Errors)
  - Silhouette scores

## Results
- Clusters differentiate regions by total rooms, median income, median house value, population, and households.
- Scaling data improved cluster separation and revealed more subtle differences.
- Optimal cluster number for K-means on scaled data was found to be 4.

## Visualizations
- Boxplots for key variables across clusters
- Cluster comparison on original and normalized datasets

## How to Run
1. Load the California housing dataset.
2. Run preprocessing scripts to scale features.
3. Execute clustering notebooks/scripts.
4. Visualize results with provided plotting scripts.

## Dependencies
- Python 3.x
- pandas
- scikit-learn
- matplotlib
- seaborn


