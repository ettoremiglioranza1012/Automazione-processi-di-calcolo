# Automazione processi di calcolo per report 'laboratorio sull'economia Italiana'. 
import pandas as pd 
import re 


def replace_comma_with_dot(value):
    return re.sub(r',','.',str(value))

def formatta_cella(value):
    if isinstance(value, (int,float)):
        x_float = float(value)
        x_formattato = format(x_float, '.2f').replace(r'.',',')

        return x_formattato
    else:
        return value 

bf = pd.read_csv('dati fra.csv')

bf.iloc[:, 1:] = bf.iloc[:, 1:].applymap(replace_comma_with_dot)
bf.iloc[:, 1:] = bf.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
colonne_temporali = bf.columns[1:]  
bf_variazioni = bf[['Unnamed: 0']].copy()

for colonna in colonne_temporali:
    anno_corrente = int(colonna)
    
    if anno_corrente > 2014:
        colonna_precedente = str(anno_corrente - 1)
        bf_variazioni[colonna] = ((bf[colonna] - bf[colonna_precedente]) / bf[colonna_precedente]) * 100

bf_variazioni = bf_variazioni.applymap(formatta_cella)
bf_variazioni.to_excel('dataset_arrotondato.xlsx', index=False)