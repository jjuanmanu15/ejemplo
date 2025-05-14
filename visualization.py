import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

from analysis import DataAnalyzer

data = pd.read_csv('adult.csv')
analize = DataAnalyzer(data)

analize.summary()
analize.correlation_matrix()
#analize.categorical_analysis()