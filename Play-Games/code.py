# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)
plt.hist(data['Rating'].dropna())
data = data[data['Rating'] <= 5]
plt.hist(data['Rating'].dropna())
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null, percent_null], axis= 1, keys= ['Total','Percent'])
print(missing_data)

data.dropna(inplace= True)

total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())

missing_data_1 = pd.concat([total_null_1, percent_null_1], axis= 1, keys= ['Total','Percent'])
print(missing_data_1)
# code ends here


# --------------

#Code starts here

catplot = sns.catplot(x= "Category", y= "Rating", data= data, kind= "box", height= 10)
catplot.set_xticklabels(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
catplot.fig

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

data['Installs'] = data['Installs'].str.replace(pat='+', repl='')
data['Installs'] = data['Installs'].str.replace(pat=',', repl='')
data['Installs'] = data['Installs'].astype('int')

encoder = LabelEncoder()
encoder.fit(data['Installs'])
data['Installs'] = encoder.transform(data['Installs'])

plt.title('Rating vs Installs [RegPlot]')
sns.regplot(x= "Installs", y= "Rating", data= data)


#Code ends here



# --------------
#Code starts here

print(data['Price'].value_counts())
data['Price'] = data['Price'].str.replace(pat='$', repl='')
data['Price'] = data['Price'].astype('float')
plt.title('Rating vs Price [RegPlot]')
sns.regplot(x= "Price", y= "Rating", data= data)

#Code ends here


# --------------

#Code starts here
# data['Genres'].unique()
data['Genres'] = data["Genres"].str.split(";", expand = True)[0]

gr_mean = data[['Genres', 'Rating']].groupby(by= 'Genres', as_index=False).mean()
gr_mean.describe()
gr_mean = gr_mean.sort_values(by= 'Rating')
print(gr_mean.iloc[0])
print(gr_mean.iloc[-1])


#Code ends here


# --------------

#Code starts here

data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()

data['Last Updated Days'] = (pd.to_datetime(max_date) - data['Last Updated']).dt.days
plt.figure(figsize=(10,10))
sns.regplot(x= 'Last Updated Days' , y= "Rating", data= data)
plt.title('Rating vs Last Updated [RegPlot]')


#Code ends here


