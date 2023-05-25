import pandas as pd
import csv 

csv_file = open('scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Links','Image Links'])

# Webpage url                                                                                                               
url = 'https://swadeshplywoods.com/swadesh-flush-doors/'

# Extract tables
dfs = pd.read_html(url)


# Get first table                                                                                                           
df = dfs[-1][3]
pd.set_option('max_colwidth', 120)
print(df)
csv_writer.writerow([df])
#df.to_csv('python.csv')

# Extract columns                                                                                                           
# df2 = df[['Test Prescribed in IS: 2202 (Part-I), 1999','Minimum Value for Conformity','Observed Value']]
# print(df2)