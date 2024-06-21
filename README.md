# Mushroom Classification

[Original Data Source](https://archive.ics.uci.edu/dataset/73/mushroom)

## Table of Contents
- [Introduction](#introduction)
- [Data Description](#data-description)
- [Model and Pipeline](#model-and-pipeline)
- [Streamlit App](#streamlit-app)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)

## Introduction

This project involves building a machine learning model to classify mushrooms as edible or not edible based on various features. The model is trained using a cleaned version of the Mushroom Dataset available at the UCI Machine Learning Repository. The final model, a Random Forest classifier, is deployed as a web application using Streamlit. You can try the app [here](https://test-et8j68owdz.streamlit.app/).

## Data Description

The dataset used for this project is a cleaned version of the original Mushroom Dataset. It contains the following 9 columns:

1. **Cap Diameter** - The diameter of the mushroom's cap.
2. **Cap Shape** - The shape of the mushroom's cap.
3. **Gill Attachment** - How the gills are attached to the stem.
4. **Gill Color** - The color of the mushroom's gills.
5. **Stem Height** - The height of the mushroom's stem.
6. **Stem Width** - The width of the mushroom's stem.
7. **Stem Color** - The color of the mushroom's stem.
8. **Season** - The season in which the mushroom was found.
9. **Target Class** - Whether the mushroom is edible (`1`) or not (`0`).

The dataset was preprocessed using various techniques such as modal imputation, one-hot encoding, z-score normalization, and feature selection to ensure optimal performance.

## Model and Pipeline

The final model chosen for this classification task is a **Random Forest** classifier due to its superior performance in terms of accuracy and robustness.

A machine learning pipeline was created to handle preprocessing steps and the model training process. This pipeline was then serialized and saved for deployment purposes.

### Key Components:

- **Preprocessing**: Modal imputation for missing values, one-hot encoding for categorical variables, and normalization of numerical features.
- **Model**: Random Forest classifier.

## Streamlit App

The Streamlit app provides an intuitive interface for users to input mushroom features and receive predictions on whether a mushroom is edible or not. 

- Try the app [here](https://test-et8j68owdz.streamlit.app/).

## Getting Started

### Prerequisites

- Python 3.7 or above
- Libraries: `pandas`, `numpy`, `scikit-learn`, `joblib`, `streamlit`

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/SiddharthGoel/MushroomBinaryClassification.git
    cd mushroom-classification
    ```

2. **Install Required Libraries**

    ```bash
    pip install -r requirements.txt
    ```

3. **Download the Dataset**

    The dataset is directly accessed via URL in the code, so no manual download is necessary.

## Usage

### Training the Model

1. **Preprocess and Train**

    Run the notebook ModelCreation.ipynb to preprocess the data and train the model. This will create and save the model pipeline in the `models` directory.

2. **Running the Streamlit App**

    Start the Streamlit app to interact with the model.

    ```bash
    streamlit run streamlit_app.py
    ```

### Predicting Mushroom Edibility

1. Visit the [Streamlit app](https://test-et8j68owdz.streamlit.app/).
2. Enter the required mushroom features.
3. Click on the `Predict` button to see the result.

## Results

The Random Forest model achieved high accuracy in predicting whether mushrooms are edible or not, making it a reliable tool for mushroom classification.
