import pandas as pd
import matplotlib.pyplot as plt

def importar_csv(caminho):
    df = pd.read_csv(caminho, thousands=",")
    return df

def grafico_barra(df):
    df["Spotify Streams"] = df["Spotify Streams"].fillna(0)
    agregado_artista = df.groupby("Artist")["Spotify Streams"].sum()
    agregado_artista = agregado_artista.sort_values(ascending=False)
    top_10 = agregado_artista.head(10)


    plt.figure(figsize=(12, 6))
    plt.bar(top_10.index, top_10)
    plt.title("Dez Artistas Mais Ouvidos no Spotify em 2024", fontweight="bold")
    plt.xlabel("Artistas")
    plt.xticks(rotation=45, ha='right')
    plt.ticklabel_format(style='plain', axis='y')

    y_ticks = plt.gca().get_yticks()
    plt.gca().set_yticklabels([f'{(y / 1_000_000_000)}B' for y in y_ticks])

    plt.tight_layout()
    plt.ylabel("Streams no Spotify (Bilhões)")
    plt.subplots_adjust(left=0.07)
    plt.grid(axis="y", color = "black", linestyle = "--", linewidth = 0.3)
    plt.show()


def grafico_setores(df):
    df["Explicit Track"] = df["Explicit Track"].map({0: "Não Explícita", 1: "Explícita"})
    contagem = df["Explicit Track"].value_counts()
    plt.figure(figsize=(12, 6))
    plt.title("Proporção Entre Músicas Explícitas e Não Explícitas mais ouvidas no Spotify em 2024",
              fontweight="bold", fontsize="16")
    plt.pie(contagem.values, labels=contagem.index, colors = ["#6699ff", "#f63737"], autopct='%1.1f%%', startangle=90,
            textprops={"fontsize": 16})
    plt.axis('equal')
    plt.show()

def grafico_dispercao(df):
    df["Spotify Streams"] = df["Spotify Streams"].fillna(0)
    df = df.sort_values(by="Spotify Streams", ascending=False)
    top_1000 = df.head(1000)

    plt.figure(figsize=(12, 6))
    plt.scatter(top_1000["Spotify Streams"], top_1000["Spotify Popularity"])
    plt.title("Relação Entre Número de Streams e Rating das 1000 Músicas mais Ouvidas no Spotify em 2024",
              fontweight="bold")
    plt.xlabel("Número de Streams no Spotify (Bilhões)")
    plt.ticklabel_format(style='plain')
    x_ticks = plt.gca().get_xticks()
    plt.gca().set_xticklabels([f'{(x / 1_000_000_000)}B' for x in x_ticks])
    plt.ylabel("Rating no Spotify")
    plt.grid(True, color="black", linestyle="--", linewidth=0.3)

    plt.show()



if __name__ == '__main__':
    df = importar_csv(r"C:\Users\Valter\Desktop\spotify.csv")
    grafico_barra(df)
    grafico_setores(df)
    grafico_dispercao(df)