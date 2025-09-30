import pandas as pd
import nltk
import re
import matplotlib.pyplot as plt
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from wordcloud import WordCloud

#nltk.download('wordnet')


def importar_csv(caminho):
    df = pd.read_csv(caminho, thousands=",")
    return df


def pre_processamento_nltk(df):
    todos_tweets = " ".join(df['tweet'].astype(str).tolist())
    texto = re.sub(r'http\S+|@\w+|RT\s?', '', todos_tweets)
    tokens = nltk.word_tokenize(texto.lower())

    stop_words = set(stopwords.words('english'))
    lemma = WordNetLemmatizer()

    tokens_processados = []
    for token in tokens:
        if token.isalpha() and token not in stop_words:
            tokens_processados.append(lemma.lemmatize(token))

    return tokens_processados


def pre_processamento_pandas(df, nome, ano):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['insult'] = df['insult'].str.lower()
    df['insult'] = df['insult'].str.replace(r'[^\w\s]', '', regex=True)
    df['insult'] = df['insult'].str.replace('judgement', 'judgment', regex=True)
    df_filtrado = df[(df['target'] == nome) & (df['year'] == ano)]
    df_insultos = df_filtrado['insult'].value_counts().head(10)
    return df_insultos


def grafico_barra(frequencia, titulo):
    palavras = frequencia.index
    quantidade = frequencia.values

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(palavras, quantidade, color='blue')
    ax.bar_label(bars, fmt='%d')
    plt.bar(palavras, quantidade, color='blue')
    plt.xlabel('Palavras')
    plt.ylabel('Quantidade de Vezes Utilizada')
    plt.title(titulo)
    plt.grid(axis="y", color="black", linestyle="--", linewidth=0.3)
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()


def word_cloud(frequencia, titulo):
    wordcloud = WordCloud(
        background_color='white',
        width=1600,
        height=800,
        max_words=20,
        min_font_size=30
    ).generate_from_frequencies(frequencia)

    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(titulo, fontsize=28)
    plt.show()


if __name__ == '__main__':
    df = importar_csv(r"C:\Users\Valter\Desktop\databaseTrump.csv")

    tweets_limpos = pre_processamento_nltk(df)
    frequencia = nltk.FreqDist(tweets_limpos)
    top_20 = frequencia.most_common(20)
    top_20_series = pd.Series([qnt for palavra, qnt in top_20], index=[palavra for palavra, qnt in top_20])
    grafico_barra(top_20_series, "Top 20 Palavras Mais Utilizadas por Donald Trump em seus Insultos no Twitter")
    word_cloud(frequencia, "Top 20 Palavras Mais Utilizadas por Donald Trump em seus Insultos no Twitter")

    insultos_hillary = pre_processamento_pandas(df.copy(), "hillary-clinton", 2016)
    word_cloud(insultos_hillary, "Top 10 Insultos de Donald Trump a Hillary Clinton em 2016")
    grafico_barra(insultos_hillary, "Top 10 Insultos de Donald Trump a Hillary Clinton em 2016")

    insultos_biden = pre_processamento_pandas(df.copy(), "joe-biden", 2020)
    word_cloud(insultos_biden, "Top 10 Insultos de Donald Trump a Joe Biden em 2016")
    grafico_barra(insultos_biden, "Top 10 Insultos de Donald Trump a Joe Biden em 2016")



