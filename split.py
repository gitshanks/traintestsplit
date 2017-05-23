import pandas as pd
from sklearn.model_selection import train_test_split

#importing forest fire data
dataset_url = 'http://www.dsi.uminho.pt/~pcortez/forestfires/forestfires.csv'
data = pd.read_csv(dataset_url)
print data.head()

#splitting label and features
y = data.temp
X = data.drop('temp', axis=1)

#slpitting into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

print "\nX_train:\n"
print(X_train.head())
print X_train.shape

print "\nX_test:\n"
print(X_test.head())
print X_test.shape