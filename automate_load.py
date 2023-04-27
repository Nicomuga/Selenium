import os
from selenium import webdriver

# Inicializa el navegador
driver = webdriver.Chrome()

# Navega a la página de carga de archivos
driver.get("https://ejemplo.com/carga-de-archivos")

# Obtiene la ruta completa de la carpeta exterior
carpetaexterior_path = "/ruta/completa/a/carpetaexterior"

# Para cada carpeta interior en la carpeta exterior
for carpeta in os.listdir(carpetaexterior_path):
    
    # Obtiene la ruta completa de la carpeta interior
    carpeta_path = os.path.join(carpetaexterior_path, carpeta)
    
    # Para cada archivo en la carpeta interior
    for archivo in os.listdir(carpeta_path):
        
        # Obtiene la ruta completa del archivo
        archivo_path = os.path.join(carpeta_path, archivo)
        
        # Ejecuta código JavaScript para cargar el archivo
        driver.execute_script("document.getElementById('boton-carga').style.display = 'block';")
        driver.execute_script("loadimage('{}');".format(archivo_path))
        
        # Haz clic en el botón de carga de la interfaz web para enviar el archivo
        submit_button = driver.find_element_by_xpath("//input[@type='submit']")
        submit_button.click()

# Cierra el navegador
driver.quit()