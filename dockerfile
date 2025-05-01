# Usa una imagen base de Python más liviana y actual
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR ./

# Copia los archivos de tu proyecto
COPY . .

# Instala las dependencias
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080 que Cloud Run usará por defecto
EXPOSE 8080

# Comando para ejecutar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]


# Reemplaza CMD con:
CMD ["bash", "start.sh"]
