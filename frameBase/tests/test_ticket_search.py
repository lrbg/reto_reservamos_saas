from pages.search_page import SearchPageTicket
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_ticket_search(browser):
    search_page = SearchPageTicket(browser)
    
    # Cargar la página.
    search_page.load()
    
    # Introducir texto en el campo de origen y hacer clic en el mismo campo.
    search_page.enter_text_in_input_and_click(search_page.INPUT_ORIGEN_ID, 'Ciudad De Mexico Auditorio Nacional Cdmx')
    
    # Esperar a que aparezcan las sugerencias y seleccionar la sugerencia correcta por su texto.
    search_page.select_suggestion_by_text('Ciudad de México Auditorio Nacional Cdmx')

    # Introducir texto en el campo de destino y hacer clic en el mismo campo.
    search_page.enter_text_in_input_and_click(search_page.INPUT_DESTINO_ID, 'Leon Centro Max Hotsson Smart')
    
    # Esperar a que aparezcan las sugerencias y seleccionar la sugerencia correcta por su texto.
    search_page.select_suggestion_by_text('León Centro Max Hotsson Smart')

    # Seleccionar la fecha "Mañana".
    search_page.select_date_tomorrow()

    # Esperar 
    time.sleep(5)

    # Hacer clic en el botón de búsqueda.
    search_page.click_search_button()

    # Verificar que el contenedor de resultados está presente en la página.
    search_page.validationResultSeach()

    # Esperar 
    time.sleep(5)    

    # Ahora selecciona el tercer viaje disponible
    search_page.select_third_trip()

    # Esperar 
    time.sleep(5)

    # verifica la apertura de la pag de seleccion de asientos
    search_page.validationseats()

    # Esperar 
    time.sleep(5)

    # Seleccionar un asiento
    search_page.select_seat('4')  # Por ejemplo, para seleccionar el asiento número 3

        # Esperar 
    time.sleep(5)

    # continua con el step 2
    search_page.click_element_sept_1()

    # ... (Otros pasos de la prueba)
    search_page.fill_passenger_info("Juan", "Pérez", "juan.perez@example.com")

    # Esperar 
    time.sleep(5)

    # click en step 2 
    search_page.click_element_sept_2()

    # Esperar 
    time.sleep(5)

    # valida el loading
    search_page.wait_for_loader_to_disappear()
       

    

    # Esperar durante 5 minutos
    time.sleep(10)
