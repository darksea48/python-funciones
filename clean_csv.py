import pandas as pd
import os

# --- Configuración ---
# Define la ruta de tu archivo CSV de entrada y el nombre del archivo de salida.
input_file_path = r'e:\Carpetas Usuario\Downloads\19761_base.csv'
output_file_path = r'e:\Carpetas Usuario\Downloads\contactos_limpios.csv'
# --- Fin de la Configuración ---

def clean_csv_data(input_path, output_path):
    """
    Lee un archivo CSV, limpia los datos y lo guarda como un nuevo archivo CSV
    con codificación UTF-8 para manejar correctamente tildes y eñes.
    """
    try:
        # Lee el CSV. Usamos dtype=str para evitar la conversión automática de tipos (ej. notación científica).
        # El engine='python' ayuda a manejar mejor los delimitadores y comillas complejas.
        # Se añade encoding='utf-8' para leer caracteres especiales como tildes y 'ñ'.
        df = pd.read_csv(input_path, sep=';', dtype=str, engine='python', encoding='utf-8')

        # 1. Limpiar los nombres de las columnas (quitar espacios)
        df.columns = df.columns.str.strip()

        # 2. Limpiar los datos en cada celda
        for col in df.columns:
            if df[col].dtype == 'object':  # Aplicar solo a columnas de texto
                # Quitar espacios al inicio y al final
                df[col] = df[col].str.strip()
                # Reemplazar saltos de línea y tabulaciones por un espacio
                df[col] = df[col].str.replace(r'[\r\n\t]+', ' ', regex=True)
                # Quitar comillas dobles que estén dentro del texto
                df[col] = df[col].str.replace('"', '', regex=False)
                # Reemplazar múltiples espacios seguidos por uno solo
                df[col] = df[col].str.replace(r'\s+', ' ', regex=True).str.strip()

        # 3. Eliminar filas donde el 'email' es nulo o está vacío, ya que es un campo crucial.
        # df.dropna(subset=['email'], inplace=True)

        # 4. Guardar el DataFrame limpio en un nuevo archivo CSV, usando comas como delimitador.
        # Se guarda con encoding='utf-8-sig' para que Excel y otros programas reconozcan los caracteres especiales.
        df.to_csv(output_path, index=False, sep=',', encoding='utf-8-sig')
        print(f"✅ ¡Limpieza completada! Archivo guardado en: {output_path}")

    except FileNotFoundError:
        print(f"❌ Error: No se pudo encontrar el archivo en: {input_path}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    clean_csv_data(input_file_path, output_file_path)