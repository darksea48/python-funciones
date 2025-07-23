import pandas as pd
import os
import sys

# --- Configuración ---
# Define la ruta de tu archivo CSV de entrada y el nombre del archivo de salida.
input_file_path = r'C:\Users\Douglas Suárez Z\OneDrive - Cadem S.A\recovery 2022-08-05 trabajo cadem\estudios\2025-07-07 encuestas\19797 aiep\BASE_ AIEP Empleadores 2025 - SAE 19797 - WEB_PARTE2_v1.csv'
# Se usa os.path.splitext para separar la ruta base de la extensión.
base_path, _ = os.path.splitext(input_file_path)
output_file_path = base_path + '_LIMPIO_v1.csv'
# --- Fin de la Configuración ---

# --- Constantes para la limpieza ---
# Mapa para normalizar caracteres comunes en los correos.
EMAIL_NORMALIZATION_MAP = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'n',
    ',': '.'
}
# Expresión regular para eliminar cualquier caracter que NO sea una letra, número o uno de [@ . _ -]
INVALID_EMAIL_CHARS_REGEX = r'[^a-z0-9@._-]'

def _clean_email_series(email_series: pd.Series) -> pd.Series:
    """
    Función auxiliar que aplica una serie de pasos de limpieza a una Serie de pandas de correos.
    Es más eficiente al agrupar operaciones.
    """
    if email_series.dtype != 'object':
        return email_series

    # 1. Convertir a minúsculas, quitar espacios y tomar solo el primer "bloque" de texto.
    cleaned_series = email_series.str.lower().str.strip().str.split().str.get(0)

    # 2. Normalizar caracteres (tildes, ñ, comas) usando el mapa de constantes.
    for old, new in EMAIL_NORMALIZATION_MAP.items():
        cleaned_series = cleaned_series.str.replace(old, new, regex=False)

    # 3. Eliminar todos los caracteres no válidos de una sola vez usando la expresión regular.
    cleaned_series = cleaned_series.str.replace(INVALID_EMAIL_CHARS_REGEX, '', regex=True)

    # 4. Reemplazar dos o más puntos seguidos por uno solo (ej: 'a..b' -> 'a.b').
    cleaned_series = cleaned_series.str.replace(r'\.+', '.', regex=True)

    # 5. Quitar puntos, guiones o guiones bajos que puedan quedar al inicio o final.
    cleaned_series = cleaned_series.str.strip('._-')

    return cleaned_series

def clean_csv_data(input_path, output_path):
    """
    Lee un archivo CSV, limpia los datos de forma eficiente y lo guarda como un nuevo archivo CSV
    con codificación UTF-8 para manejar correctamente tildes y eñes.
    """
    try:
        # Lee el CSV. Usamos dtype=str para evitar la conversión automática de tipos.
        df = pd.read_csv(input_path, sep=';', dtype=str, engine='python', encoding='utf-8')

        # 1. Limpiar los nombres de las columnas (quitar espacios)
        df.columns = df.columns.str.strip()

        # 2. Limpiar la columna específica 'email' usando la función auxiliar.
        col_to_clean = 'email'
        if col_to_clean in df.columns:
            print(f"Limpiando la columna '{col_to_clean}'...")
            df[col_to_clean] = _clean_email_series(df[col_to_clean])
        else:
            print(f"⚠️  Advertencia: La columna '{col_to_clean}' no se encontró en el archivo. No se aplicó limpieza a esa columna.")
            # Continuamos para limpiar el resto del archivo.
        
        # 3. Limpiar el resto de las columnas de texto.
        print("Limpiando celdas y reemplazando punto y coma (;) en las demás columnas...")
        # Primero, quitamos espacios en blanco de todas las celdas de texto.
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
        # Luego, reemplazamos ';' por '/' en las columnas de texto, excluyendo la de email.
        other_text_cols = [c for c in df.select_dtypes(include='object').columns if c != col_to_clean]
        if other_text_cols:
            df[other_text_cols] = df[other_text_cols].apply(lambda col: col.str.replace(';', '/', regex=False))

        # 4. Limpiamos las filas completamente vacías
        df.dropna(how='all', inplace=True)
        
        # 5. Guardar el DataFrame limpio en un nuevo archivo CSV.
        # Se guarda con encoding='utf-8-sig' para que Excel reconozca los caracteres especiales.
        df.to_csv(output_path, index=False, sep=';', encoding='utf-8-sig')
        print(f"✅ ¡Limpieza completada! Archivo guardado en: {output_path}")

    except FileNotFoundError:
        print(f"❌ Error: No se pudo encontrar el archivo en: {input_path}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    clean_csv_data(input_file_path, output_file_path)