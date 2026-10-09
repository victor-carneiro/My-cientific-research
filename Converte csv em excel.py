import pandas as pd
import glob
import re
import numpy as np
import matplotlib.pyplot as plt

# Conversão CSV -> Excel
for arquivo in glob.glob("*.csv"):
    nome = arquivo.replace(".csv", "")
    df = pd.read_csv(arquivo, sep=";", encoding="utf-8-sig", header=None)
    df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], format="%d%m%Y", errors="coerce").dt.strftime("%d/%m/%Y")
    df.to_excel(f"{nome}.xlsx", index=False, header=False)
    print(f"✅ {nome}.xlsx criado")

# Concatenação do maior para o menor
arquivos_com_parenteses = [f for f in glob.glob("CotacoesMoedasPeriodo*.xlsx") if re.search(r'\((\d+)\)', f)]
arquivos_sem_parenteses = [f for f in glob.glob("CotacoesMoedasPeriodo*.xlsx") if not re.search(r'\((\d+)\)', f) and 
                           "Copia" not in f and "resultado" not in f]

arquivos_com_parenteses = sorted(arquivos_com_parenteses, key=lambda x: int(re.search(r'\((\d+)\)', x).group(1)), reverse=True)

arquivos_final = arquivos_com_parenteses + arquivos_sem_parenteses

df_final = pd.concat([pd.read_excel(f, header=None) for f in arquivos_final], ignore_index=True)
df_final = df_final.dropna(subset=[0])
df_final = df_final.drop_duplicates(subset=[0])

df_final[0] = pd.to_datetime(df_final[0], format="%d/%m/%Y")
df_final = df_final.sort_values(by=0).reset_index(drop=True)
df_final[0] = df_final[0].dt.strftime("%d/%m/%Y")

# Converter colunas E e F para número
df_final[4] = df_final[4].astype(str).str.replace(",", ".").astype(float)
df_final[5] = df_final[5].astype(str).str.replace(",", ".").astype(float)

# Calcular MBG e guardar índices das colunas
colunas_mbg = {}
for col in [4, 5]:
    colunas_mbg[col] = {}
    for p in [1, 7, 30, 180]:
        nome_coluna = df_final.shape[1]
        d = ((np.log(df_final[col].shift(-p)) - np.log(df_final[col])) ** 2) / p
        df_final[nome_coluna] = d.cumsum()
        colunas_mbg[col][p] = nome_coluna

df_final.to_excel("resultado.xlsx", index=False, header=False)
print("✅ resultado.xlsx criado")

# Gráficos
datas = pd.to_datetime(df_final[0], format="%d/%m/%Y")
nomes_col = {4: "Coluna E", 5: "Coluna F"}

for col in [4, 5]:
    for p in [1, 7, 30, 180]:
        idx = colunas_mbg[col][p]
        plt.figure(figsize=(12, 5))
        plt.plot(datas, df_final[idx])
        plt.title(f"MBG - {nomes_col[col]} - p={p}")
        plt.xlabel("Data")
        plt.ylabel("Cm")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"grafico_{nomes_col[col].replace(' ', '_')}_p{p}.png")
        plt.close()
        print(f"✅ grafico_{nomes_col[col].replace(' ', '_')}_p{p}.png criado")