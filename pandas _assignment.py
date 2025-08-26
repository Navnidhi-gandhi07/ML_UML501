import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, KBinsDiscretizer, OneHotEncoder, Binarizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import jaccard
from scipy.stats import pearsonr

df = pd.read_csv("AWCustomers.csv")

selected = df[['YearlyIncome','TotalChildren','MaritalStatus','Gender','NumberCarsOwned','AddressLine1']]
selected = selected.dropna()

scaler = MinMaxScaler()
selected[['YearlyIncome']] = scaler.fit_transform(selected[['YearlyIncome']])



ohe = OneHotEncoder(sparse=False, drop='first')
encoded = ohe.fit_transform(selected[['MaritalStatus','Gender']])
encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out(['MaritalStatus','Gender']))
selected = pd.concat([selected.drop(['MaritalStatus','Gender'], axis=1), encoded_df], axis=1)

std_scaler = StandardScaler()
selected[['YearlyIncome']] = std_scaler.fit_transform(selected[['YearlyIncome']])

binr = Binarizer(threshold=2)
selected['NumberCarsOwned'] = binr.fit_transform(selected[['NumberCarsOwned']])

obj1 = selected.iloc[0].values
obj2 = selected.iloc[1].values

simple_matching = np.sum(obj1==obj2)/len(obj1)
jaccard_sim = 1 - jaccard(obj1,obj2)
cosine_sim = cosine_similarity([obj1],[obj2])[0][0]

commute = df['NumberCarsOwned'].dropna().values
income = df['YearlyIncome'].dropna().values[:len(commute)]
corr, _ = pearsonr(commute, income)

print("Simple Matching Similarity:", simple_matching)
print("Jaccard Similarity:", jaccard_sim)
print("Cosine Similarity:", cosine_sim)
print("Correlation (NumberCarsOwned vs YearlyIncome):", corr)
