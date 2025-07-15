import pandas as pd
import os

# --- Configuración ---
# Define la ruta de tu archivo CSV de entrada y el nombre del archivo de salida.
input_file_path = r'C:\Users\Douglas Suárez Z\OneDrive - Cadem S.A\recovery 2022-08-05 trabajo cadem\estudios\2025-07-07 encuestas\19797 aiep\BASE_ AIEP Empleadores 2025 - SAE 19797 - WEB_PARTE1.csv'
output_file_path = r'C:\Users\Douglas Suárez Z\OneDrive - Cadem S.A\recovery 2022-08-05 trabajo cadem\estudios\2025-07-07 encuestas\19797 aiep\BASE_ AIEP Empleadores 2025 - SAE 19797 - WEB_PARTE1_LIMPIO.csv'
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

        # 2. Limpiar los datos en la columna específica 'email'
        col_to_clean = 'email'
        if col_to_clean in df.columns:
            # Aplicamos la limpieza solo si la columna es de tipo texto ('object')
            if df[col_to_clean].dtype == 'object':
                print(f"Limpiando la columna '{col_to_clean}'...")
                df[col_to_clean] = (df[col_to_clean].str.lower()  # 1. Convertir todo a minúsculas para simplificar
                    .str.strip()  # 2. Quitar espacios al inicio y al final
                    # 3. Truncar a un solo correo (el primero) si hay varios separados por espacio
                    .str.split().str.get(0)
                    # 4. Normalizar caracteres comunes (tildes, ñ, etc.)
                    .str.replace('á', 'a', regex=False)
                    .str.replace('é', 'e', regex=False)
                    .str.replace('í', 'i', regex=False)
                    .str.replace('ó', 'o', regex=False)
                    .str.replace('ú', 'u', regex=False)
                    .str.replace('ü', 'u', regex=False)
                    .str.replace('ñ', 'n', regex=False)
                    .str.replace(',', '.', regex=False)  # Reemplazar comas por puntos
                    # 5. Eliminar todos los caracteres que no son válidos en un email.
                    #    Esto incluye espacios, saltos de línea, comillas, !, #, $, etc.
                    .str.replace(' ', '', regex=False)
                    .str.replace('\n', '', regex=False)
                    .str.replace('"', '', regex=False)
                    .str.replace('!', '', regex=False)
                    .str.replace('#', '', regex=False)
                    .str.replace('$', '', regex=False)
                    .str.replace('%', '', regex=False)
                    # 6. Reemplazar dos o más puntos seguidos por uno solo (ej: 'a..b' -> 'a.b').
                    .str.replace(r'\.+', '.', regex=True)
                    # 7. Quitar puntos, guiones o guiones bajos que puedan quedar al inicio o final.
                    .str.strip('._-><'))
        else:
            print(f"⚠️  Advertencia: La columna '{col_to_clean}' no se encontró en el archivo. No se aplicó limpieza a esa columna.")

        # 3. En el resto de las columnas, reemplazar ';' por '/'
        print("Reemplazando punto y coma (;) por barra (/) en las demás columnas de texto...")
        for col in df.columns:
            # Aplicamos el cambio solo a las columnas que no son 'email' y son de tipo texto
            if col != col_to_clean and df[col].dtype == 'object':
                df[col] = df[col].str.replace(';', '/', regex=False)

        # 4. Eliminar filas donde el 'email' es nulo o está vacío, ya que es un campo crucial.
        # df.dropna(subset=['email'], inplace=True)

        # 5. Guardar el DataFrame limpio en un nuevo archivo CSV, usando comas como delimitador.
        # Se guarda con encoding='utf-8-sig' para que Excel y otros programas reconozcan los caracteres especiales.
        df.to_csv(output_path, index=False, sep=';', encoding='utf-8-sig')
        print(f"✅ ¡Limpieza completada! Archivo guardado en: {output_path}")

    except FileNotFoundError:
        print(f"❌ Error: No se pudo encontrar el archivo en: {input_path}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    clean_csv_data(input_file_path, output_file_path)