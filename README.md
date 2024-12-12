This repository contains the code for a machine learning project focused on building and evaluating various models on a tic-tac-toe dataset. The project involves implementing classifiers and regressors using libraries such as `pandas`, `numpy`, and `scikit-learn`, and demonstrates how these models can be used to predict optimal moves in a tic-tac-toe game.

## overview

This project implements several machine learning models to classify and predict outcomes in a tic-tac-toe game. The dataset includes final board states, optimal single moves, and optimal multiple moves. The models are evaluated based on their accuracy and root mean square error (RMSE).

## Implementation Details

The code is implemented in a Jupyter notebook and includes the following steps:
1. **Data Import and Processing**: Using `pandas` and `numpy` to handle the tic-tac-toe data.
2. **Model Building**: Implementing and training the following models:
   - Classifiers: Linear SVM, K-Nearest Neighbors (KNN), and Multilayer Perceptron (MLP).
   - Regressors: KNN, MLP, and Linear Regression.
3. **Model Evaluation**: Evaluating the models using metrics such as accuracy and RMSE.
4. **Saving Models**: Using the `joblib` library to save the trained regression models for use in a command line tic-tac-toe game.

## Evaluation Results

### Classifiers
- **MLP**: 
  - Accuracy: 99% (final board state data), 91% (single move data)
- **KNN**: 
  - Accuracy: ~100% (final board state data), 86% (single move data)
- **SVM**: 
  - Accuracy: 98% (final board state data), 82% (single move data)

### Regressors
- **MLP**: 
  - Accuracy: 83%, RMSE: 0.1673
- **KNN**: 
  - Accuracy: 69%, RMSE: 0.2838
- **Linear Regression**: 
  - Accuracy: 0%, RMSE: 0.464



 ## how to run the code
To run the code, ensure you have Python installed along with the necessary libraries. Follow these steps:

1. Clone this repository:

    git clone https://github.com/abdulhakim233/Tic-Tac-Toe.git
    cd Tic-Tac-Toe 
    ```

2. Install the required libraries:
    ``
    pip install pandas numpy scikit-learn matplotlib 
    ```

3. Open on the Jupyter notebook or any code editor you want 
  

4. Run the cells in the notebook to train and evaluate the models.

## Known Issues

- The multi-output linear regression model currently has an accuracy of zero. 
- Due to computational limitations, the number of iterations for the MLP model is restricted, potentially affecting its performance.

