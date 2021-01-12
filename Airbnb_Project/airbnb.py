import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LogisticRegression
import sklearn.metrics
from sklearn.model_selection import GridSearchCV

listings_boston = pd.read_csv('listings_boston.csv')
listings_seattle = pd.read_csv('listings_seattle.csv')

listings_boston.head()

listings_seattle.head()
listings_boston.columns
max(listings_boston['price'].values, key = len)
max(listings_seattle['price'].values, key = len)

listings_boston['price'] = listings_boston['price'].apply(lambda x: x.replace('$', ''))
listings_seattle['price'] = listings_seattle['price'].apply(lambda x: x.replace('$', ''))
listings_boston['price'] = pd.to_numeric(listings_boston['price'])
listings_seattle['price'] = pd.to_numeric(listings_seattle['price'])
