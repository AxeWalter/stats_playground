import nltk
from nltk.corpus import stopwords
from csv import DictReader
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('punkt_tab')

def importar_csv(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', newline='', encoding='utf-8') as arquivo:
            leitor = DictReader(arquivo)
            for linha in leitor:
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f"Erro: não foi encontrado nenhum arquivo no caminho {caminho_arquivo}")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

def analise_frequencia(lista_texto):
    textao = ""
    for linha in lista_texto:
        textao += linha["Text"] + " "
    tokens = nltk.word_tokenize(textao.lower())
    tabela_remocao_pontuacao = str.maketrans('', '', string.punctuation)
    palavras_sem_pontuacao = [palavra.translate(tabela_remocao_pontuacao) for palavra in tokens]
    palavras = [palavra for palavra in palavras_sem_pontuacao if palavra.isalpha()]
    palavras_vazias = set(stopwords.words('portuguese'))
    adicionar_palavras_vazias = {'rony', 'ronylocher', 'pra', 'https', 'https', 'q', 'cara', 'tá', 'pq', 'pro', 'ter', 'vc', 'aí', 'n', 'lá', 'la', 'futebolinfo',
                                 'vai', 'agora', 'fez', 'hoje', 'ainda', 'faz', 'tudo', 'vou', 'ai', 'assim', 'kkkk'}
    palavras_vazias.update(adicionar_palavras_vazias)
    palavras_filtradas = [palavra for palavra in palavras if palavra not in palavras_vazias]
    freq_distribuicao = nltk.FreqDist(palavras_filtradas)

    mais_frequentes = freq_distribuicao.most_common(50)
    #print(f"A palavra mais frequente foi '{mais_frequentes[0][0]}', sendo utilizada {mais_frequentes[0][1]} vezes!\nA segunda"
    #      f" palavra mais frequente foi '{mais_frequentes[1][0]}', sendo utilizada {mais_frequentes[1][1]} vezes!\nA terceira"
    #      f" palavra mais frequente foi '{mais_frequentes[2][0]}', sendo utilizada {mais_frequentes[2][1]} vezes!")

    most_freq_dict = dict(mais_frequentes)
    print(mais_frequentes)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(most_freq_dict)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    csv = importar_csv(r"C:\Users\Valter\PycharmProjects\Projects\stats_playground\tweets_rony3.csv")
    analise_frequencia(csv)