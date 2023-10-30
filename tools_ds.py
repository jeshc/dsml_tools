
import matplotlib.pyplot as plt
import seaborn as sns

def graf_dist_categoricas(dframe, *categoricas):
    cantidad = len(categoricas)
    rows = cantidad // 3
    rows = rows if rows%3 ==0 else rows+1
    fig, axes = plt.subplots(rows, 3, figsize=(18, 12))
    axes = axes.flatten()
    for grafica in range(cantidad):
        sns.countplot(x=categoricas[grafica], data=df, ax=axes[grafica])
        axes[grafica].set_title('Distribución de ' + categoricas[grafica])
    #axes[5].axis('off')
    plt.tight_layout()
    plt.show()


