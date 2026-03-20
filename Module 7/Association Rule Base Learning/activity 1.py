import pandas as pd 

from mlxtend.frequent_patterns import apriori, association_rules 
dataset = pd.read_csv('customers.csv')

frequent_itemsets = apriori(dataset, min_support=0.01, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

frequent_itemsets[(frequent_itemsets['length'] == 2)& (frequent_itemsets['support'] >= 0.05)]

frequent_itemsets[(frequent_itemsets['length'] ==3)].head()