from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


User = "standard_user"
Password = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")
#login
    user_input = driver.find_element(By.ID, "user-name")
    user_input.send_keys(User)
    pass_input = driver.find_element(By.ID, "password")
    pass_input.send_keys(Password)
    button = driver.find_element(By.ID, "login-button")
    button.click()

    # Esperar un momento a que cargue el inventario
    time.sleep(3)

    # Obtener listas separadas de nombres y precios
    nombres = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    datos_productos = []

    # Combinar ambas listas
    for nombre_elem, precio_elem in zip(nombres, precios):
        nombre_texto = nombre_elem.text
        precio_texto = precio_elem.text

        print(f"Producto: {nombre_texto} - Valor: {precio_texto}")

        datos_productos.append((nombre_texto, precio_texto))

    print("\nLista final:")
    print(datos_productos)

    print("\n" + "="*50)
    print(f"{'PRODUCTO':<35} {'PRECIO':>10}")
    print("="*50)

    for nombre, precio in datos_productos:
        print(f"{nombre:<35} {precio:>10}")

    print("="*50)

if __name__ == '__main__':
    main()