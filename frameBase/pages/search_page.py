from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

class SearchPageTicket:
    URL = 'https://roll-bits.reservamos-saas.com/'
    INPUT_ORIGEN_ID = "txtorigin-desktop"
    INPUT_DESTINO_ID = "txtdestination-desktop"
    LISTA_SUGERENCIAS = ".es-list li .place-info-classic div.place-info"
    BOTON_BUSCAR = "button[class*='search-button']"
    BOTONES_FECHA = "div.dates-controls-wrapped button.dates-controls-button"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def enter_text_in_input_and_click(self, element_id, text):
        input_field = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.ID, element_id))
        )
        input_field.clear()
        input_field.send_keys(text)
        input_field.click()

    def click_element(self, css_selector):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()

    def select_suggestion_by_text(self, partial_text):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.LISTA_SUGERENCIAS))
        )
        all_suggestions = self.browser.find_elements(By.CSS_SELECTOR, self.LISTA_SUGERENCIAS)
        for suggestion in all_suggestions:
            if partial_text in suggestion.text:
                suggestion.click()
                return

    def select_date_tomorrow(self):
        date_buttons = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.BOTONES_FECHA))
        )
        # Buscar y hacer clic en el botón que contiene el texto "Mañana"
        for button in date_buttons:
            if button.text == "Mañana":
                button.click()
                break

    def click_search_button(self):
        self.click_element(self.BOTON_BUSCAR)


    def validationResultSeach(self):
        # Verificar que el contenedor de resultados está presente en la página.
        WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".results-container"))
    )

    def select_third_trip(self):
        # Localiza todos los viajes en la página
        trips = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".matrix.matrix-default"))
        )
        # Asegúrate de que hay al menos tres viajes listados
        if len(trips) >= 3:
            # Los elementos están indexados desde 0, así que 2 será el tercer elemento
            choose_buttons = trips[2].find_elements(By.CSS_SELECTOR, "button.css-1kcqoud-D")
            # Asegúrate de que hay al menos un botón "Elegir"
            if choose_buttons:
                # Hacer clic en el primer botón "Elegir" del tercer viaje
                choose_buttons[0].click()
        else:
            raise Exception("No hay suficientes viajes listados para seleccionar el tercero.")


    def validationseats(self):
        WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".purchase-step-wrapper"))
    )

    # Método para seleccionar un asiento disponible
    def select_seat(self, seat_number):
        # Espera hasta que los asientos estén visibles
        seats = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".seat-available"))
        )
        # Encuentra el botón del asiento por su texto y haz clic
        for seat in seats:
            if seat.text == str(seat_number):
                seat.click()
                return
        raise Exception(f"Seat number {seat_number} not found or is not available.")


    def click_element_sept_1(self):
        # Esperar hasta que el elemento sea clickeable
        element = WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-10fhysf-D"))
        )
        element.click()

    # Método para llenar el formulario del pasajero
    def fill_passenger_info(self, first_name, last_name, email):
        # Esperar y rellenar el nombre
        first_name_field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "passengers[0].firstName"))
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        # Esperar y rellenar el apellido
        last_name_field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "passengers[0].lastName"))
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        # Esperar y rellenar el correo electrónico
        email_field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "passengers[0].email"))
        )
        email_field.clear()
        email_field.send_keys(email)    

    # Método para dar click al boton de siguiente proceder con el pago
    def click_element_sept_2(self):
        # Esperar hasta que el elemento sea clickeable
        element = WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".main-button"))
        )
        element.click()

    # Método para verificar la presencia del loader y esperar hasta que desaparezca
    def wait_for_loader_to_disappear(self):
        # Define el localizador del elemento loader
        loader_text_locator = (By.CSS_SELECTOR, "p.loader-text > em#content")
        
        # Configura un tiempo de espera
        wait_time = 10

        # Inicia un bucle que dura wait_time segundos
        end_time = time.time() + wait_time
        while True:
            try:
                # Busca el loader y espera a que esté visible
                WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located(loader_text_locator))
            except TimeoutException:
                # Si el loader no se encuentra, rompe el bucle
                break
            
            # Si el tiempo actual es mayor al tiempo final, lanza la excepción de timeout
            if time.time() > end_time:
                raise TimeoutException("El loader no desapareció después de {} segundos".format(wait_time))
            
            # Espera un breve momento antes de revisar de nuevo
            time.sleep(0.1)
