# we create a function to test key words presence in a comment

def word_included(comment, word):
    comment = unicodedata.normalize('NFKD', comment).encode('ASCII', 'ignore').decode('ASCII')
"""
Return the normal form NFKD for the Unicode comment
"""
    for word in words:
        if word in comment:
            return True
    return False

NegativeWords = ["indisposé", "malade", "intoxication", "infection", "parasite", "virus", "maux", "fatigue", "fièvre", "vomi", "diarhée", "indigestion", "nausées", "sale", "hygiène", "vénéneux", "dégueulasse", "caca", "chiasse", "infame", "douteux", "barbouille", "crasse", "honteux", "suspect", "répugnant", "cracra", "dégoutant", "souillé", "louche", "mauvaise", "propre", "colique", "dysenterie", "débacle", "pourrie", "odeur", "infecte", "qualité", "déception", "désastre", "horrible", "honteux", "dégueux", "important"]

# Create a new instance of a French specific subclass
stemmer = SnowballStemer('french')
NegativeWords = [unicodedata.normalize('NFKD', i).encode('ASCII', 'ignore').decode('ASCII') for i in NegativeWords]
NegativeWordsStem = [stemmer.stem(i) for i in NegativeWords]
NegativeWordsStem = [unicodedata.normalize('NFKD', i).encode('ASCII', 'ignore').decode('ASCII') for i in NegativeWordsStem]

# Get comments related to those words
df_test = pandas.read_csv("NosCommentairesScrappes.csv", encoding = "utf-8")

# Define an anonymous function that needs additional positional arguments and pass these additional arguments using the args keyword
df_test['Sale'] = df_test['Commentaire'].apply(lambda x : word_included(str(x), NegativeWordsStem))
df_sale = df_test.query("Sale == True & Note in [1,2]")
df_sale.reset_index(drop=True, inplace=True)
print (df_sale.shape)
df_sale.head()

restau_dirty = []
for restau in df_dirty.Restau.unique(): # Returns the sorted unique elements of an array
    nb = len(df_dirty[df_sale.Resto == restau])
    if nb > 1 :
        restau_dirty.append(restau)

# Query the columns of a frame with a boolean expression
df_dirty_recurring = df_dirty.query("Restau in %s" %restau_dirty)


# drop parameter to avoid the old index being added as a column
# create a new object
df_dirty_recurring.reset_index(drop=True, inplace=True)
print("Restaurants potentiellement sales:", len(restau_dirty))
print(df_dirty_recurring.shape)