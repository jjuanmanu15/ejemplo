import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import io

df = pd.read_csv('adult.csv')
print(df.head())

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def summary(self):
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        salida = buffer.getvalue()
        salida_describe = self.df.describe().to_string()
        salida += "\n\n" + salida_describe
        return salida

    def missing_values(self):
        return self.df.isnull()

    def imprimir():
        print()

    def correlation_matrix(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        corr = self.df[numeric_cols].corr()
        plt.figure()
        sns.heatmap(corr, annot=True, cmap='autumn')
        plt.title('Matriz de Correlación')
        plt.show()

    def categorical_analysis(self):
        categorical_cols = self.df.select_dtypes(include='object').columns
        print(f"Las columnas categoricas son: {categorical_cols}")
        column = input("Digite la columna a visualizar: ")

        if column in categorical_cols:
            plt.figure()
            sns.countplot(data=self.df, x=column, order=self.df[column].value_counts().index)
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("La columna no es categorica o está mal escrita.")

