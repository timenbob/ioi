import json, os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

# --- 1) NALOŽI PODATKE (json ali .data) ---
if os.path.exists("iris.json"):
    with open("iris.json") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
else:
    # iris.data: 5 stolpcev, brez glave
    df = pd.read_csv(
        "iris.data",
        header=None,
        names=["sepal_length","sepal_width","petal_length","petal_width","class"]
    )

# --- 2) PCA na 2 komponenti ---
X = df[["sepal_length","sepal_width","petal_length","petal_width"]].values# vzami le stevilcne atribute ker z njimi lahko nekaj pocnemo
Z = StandardScaler().fit_transform(X)#normaliziraj podatke da je smiselno
pca = PCA(n_components=2) #ustvari pca objekt  in povemo da hocemo 2 komponenti
PC = pca.fit_transform(Z) #dobimo nove podatke

df_pca = pd.DataFrame({"PC1": PC[:,0], "PC2": PC[:,1], "class": df["class"]})  # bam nova teabela podatkov
df_pca.to_json("pca_iris.json", orient="records", indent=2)
