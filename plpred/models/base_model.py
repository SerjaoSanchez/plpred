from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator
import pandas as pd
import numpy as np
import pickle

class BaseModel: 
    def __init__(self, estimator:BaseEstimator=RandomForestClassifier()):
        """
        Initialize the object.
        Parameters
        ----------
        estimator: BaseEstimator
            A scikit-learn estimator
        Returns
        -------
            None
        """
        self.estimator = estimator

    def fit(self, X:pd.DataFrame, y:pd.Series) -> None:
        """
        Create a Pandas DataFrame.
        Parameters
        ----------
        X: pd.DataFrame
                Features
        y: pd.Series
                Labels
        Returns
        -------
            None
        """
        
        self.estimator.fit(X, y)
  
    def predict(self, X:pd.DataFrame) -> np.array: 
        """
        Generates a prediction based on the underlying fitted model.

        Parameters
        ----------
        pd.DataFrame
            features
        Returns
        -------
        y_pred: np.array
            labels
        """
        y_pred = self.estimator.predict(X)
        return y_pred

    def validate(self, X_test:pd.DataFrame, y_test:pd.Series) -> str:
        """
        Validates the X_test and y_test data
        Parameters
        ----------
        X_test: pd.DataFrame
            features
        y_test: pd.Series

        Results
        -------
        report: str
            report with main classification metrics
        """
        y_pred = self.predict(X_test)
        return classification_report(y_test, y_pred)

    def save(self, file_path:str) -> None:
        """
        Saves a model with a serialized pickle file.
        
        Parameters
        ----------
        file_path: str
            path to the output file.
        
        Returns
        -------
            None
        """
        with open(file_path, 'wb') as handle:
            pickle.dump(self, handle)
