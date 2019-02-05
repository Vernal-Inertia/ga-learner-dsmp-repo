# --------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
# code starts here
df = pd.read_csv(path)         
df.head()

y = df['list_price']
X = df.drop(columns='list_price')
X_train, X_test, y_train, y_test = tts(X, y , test_size = 0.3, random_state = 6)

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns
plt.figure(figsize=(9,9))
for i in range(len(cols)):
    plt.subplot(3,3,i+1)
    plt.scatter(X_train[cols[i]], y_train, color=plt.cm.Paired(i/10.))
    plt.xlabel('list_price')
    plt.ylabel(cols[i])
    plt.title(i)
    plt.legend(loc=2)
plt.tight_layout()
plt.show()
# code ends here



# --------------
# Code starts here
corr = X_train.corr()
print(corr)
_ = X_train.drop(columns=['play_star_rating', 'val_star_rating'], inplace=True)
_ = X_test.drop(columns=['play_star_rating', 'val_star_rating'], inplace=True)


# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(mse)
r2 = r2_score(y_test, y_pred)
print(r2)
# Code ends here


# --------------
# Code starts here
residual = y_test - y_pred
plt.hist(residual)
# Code ends here


