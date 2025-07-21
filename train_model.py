import pandas as ps
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

#  load the dataset
data = ps.read_csv('data/iris.csv')


# select all rows and all columns except the last one
x = data.iloc[:,:-1].values

# select the target column
y = data.target.values
print(y)

# split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

# evaluate the model
accuracy = model.score(x_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

# save the model
dump(model, 'model.joblib')
