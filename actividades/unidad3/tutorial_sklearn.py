# %%
import sklearn
import numpy as np
%matplotlib ipympl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../../clases/unidad3/data/cancer.csv', index_col=0)
x, y = df.drop(columns="diagnosis").values, df["diagnosis"].replace({'M':1, 'B':0}). values
# %%
fig, ax = plt.subplots()
ax.hist(y)
# %%

# Particionar dataset
from sklearn.model_selection import train_test_split, GridSearchCV
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12345, stratify=y)

# Entrenar y calibrar clasificador
from sklearn.tree import DecisionTreeClassifier

params = {'class_weight': (None, 'balanced'), 
'criterion': ('gini', 'entropy'), 
'max_depth': range(1, 30)}

gscv = GridSearchCV(DecisionTreeClassifier(), params, cv=5)
gscv.fit(x_train, y_train)
# Evaluar 

# %%
clf = gscv.best_estimator_

from sklearn.metrics import roc_curve, roc_auc_score

fpr, tpr, thresholds = roc_curve(y_test, clf.predict_proba(x_test)[:, 1], pos_label=1)
fig, ax = plt.subplots(tight_layout=True)
ax.plot(fpr, tpr)
ax.plot([0, 1], [0, 1], ls='--')
ax.set_xlabel('FPR')
ax.set_ylabel('TPR')
# %%
