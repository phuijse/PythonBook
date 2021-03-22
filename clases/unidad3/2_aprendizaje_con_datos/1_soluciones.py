from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import plot_confusion_matrix


clf = GaussianNB(priors=py) 
clf.fit(x, y)

fig, ax = plt.subplots(figsize=(5, 3), tight_layout=True)

plot_confusion_matrix(clf,x, y, 
                      ax=ax, display_labels=np.array(['Benigno', 'Maligno']), 
                      cmap=plt.cm.Blues, normalize=None);