g# clear the output of a cell
from IPython.display import clear_output
def rating_dirt (commentsScrapped):
    print(comment)
    dirt = input("C'est sale ?")
    return dirt

comments = [
    'ce resto c bobo',
    'ce resto caca'
] # from scrapping or database

# comments = connection.execute('SELECT * from comment')

labels = []
for comment in comments:
    labels.append(note_salete(comment))

print(labels)

# create a dataframe with comments and their labels

df_rate_arthur = pandas_csv("lame spots.csv", sep";", encoding = "ISO-8859-1")
# iso df_note_arthur = pandas.read_csv("lame spots.csv", sep=";", encoding ="ISO-8859-1")
del df_rate_arthur["Unnamed: 0"]
df_rate_arthur.head()

for i in df_rate_arthur.axes[0]:
    print(i)
    df_rate_arthur.at[i, 'POND1'] = dirt_rate(df_rate_arthur.Comment[i])
    clear_output()

df_rate_arthur.to_csv("lame spots (Arthur).csv", sep=";", index = False, encoding = 'utf_8')