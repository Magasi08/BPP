#%%
import pandas as pd
import os
#%%
#Verifica que el archivo existe y lo lee 
try:
    df = pd.read_csv(os.getcwd()+"\\finanzas2020[1].csv", sep='\t')
    
except FileNotFoundError as e:
    print("El archivo no fue encontrado. Verifique la ruta."
          )
#%%
#Verifica que el archivo tiene 12 columnas
class RaiseLenColumns(Exception):
    pass

try:
    if len(df.columns)!=12:
        raise (RaiseLenColumns)
except RaiseLenColumns:
    print("El número de columnas del archivo no es 12. Compruebe que el archivo tiene la estructura correcta.")

#%%
#Verifica que cada mes tenga datos:
class RaiseDataColumns(Exception):
    pass
try:
    meses=[]
    for columna in df.columns:
        if df[columna].notnull().sum()==0:
            meses.append(columna)
    if len(meses)!=0:
        raise (RaiseDataColumns)
except RaiseDataColumns:
    if len(meses)==1:
        print(f"Las filas del mes de {meses} no contienen datos. Verifique el archivo.")
    else:
        columnas= ', '.join(meses[:-1])+ ' y '+ meses[-1]
        print(f"Las filas de los meses de {columnas} no contienen datos. Verifique el archivo.")
# %%

# Comprueba que todos los datos son correctos
df = df.apply(lambda mes: pd.to_numeric(mes, errors='coerce'))
x = df.isna().any()
x= x[ x== True].index
if len(x)>0:
    columnas=[]
    columnas= ', '.join(x[:-1])+ ' y '+ x[-1]
    print(f"Los meses de {columnas} contienen valores no numéricos. Los mismos serán reemplazados por 0.")
df.fillna(0, inplace=True)

# %%
#¿Qué mes se ha gastado más?
suma= df[df<0].sum()
mesmin=suma[suma==suma.min()].index[0]
min= abs(suma[suma==suma.min()].values[0])
print(f"El mes que se gastó más fue {mesmin} y el gasto fue de {min:.2f}.")

# %%
#¿Qué mes se ha ahorrado más?
suma=df.sum()
mesmax=suma[suma==suma.max()].index[0]
max= suma[suma==suma.max()].values[0]
print(f"El mes que se ahorró más fue {mesmax} y el ahorro fue de {max:.2f}.")

# %%
#¿Cuál es la media de gastos al año?
media=abs(df[df<0].stack().mean())
print(f"La media de gastos al año es {media:.2f}.")

# %%
#¿Cuál ha sido el gasto total a lo largo del año?
gastototal= abs(df[df<0].stack().sum())
print(f"El gasto total durante el año fue de {gastototal:.2f}.")

# %%
#¿Cuáles han sido los ingresos totales a lo largo del año?
ingresototal= df[df>0].stack().sum()
print(f"El ingreso total durante el año fue de {ingresototal:.2f}.")

# %%
# Realice una gráfica de la evolución de ingresos a lo largo del año
pd.DataFrame(df[df>0].sum(), columns= ["Ingresos"]).plot.bar()

# %%
