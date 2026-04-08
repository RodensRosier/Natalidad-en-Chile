# Natalidad en Chile
### Tasa de natalidad en Chile en comparación con las otras naciones

# Canasta Básica e Inflación en Chile 
### Análisis de la variación de la canasta básica y ajuste de la inflación (2016-2026)

### Descripción del Proyecto

### Stack Tecnológico
Lenguaje: Python 3.10
Librerías de Análisis: Pandas, NumPy
Visualización: Matplotlib, Seaborn, Tableau
Entorno Cloud: Google Cloud Platform (BigQuery para procesamiento masivo)

### Metodología (Pipeline ETL)
Extracción: Obtención de microdatos desde el portal de datos abiertos del INE Chile.
Transformación (Limpieza):
Tratamiento de valores nulos y registros atípicos (outliers).
Normalización de variables de ingresos y categorías de ocupación.
Análisis: Cálculo de la brecha salarial bruta y ajustada por horas trabajadas y nivel de instrucción.
Carga/Visualización: Exportación de resultados a un Dashboard interactivo en Tableau.

### Hallazgos Claves
Brecha Promedio: Se identificó una brecha salarial del XX% a nivel nacional.
Sectores Críticos: El sector de Minería presenta la brecha más alta, mientras que Tecnología muestra una tendencia a la reducción.
Efecto Educación: A mayor nivel educativo, la brecha tiende a [aumentar/disminuir] según los datos procesados.

### Estructura del Repositorio
/data: Diccionarios de datos y fuentes.
/notebooks: Jupyter Notebooks con el Análisis Exploratorio (EDA).
/scripts: Scripts de Python para la automatización del proceso.

### Dashboard y gráficos estadísticos.

### Cómo Ejecutar el Proyecto
### bash
```
    git clone https://github.com
    cd brecha-salarial-chile
    pip install -r requirements.txt
    python script.py
```

### Fuentes
• INE Chile - Estadísticas Vitales: La fuente primaria de nacimientos y defunciones. <br>
• DEIS (Ministerio de Salud): Datos sobre partos y salud reproductiva.<br>
• CELADE (División de Población de la CEPAL): Para comparar la situación de Chile con el resto de Latinoamérica.
