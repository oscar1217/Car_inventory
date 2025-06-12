import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.header('Inventario 2025')
car_data = pd.read_csv('notebooks/car_model.csv') # leer los datos

# crear una casilla de verificación
build_histogram = st.button('Visualizar histograma de precios')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('**Histograma de Precios** muestra cómo se distribuyen los precios de los coches en tu inventario. Las barras más altas indican los rangos de precios donde tienes más vehículos. Esto te ayuda a ver qué precios son los más comunes y si hay coches muy caros o muy económicos.')
    plt.figure(figsize=(10, 6))
    sns.histplot(car_data['price'], kde=True, color='skyblue')
    plt.xlim(0,25000)
    plt.title('Distribución de Precios de Coches')
    plt.xlabel('Precio USD')
    plt.ylabel('Cantidad de coches')
    st.pyplot(plt.gcf())
 
 # crear una casilla de verificación
price_histogram = st.button('Visualizar scatterpolot de precios')

if price_histogram: # si la casilla de verificación está seleccionada
   
    st.write('*Descubre la relación entre el uso y el valor del vehículo*')
    sns.scatterplot(data=car_data, x='odometer', y='price', hue='type', size='model_year', alpha=0.7, palette='tab10')
    plt.title('Precio vs. Kilometraje por Tipo de Coche', fontsize=14)
    plt.ylim(0,200000)
    plt.xlabel('Kilometraje', fontsize=12)
    plt.ylabel('Precio (USD$)', fontsize=12)
    plt.legend(title='Tipo de Coche', bbox_to_anchor=(1.05, 1), loc='upper left') # Mueve la leyenda fuera del gráfico
    plt.tight_layout()
    st.pyplot(plt.gcf())

marca_button = st.checkbox('Número de coches por marca en el inventario') # crear un botón
     
if marca_button:# al hacer clic en el botón
    # escribir un mensaje
    st.write('Esta **gráfica de barras** muestra cuántos vehículos de cada marca están disponibles en el inventario.')
    # crear un histograma
    plt.figure(figsize=(10, 6))
    sns.countplot(data=car_data, y='brand', order=car_data['brand'].value_counts().index, palette='viridis')
    plt.title('Número de Coches por Marca en el Inventario')
    plt.xlabel('Número de Coches')
    plt.ylabel('Marca')
    st.pyplot(plt.gcf())
    
year_button = st.checkbox('Número de coches por año en el inventario') # crear un botón
     
if year_button:# al hacer clic en el botón
    # escribir un mensaje
    st.write('Esta **gráfica de barras** muestra la cantidad de vehículos disponibles para cada año de fabricación. Permite ver la antigüedad promedio de nuestro inventario y cuántos coches tienes de modelos más recientes, usados o incluso clásicos.')
    # crear una gráfica de barras
    plt.figure(figsize=(10, 6))
    sns.countplot(data=car_data, x='model_year', palette='viridis')
    plt.title('Número de Coches por Año', fontsize=14)
    plt.xlabel('Año del Coche', fontsize=12)
    plt.ylabel('Número de Coches', fontsize=12)
    plt.xticks(rotation=90, ha= 'right', fontsize=6) # Rota las etiquetas del eje X para mejor legibilidad
    st.pyplot(plt.gcf())