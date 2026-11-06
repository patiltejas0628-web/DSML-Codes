import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data={
"students":["a","b","c","d"],
"marks":[10,20,30,40]
}

df=pd.DataFrame(data=data)
sns.barplot(
    data=df,
    x="students",
    y="marks"
)

plt.show()