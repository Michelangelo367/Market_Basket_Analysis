import pandas as pd
df = pd.read_csv('groceries.csv', error_bad_lines=False)

records = []
for i in range((len(df))):
    records.append([str(df.values[i,j]) for j in range(0, df.shape[1])])

from mlxtend.preprocessing.transactionencoder import TransactionEncoder

te = TransactionEncoder()
te_data = te.fit(records).transform(records)
df = pd.DataFrame(te_data, columns = te.columns_)
df = df.drop(("nan"),axis=1)

from mlxtend.frequent_patterns import apriori

df1 = apriori(df, min_support=0.003, use_colnames = True, verbose=1)
df1.head()

from mlxtend.frequent_patterns import association_rules

rules = association_rules(df1, metric = "confidence", min_threshold = 0.2)
rules.head()

