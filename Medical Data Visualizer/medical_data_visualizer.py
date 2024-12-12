import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

df['ap_lo']=pd.to_numeric(df['ap_lo'],errors='coerce')
df['ap_hi']=pd.to_numeric(df['ap_hi'],errors='coerce')


df=df.dropna(subset=('ap_lo','ap_hi'))


# 2

df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)



df['cholesterol']=(df['cholesterol']>1).astype(int)
df['gluc']=(df['gluc']>1).astype(int)

df=df[
    (df['ap_lo'] <= df['ap_hi']) &  
    (df['height'] >= df['height'].quantile(0.025)) &  
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) & 
    (df['weight'] <= df['weight'].quantile(0.975))
]
# 3


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars=["cardio"],value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # 6
    df_cat = (
        df_cat
        .groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )
    

    # 7



    # 8
    fig = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="bar"
    ).fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    corr=df.corr()

    mask=np.triu(np.ones_like(corr,dtype=bool))



    



    # 14
    fig, ax = plt.subplots(figsize=(10,8))


    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        square=True,
        cbar_kws={"shrink":0.5},
        ax=ax
    )


    # 16
    fig.savefig('heatmap.png')
    return fig

