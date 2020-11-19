from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

budget_ix, popularity_ix, runtime_ix = 0, 1, 2

class AttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_new_attributes=True): # no *args or **kargs
        self.add_new_attributes = add_new_attributes
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        budget_to_popularity = X[:, budget_ix] / X[:, popularity_ix]
        budget_to_runtime = X[:, budget_ix] / X[:, runtime_ix]
        return np.c_[X, budget_to_popularity, budget_to_runtime]
