from csv import DictReader
import matplotlib.pyplot as plt
import pandas as pd

def importar_csv(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', newline='', encoding='utf-8') as arquivo:
            leitor = DictReader(arquivo)
            for linha in leitor:
                dados.append(linha)
            return dados
    except FileNotFoundError:
        print(f"Nenhum caminho com o nome {caminho_arquivo} encontrado")
        return None
    except Exception as e:
        print(f"Erro {e} encontrado")
        return None


# Importante lembrar que os dados aqui sao esperados no formato dicionario
def grafico_linha(dados):
    df = pd.DataFrame(dados)
    df["Data"] = pd.to_datetime(df["Data"], format="%d.%m.%Y")

    # Set 'Data' as index
    df = df.set_index("Data")

    # Convert USD_BRL to numeric, handling potential non-numeric values
    df["USD_BRL"] = pd.to_numeric(df["USD_BRL"])

    # Aggregate to monthly mean
    df_mensal = df["USD_BRL"].resample("ME").mean()

    print(df_mensal.head())
    plt.figure(figsize=(12, 6))
    plt.plot(df_mensal.index, df_mensal.values)
    plt.title("Média Mensal da Conversão Dólar-Real")
    plt.xlabel("Ano")
    plt.ylabel("Valor do R$")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    dados = importar_csv(r"C:\Users\Valter\Desktop\USD_BRL_hist.csv")
    grafico_linha(dados)
