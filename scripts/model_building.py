# Import necessary libraries
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
import shap  # Import SHAP for model interpretation

def linear_regression(X_train, y_train, X_test, y_test):
    model = LinearRegression()  # Initialize the Linear Regression model
    model.fit(X_train, y_train)  # Fit the model to the training data
    predictions = model.predict(X_test)  # Make predictions on the test set
    mse = mean_squared_error(y_test, predictions)  # Calculate mean squared error
    return model, mse  # Return the trained model and the error


def random_forest(X_train, y_train, X_test, y_test):
    model = RandomForestRegressor(random_state=42)  # Initialize the Random Forest model
    model.fit(X_train, y_train)  # Fit the model to the training data
    predictions = model.predict(X_test)  # Make predictions on the test set
    mse = mean_squared_error(y_test, predictions)  # Calculate mean squared error
    return model, mse  # Return the trained model and the error

 
def xgboost_model(X_train, y_train, X_test, y_test):
    model = XGBRegressor(random_state=42)  # Initialize the XGBoost model
    model.fit(X_train, y_train)  # Fit the model to the training data
    predictions = model.predict(X_test)  # Make predictions on the test set
    mse = mean_squared_error(y_test, predictions)  # Calculate mean squared error
    return model, mse  # Return the trained model and the error


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)  # Make predictions on the test set
    mse = mean_squared_error(y_test, predictions)  # Calculate mean squared error
    r2 = r2_score(y_test, predictions)  # Calculate R² score
    return {"mse": mse, "r2": r2}  # Return the evaluation metrics


