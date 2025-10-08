import pandas as pd
import os

def load_data(pasta, arquivo):
    path = os.path.join(pasta, arquivo)

    try:
        df = pd.read_csv(str(path), sep=';')
        print("CSV file uploaded successfully!")
        return df
    except FileNotFoundError:
        print(f"Error: The file was not find in the path: {path}")
        return None

def delete_columns(df):
    columns_to_remove = ['ParCalc', 'DescrParCalc', 'Qtde_Total', 'Valor_Total']

    clean_df = df.drop(columns=columns_to_remove)

    print(f"Columns '{', '.join(columns_to_remove)}' successfully removed!")

    return clean_df

def columns_rename(df):
    map = {
        'Matricula': 'MATRÍCULA',
        'Cpf': 'CPF',
        'Nome_Completo': 'NOME DO FUNCIONÁRIO',
        'Des_LocalTrab': 'LOCAL DE TRABALHO',
        'Des_Cargo': 'CARGO',
        'CBO': 'CBO',
        'Resc': 'ATV (NOME DO MES)',
        'HrSem': 'JORN. SEMANAL',
        'VB001_Valor': 'SALARIO BASE'
    }

    new_df = df.rename(columns=map)

    return new_df



if __name__ == "__main__":
    dataframe = load_data('dados_entrada', 'entrada.csv')
    cleaned_df = delete_columns(dataframe)
    df_renamed = columns_rename(cleaned_df)

    print(df_renamed)
