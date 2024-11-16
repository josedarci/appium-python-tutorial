Automação de testes em aplicativos Android utilizando Appium e Python. Este repositório contém um exemplo prático de script que utiliza o Appium para interagir com um botão em um aplicativo Android, incluindo as configurações necessárias e um passo a passo para iniciar.


# Appium Test Script - Android Automation


Este repositório contém um exemplo prático de automação de testes para aplicativos Android utilizando Appium e Python. O script foi desenvolvido por **José Darci Rodrigues Junior** para demonstrar como interagir com um aplicativo através de coordenadas e executar ações automatizadas.


## Sobre o Projeto

Este projeto utiliza o Appium para criar um script que interage com o aplicativo **Nebula Phantoms**. O script realiza as seguintes ações:

- Inicializa o Appium com as configurações do dispositivo e do aplicativo.
- Aguarda a abertura do aplicativo.
- Clica no botão "Play" usando coordenadas específicas (x: 708, y: 1205).
- Encerra a sessão após a execução.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados e configurados:

- Python 3.8 ou superior
- Appium Server
- Appium Python Client (`pip install appium-python-client`)
- Android Debug Bridge (ADB)
- Dispositivo Android com o aplicativo **Nebula Phantoms** instalado ou um emulador configurado.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/josedarci/appium-test-script.git
   cd appium-test-script
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install appium-python-client
   ```

3. Certifique-se de que o Appium Server está rodando:
   ```bash
   appium
   ```

4. Conecte seu dispositivo Android ou inicie um emulador.

5. Execute o script:
   ```bash
   python3 testeapp.py
   ```

6. O script abrirá o aplicativo e clicará no botão "Play".

## Estrutura do Repositório

- **`testeapp.py`**: Script principal de automação.
- **`README.md`**: Este arquivo de documentação.

## Configurações do Script

Atualize as configurações no script de acordo com o seu ambiente:

```python
options.platform_version = "14"  # Substitua pela versão do Android
options.device_name = "Galaxy S22 Ultra"  # Substitua pelo nome do seu dispositivo
options.app_package = "com.pally_evil_studio.NebulaPhantoms"
options.app_activity = ".RunnerActivity"
```
Aqui está a lista completa de dependências necessárias para configurar o ambiente e executar o script de automação com Appium:

---

## Dependências para o Projeto Appium com Python e Node.js

### 1. **Ferramentas Necessárias**
- **Python 3.8 ou superior**
  - Certifique-se de ter o Python instalado.
  - Comando para verificar a versão:
    ```bash
    python3 --version
    ```

- **Node.js e npm**
  - Necessário para instalar e executar o Appium Server.
  - Instale a versão estável LTS do [Node.js](https://nodejs.org/).
  - Verifique a versão:
    ```bash
    node --version
    npm --version
    ```

- **Java Development Kit (JDK)**
  - Requisito para Appium e Android SDK.
  - Instale o JDK (preferencialmente a versão 8 ou superior).
  - Verifique a instalação:
    ```bash
    java -version
    ```

### 2. **Dependências de Python**
Instale as dependências do Python usando `pip`:

- **Appium Python Client**:
  ```bash
  pip install appium-python-client
  ```
- **Selenium WebDriver**:
  ```bash
  pip install selenium
  ```

### 3. **Dependências de Node.js**
Instale globalmente as dependências usando `npm`:

- **Appium Server**:
  ```bash
  npm install -g appium
  ```
- **Appium Inspector** (opcional, para inspecionar elementos):
  ```bash
  npm install -g appium-inspector
  ```

### 4. **Android Debug Bridge (ADB)**
- Instale o ADB para comunicação com dispositivos Android:
  - Se você já tem o Android SDK instalado, o ADB geralmente está incluído.
  - Verifique a instalação:
    ```bash
    adb version
    ```

### 5. **Android SDK**
- Instale o Android SDK para gerenciar dispositivos e emuladores Android:
  - Baixe o SDK Manager [aqui](https://developer.android.com/studio).
  - Certifique-se de instalar:
    - Android SDK Platform-Tools
    - Android Emulator (se necessário)
    - Android Build-Tools

- Adicione as ferramentas do SDK ao `PATH` no sistema:
  ```bash
  export ANDROID_HOME=/caminho/para/android-sdk
  export PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH
  ```

### 6. **Outras Dependências**
- **uiautomator2-driver**: Usado pelo Appium para interagir com dispositivos Android.
  ```bash
  npm install -g appium-uiautomator2-driver
  ```

### 7. **Ferramentas de Suporte (Opcional)**
- **Google Chrome** (para inspecionar logs e depurar):
  - Certifique-se de instalar o Google Chrome no seu sistema e no dispositivo Android.
- **WebDriver para Chrome**:
  - Baixe o WebDriver para a versão do Chrome instalada no dispositivo.
  - Instale-o e adicione ao `PATH`:
    ```bash
    pip install chromedriver-autoinstaller
    ```

---

## Checklist Resumido de Dependências Instaladas

| Ferramenta             | Comando para instalar                                      |
|-------------------------|-----------------------------------------------------------|
| Python 3.8+            | Instale pelo gerenciador do sistema                        |
| Node.js                | `npm install -g` para Appium e outras dependências         |
| Java (JDK 8+)          | Baixe e configure no PATH                                  |
| Appium Python Client   | `pip install appium-python-client`                         |
| Selenium WebDriver     | `pip install selenium`                                     |
| ADB                    | Incluído no Android SDK                                   |
| Android SDK            | Baixe do site oficial e configure no sistema              |
| uiautomator2-driver    | `npm install -g appium-uiautomator2-driver`               |

---

### Comando para Verificar Todas as Dependências
Depois de instalar tudo, verifique os comandos abaixo para confirmar que todas as ferramentas estão funcionando:

```bash
python3 --version           # Versão do Python
node --version              # Versão do Node.js
npm --version               # Versão do npm
java -version               # Versão do Java
adb version                 # Versão do ADB
appium -v                   # Versão do Appium
```

Com tudo isso configurado, você terá um ambiente pronto para executar testes automatizados com Appium, Python, Selenium, e Node.js.
## Autor

Desenvolvido por **José Darci Rodrigues Junior**. Se você tiver dúvidas ou sugestões, fique à vontade para entrar em contato.

