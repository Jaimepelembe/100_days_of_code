from prettytable import PrettyTable

table=PrettyTable()
table2=PrettyTable()
tableFields=["City name","Area","Population","Annual Rainfall"]
table.field_names=tableFields
table2=table.copy()
listContent=[
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne Mabajiana Namina", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4]
]

# Add row by row
for element in listContent:
    table.add_row(element)
    #print(f"Elemento: {i}")

    

# Add all rows at once
table2.add_rows(listContent)


print(table)
print("Segunda tabela:")
print(table2)

#Pokemon table

tablePokemon=PrettyTable()
pokemonNames=["Pikachu","Squirtle","Charmander"]
pokemonTypes=["Electric","Water","Fire"]

#Add the column Pokemon Name
tablePokemon.add_column("Pokemon Name",pokemonNames)

#Add the column Type
tablePokemon.add_column("Type",pokemonTypes)
print("\nPikachu table")
tablePokemon.align="r"
tablePokemon.header_style="upper"
#tablePokemon.border=False
print(tablePokemon)



# Reading from csv file

from prettytable import from_csv
fp= open("salesData.csv","r")
tableSales = from_csv(fp)
fp.close()

print(type(tableSales))
print(tableSales)