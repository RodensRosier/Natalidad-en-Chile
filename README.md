# Natalidad en Chile
Análisis de la tasa de natalidad en Chile

### Stack Tecnológico
**• Lenguajes de programación:** Python 3.10, SQL. <br>
**• Librerías de Análisis:** Pandas, NumPy. <br>
**• Visualización:** Tableau. <br>
**• Entorno Cloud:** GCP (Google Cloud Platform) BigQuery para el procesamiento masivo.

### Metodología (Pipeline ETL)
**• Extracción:** Obtención de microdatos desde el portal de datos abiertos del INE Chile. <br>
**• Transformación (Limpieza):** Tratamiento de valores nulos y registros atípicos (outliers) y normalización de variables de ingresos y categorías de ocupación. <br>
**• Análisis:** Cálculo de la brecha salarial bruta y ajustada por horas trabajadas y nivel de instrucción. <br>
**• Carga/Visualización:** Exportación de resultados a un Dashboard interactivo en Tableau.

### Hallazgos Claves
**• Brecha Promedio:** Se identificó una brecha salarial del XX% a nivel nacional. <br>
**• Sectores Críticos:** El sector de Minería presenta la brecha más alta, mientras que Tecnología muestra una tendencia a la reducción. <br>
**• Efecto Educación:** A mayor nivel educativo, la brecha tiende a [aumentar/disminuir] según los datos procesados.

### Estructura del Repositorio
**• /data:** Diccionarios de datos y fuentes. <br>
**• /notebooks:** Jupyter Notebooks con el Análisis Exploratorio (EDA). <br>
**• /scripts:** Scripts de Python para la automatización del proceso.

### Dashboard y gráficos estadísticos.
<br>

### Cómo Ejecutar el Proyecto
```
    git clone https://github.com
    cd brecha-salarial-chile
    pip install -r requirements.txt
    python script.py
```

### Fuentes
**• INE Chile - Estadísticas Vitales:** La fuente primaria de nacimientos y defunciones. <br>
**• DEIS (Ministerio de Salud):** Datos sobre partos y salud reproductiva.<br>
**• CELADE (División de Población de la CEPAL):** Para comparar la situación de Chile con el resto de Latinoamérica.
