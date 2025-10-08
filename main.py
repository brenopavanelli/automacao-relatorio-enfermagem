import pandas as pd
import os

def carregar_dados(pasta, arquivo):
    caminho_do_arquivo = os.path.join(pasta, arquivo)

    try:
        df = pd.read_csv(str(caminho_do_arquivo), sep=';')
        print("Arquivo CSV carregado com sucesso!")
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado no caminho: {caminho_do_arquivo}")
        return None

def delete_columns(df):
    columns_to_remove = ['ParCalc', 'DescrParCalc', 'Qtde_Total', 'Valor_Total']

    clean_df = df.drop(columns=columns_to_remove)

    print(f"Columns '{', '.join(columns_to_remove)}' successfully removed!")

    return clean_df


if __name__ == "__main__":
    dataframe = carregar_dados('dados_entrada', 'entrada.csv')
    cleaned_df = delete_columns(dataframe)

    print(cleaned_df)
