import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

# Fixture para inicializar y finalizar el navegador
@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

# Hook para capturar y adjuntar capturas de pantalla en el reporte HTML
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail) or report.passed:
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_path = os.path.join('screenshots', file_name)
            _capture_screenshot(item.funcargs['browser'], file_path)

            if file_path:
                html = '<div><img src="%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src, \\\'_blank\\\'); return false;"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(browser, file_path):
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    browser.save_screenshot(file_path)
