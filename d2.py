import pandas as pd

data={
    "names":["a","b","c"],
    "marks":[10,30,10]
}

df=pd.DataFrame(data=data)


# df["marks"]=df["marks"]+5
# print(df.sort_values(by="marks"))
# print(df["marks"])

print(df["marks"].drop_duplicates())