Distance-Based Classification Project 

## Overview
This project applies distance-based classification using different distance metrics.

##  Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/distance_classification.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. To run inside Docker:
   ```bash
   docker build -t distance_classification .
   docker run -p 8888:8888 distance_classification
   ```


##  Findings

### Clustered Faces Based on Hue and Saturation
![Clustered Faces](images/Clustered%20Faces%20Based%20on%20Hue%20and%20Saturation.png)

### K-Means Clustering of Faces Based on Hue and Saturation
![K-Means Clustering](images/K-Means%20Clustering%20of%20Faces%20Based%20on%20Hue%20and%20Saturation.png)

### Template Image Classification
![Template Image Classification](images/Template%20Image%20Classification.png)


## 🚀 Automation
- This project uses **GitHub Actions** to automatically rerun the notebook when code is updated.

## 🔗 Submission
- **GitHub Repository**: (https://github.com/saumya-a-chauhan/distance_classification)
