# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace(to_replace='-', value='Agender', inplace=True, limit=None, regex=False, method='pad')
gender_count = data['Gender'].value_counts()
gender_count.plot.bar()


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.title('Character Alignment')
alignment.plot.pie()


# --------------
#Code starts here
sc_df = pd.DataFrame(data[['Strength','Combat']])
sc_covariance = data['Strength'].cov(data['Combat'])
sc_strength = data['Strength'].std()
sc_combat = data['Combat'].std()
sc_pearson = data['Strength'].corr(data['Combat'])


ic_df = pd.DataFrame(data[['Intelligence','Combat']])
ic_covariance = data['Intelligence'].cov(data['Combat'])
ic_intelligence = data['Intelligence'].std()
ic_combat = data['Combat'].std()
ic_pearson = data['Intelligence'].corr(data['Combat'])





# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)
super_best = data[data['Total'] > total_high]
super_best_names = super_best['Name'].tolist()
print(super_best_names)


# --------------
#Code starts here

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=3, ncols=1)

data['Intelligence'].plot.box()
ax_1.set_title("Intelligence")

data['Speed'].plot.box()
ax_2.set_title("Speed")

data['Power'].plot.box()
ax_3.set_title("Power")


