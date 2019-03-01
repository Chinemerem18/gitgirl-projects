import pandas as pd
movies = pd.read_csv('metadata.csv', skiprows=[30])
movies.head()
movies.loc[(movies.title =='Grumpier Old Men')]
movies_data = movies.loc[:, ['title', 'release_date', 'budget', 'revenue', 'runtime']]
movies_data
movies_data['revenue'] = pd.to_numeric(movies_data['revenue'])
movies_data.loc[((movies_data.budget < 1000000) & (movies_data.revenue > 2000000))]
