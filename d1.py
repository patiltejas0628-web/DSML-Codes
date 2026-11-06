import pandas as pd

emp={
    "name":["tejas","om,","ram","sham"],
    "age":[10,20,30,40],
    "salery":[1000,2000,3000,4000]
}

#database print
df=pd.DataFrame(emp)
# print(df)

# #one coulmn print
# print(df["salery"])

# #two coulmn print
# print(df[["name","salery"]])

# #maximum salery
# print(df["salery"].max())

# #minimum salery
# print(df["salery"].min())

# #average salery
# print(df["salery"].mean())

# #top 5 records
# print(df.head(5))

# #last 5 records
# print(df.tail(5))

# #data filtering
# print(df[df["salery"]>2000])

# #random records
# print(df.sample(2))

#all agrigation functions details
# print(df.describe())

