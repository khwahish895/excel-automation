import matplotlib.pyplot as plt


def generate_chart(df, column):
    plt.figure()
    df[column].value_counts().plot(kind='bar')
    plt.title(f"{column} Distribution")
    plt.tight_layout()
    plt.savefig("output/chart.png")
    plt.close()
