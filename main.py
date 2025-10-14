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
    df_copy = df.copy()
    columns_to_remove = ['ParCalc', 'DescrParCalc', 'Qtde_Total', 'Valor_Total']

    df_copy = df_copy.drop(columns=columns_to_remove)

    print(f"Columns '{', '.join(columns_to_remove)}' successfully removed!")

    return df_copy

def columns_rename(df):
    df_copy = df.copy()
    map = {
        'Matricula': 'MATRÍCULA',
        'Cpf': 'CPF',
        'Nome_Completo': 'NOME DO FUNCIONÁRIO',
        'Des_LocalTrab': 'LOCAL DE TRABALHO',
        'Des_Cargo': 'CARGO',
        'CBO': 'CBO',
        'Resc': 'ATV',
        'HrSem': 'JORN. SEMANAL',
        'VB001_Valor': 'SALARIO BASE'
    }

    df_copy = df_copy.rename(columns=map)

    print("Columns have been renamed!")

    return df_copy

def sort_data(df):
    df_copy = df.copy()
    df_copy = df_copy.sort_values(by='NOME DO FUNCIONÁRIO')
    print('DataFrame sorted by "NOME DO FUNCIONÁRIO"')

    return df_copy

def update_atv(df):
    df_copy = df.copy()
    df_copy['ATV'] = df_copy['ATV'].replace('Não', 'Sim')
    print('The values in the "ATV (NOME DO MES)" column have been updated')
    return df_copy

def insert_columns(df):
    df_copy = df.copy()

    df_copy['VANTAGENS DE CARÁTER FIXO'] = 0
    df_copy['VANTAGENS VARIAVEIS'] = 0
    df_copy['AD. NOTURNO'] = 0
    df_copy['INSALUBRIDADE'] = 0

    print("Columns add successfully!")
    return df_copy


if __name__ == "__main__":
    dataframe = load_data('dados_amostra', 'fonte_exemplo.csv')

    if dataframe is not None:
        dataframe = delete_columns(dataframe)
        dataframe = columns_rename(dataframe)
        dataframe = sort_data(dataframe)
        dataframe = update_atv(dataframe)
        dataframe = insert_columns(dataframe)

        print("\n--- DataFrame ---")
        print(dataframe.head())

    else:
        print('Error!')