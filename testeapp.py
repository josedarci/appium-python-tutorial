from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# Configurações do dispositivo e do app
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14"  # Substitua pela versão do Android
options.device_name = "Galaxy S22 Ultra"  # Nome do dispositivo
options.app_package = "com.pally_evil_studio.NebulaPhantoms"  # Nome do pacote do app
options.app_activity = ".RunnerActivity"  # Atividade principal do app
options.no_reset = True  # Não reinicia o app entre execuções

# Inicializar o driver Appium
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",  # Certifique-se que o Appium Server está rodando
    options=options
)

try:
    # Aguarde o aplicativo abrir
    time.sleep(5)

    # Toque no botão "Play" com coordenadas
    driver.execute_script("mobile: clickGesture", {"x": 708, "y": 1205})

    print("Botão 'Play' clicado com sucesso!")

    # Aguarde alguns segundos para observar o resultado
    time.sleep(5)

finally:
    # Feche a sessão
    driver.quit()
