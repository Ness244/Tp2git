import pandas
data = pandas.read_csv(r"data.csv")
tableau = data.sort_values('Carton', ascending = False).head(10)
print("####    Top 10 joueurs avec le plus de carton durant 2018    ####\n")
print(tableau)
print("\n\n")
tableau = data.groupby('club').mean(numeric_only=True).sort_values('Goals', ascending = False).head(10)
print("####    Top 10 équipe avec la meilleure moyenne de but durant 2018    ####\n")
print(tableau)