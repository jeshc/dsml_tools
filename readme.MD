# Herramientas DSML

# distribuciones.py

1. Clase NormalDist
2. Clase BinomialDist


## graf_dist_categóricas:
Gráficas de frecuencias para datos categóricos. Argumentos: DF y los nombres de las columnas categóricas.

## limpia_cadena:
Para limpiar nombres de columnas de DF.

Uso
```
new_columns = {name:limpia_cadena(name.strip(),r'[\$\(\)]','') for name in df.columns}
df.rename(columns=new_columns, inplace=True)
df.head(1)
```