# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)

data['Gender'].replace(to_replace='-',value='Agender',inplace=True)

gender_count = data['Gender'].value_counts()

gender_count.plot(kind='bar')


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot(kind='pie')
plt.title('Charater Alignment')


# --------------
#Code starts here
sc_df = data.loc[:,['Strength','Combat']]

sc_covariance = sc_df.cov().loc['Strength','Combat']

sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()

sc_pearson = sc_covariance/(sc_strength*sc_combat)

ic_df = data.loc[:,['Intelligence','Combat']]

ic_covariance = ic_df.cov().loc['Intelligence','Combat']

ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance/(ic_intelligence*ic_combat)



# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)

super_best = data[data['Total']>total_high]

super_best_names = list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3,ncols=1,figsize=(15,10))
plt.show()
ax_1=plt.boxplot(data['Speed'])
plt.title('Speed')
plt.show()
ax_2=plt.boxplot(data['Intelligence'])
plt.title('Intelligence')
plt.show()
ax_3=plt.boxplot(data['Power'])
plt.title('Power')
plt.show()


