🚕 Digital Taximeter / Taxímetro Digital

🇬🇧 English Version

📌 Project Overview

This project is a digital taximeter developed in Python as part of the Factoría F5 AI Bootcamp.
The application calculates the fare according to the real time spent in two states:
- 🛑 Stopped (parado): €0.02 per second
- 🚕 Moving (movimiento): €0.05 per second

The project was developed progressively, starting with a command-line version and later adding persistence, testing, object-oriented programming, authentication, and a graphical interface.

✅ Implemented Phases
🟢 Phase 1 - MVP
The first phase focused on the essential taximeter behavior:
- Start a journey
- Change between stopped and moving states
- Calculate fare using real elapsed time
- Finish a journey and display the total
- Start another journey without restarting the application
CLI commands:
start   → Start a journey
move    → Taxi moving
stop    → Taxi stopped
finish  → Finish the journey
exit    → Close the application

🟡 Phase 2 - Observability and Persistence
The second phase added:
- Logs in taximetro.log
- Journey history in historial.txt
- External fares in tarifas.json
- Automated tests with pytest
Current fare configuration:
{
  "parado": 0.02,
  "movimiento": 0.05
}
🔵 Phase 3 - Architecture and UX
The third phase added:
- Taximetro class
- Password authentication
- Tkinter GUI
- Live fare display
- Separation between GUI and taximeter logic
🏗️ Project Architecture

The current project uses a simple structure based on the actual files and responsibilities of the application.

gui.py
│
│  The user clicks:
│  - Iniciar carrera
│  - En movimiento
│  - Parado
│  - Finalizar carrera
│
▼
Taximetro object from taximetro.py
│
│  Stores:
│  - carrera_activa
│  - estado
│  - inicio_estado
│  - inicio_carrera
│  - precio_total
│
│  Runs:
│  - iniciar_carrera()
│  - mover()
│  - parar()
│  - finalizar_carrera()
│
├── reads fares from tarifas.json
├── writes events to taximetro.log
└── writes completed journeys to historial.txt

gui.py does not reproduce the complete taximeter logic. It calls the methods of the Taximetro object and displays the current state and fare.

Main files
- main.py → application entry point
- src/taximetro.py → main taximeter logic and CLI
- src/gui.py → graphical interface
- tarifas.json → fare configuration
- test_taximetro.py → automated tests
- .gitignore → excludes local and generated files

🔐 Authentication

On the first execution, the user creates a password.
The application:
- generates a random salt
- creates a PBKDF2-HMAC-SHA256 hash
- stores only the salt and password hash
The plain-text password is not stored.
Authentication information is saved locally in: auth.json
This file is excluded from Git.
A new person cloning the repository creates their own password on first use.

🖥️ Graphical Interface
The GUI was developed with Tkinter.
It displays:
- current taxi state
- live fare
- messages
- journey controls
Available controls:
Iniciar carrera
En movimiento
Parado
Finalizar carrera
Historial
Salir
The fare updates automatically while a journey is active.
📁 Project Structure
Proyecto-1-Beste-Ozaydin/
│
├── main.py
├── src/
│   ├── __init__.py
│   ├── taximetro.py
│   └── gui.py
├── tarifas.json
├── test_taximetro.py
├── README.md
└── .gitignore
Files generated locally during execution may include:
auth.json
historial.txt
taximetro.log
__pycache__/
.venv/

🌿 Git Branches
main
Contains the current integrated and stable version.
feature/basic-taximeter
Used during development of the main taximeter functionality, including:
- CLI
- state management
- timing
- fare calculation
- logging
- history
- configuration
- testing
- OOP refactoring
- authentication
feature/gui
Used to develop:
- Tkinter GUI
- live fare display
- visible state
- GUI controls
- GUI authentication
After testing, feature/gui was merged into main.

🧰 Technologies and Modules
- Python
- Tkinter
- JSON
- time
- logging
- datetime
- hashlib
- secrets
- hmac
- os
- getpass
- pytest
- Git
- GitHub
Most of the application uses Python standard-library modules.
pytest is used for automated testing.

▶️ Run the Project
GUI
python main.py
CLI
python -m src.taximetro
Tests
python -m pytest
📊 Current Status
🟢 Phase 1 - MVP                       ✅
🟡 Phase 2 - Observability/Persistence ✅
🔵 Phase 3 - Architecture/UX           ✅
Phase 4 is not implemented yet.

🔮 Future Development - Phase 4
Possible next steps include:
- relational database
- REST API
- web dashboard
- browser interface
- Docker deployment
- persistent database storage
👩‍💻 Author
Beste Özaydin
Factoría F5 - AI Bootcamp
Barcelona, 2026

---------------------------------------------------------------------


🇪🇸 Versión en Español

📌 Descripción del Proyecto

Este proyecto es un taxímetro digital desarrollado en Python como parte del Bootcamp de Inteligencia Artificial de Factoría F5.
La aplicación calcula el precio según el tiempo real transcurrido en dos estados:
- 🛑 Parado (parado): 0,02 € por segundo
- 🚕 En movimiento (movimiento): 0,05 € por segundo
El proyecto se desarrolló progresivamente, comenzando con una versión de línea de comandos y añadiendo posteriormente persistencia, pruebas, programación orientada a objetos, autenticación e interfaz gráfica.
✅ Fases Implementadas
🟢 Fase 1 - MVP
La primera fase se centró en el comportamiento esencial del taxímetro:
- Iniciar una carrera
- Cambiar entre parado y movimiento
- Calcular el precio usando tiempo real
- Finalizar la carrera y mostrar el total
- Iniciar otra carrera sin reiniciar la aplicación
Comandos CLI:
start   → Iniciar carrera
move    → Taxi en movimiento
stop    → Taxi parado
finish  → Finalizar carrera
exit    → Cerrar aplicación
🟡 Fase 2 - Observabilidad y Persistencia
La segunda fase añadió:
- Logs en taximetro.log
- Historial de carreras en historial.txt
- Tarifas externas en tarifas.json
- Pruebas automatizadas con pytest
Configuración actual de tarifas:
{
  "parado": 0.02,
  "movimiento": 0.05
}
🔵 Fase 3 - Arquitectura y UX
La tercera fase añadió:
- clase Taximetro
- autenticación mediante contraseña
- GUI con Tkinter
- precio actualizado en tiempo real
- separación entre la interfaz y la lógica del taxímetro
🏗️ Arquitectura del Proyecto
La arquitectura actual utiliza una estructura sencilla basada en los archivos y responsabilidades reales del proyecto.
gui.py
│
│  El usuario pulsa:
│  - Iniciar carrera
│  - En movimiento
│  - Parado
│  - Finalizar carrera
│
▼
Objeto Taximetro de taximetro.py
│
│  Guarda:
│  - carrera_activa
│  - estado
│  - inicio_estado
│  - inicio_carrera
│  - precio_total
│
│  Ejecuta:
│  - iniciar_carrera()
│  - mover()
│  - parar()
│  - finalizar_carrera()
│
├── lee tarifas desde tarifas.json
├── guarda eventos en taximetro.log
└── guarda carreras finalizadas en historial.txt
gui.py no reproduce toda la lógica del taxímetro. Utiliza los métodos del objeto Taximetro y muestra el estado y el precio actual.
Archivos principales
- main.py → punto de entrada de la aplicación
- src/taximetro.py → lógica principal y CLI
- src/gui.py → interfaz gráfica
- tarifas.json → configuración de tarifas
- test_taximetro.py → pruebas automatizadas
- .gitignore → excluye archivos locales y generados
🔐 Autenticación
En la primera ejecución, el usuario crea una contraseña.
La aplicación:
- genera un salt aleatorio
- crea un hash PBKDF2-HMAC-SHA256
- guarda únicamente el salt y el hash
La contraseña en texto plano no se almacena.
La información de autenticación se guarda localmente en:
auth.json
Este archivo está excluido de Git.
Una persona que clone el repositorio crea su propia contraseña en la primera ejecución.
🖥️ Interfaz Gráfica
La GUI fue desarrollada con Tkinter.
Muestra:
- estado actual del taxi
- precio en tiempo real
- mensajes
- controles de la carrera
Controles disponibles:
Iniciar carrera
En movimiento
Parado
Finalizar carrera
Historial
Salir
El precio se actualiza automáticamente mientras la carrera está activa.
📁 Estructura del Proyecto
Proyecto-1-Beste-Ozaydin/
│
├── main.py
├── src/
│   ├── __init__.py
│   ├── taximetro.py
│   └── gui.py
├── tarifas.json
├── test_taximetro.py
├── README.md
└── .gitignore
Archivos generados localmente durante la ejecución:
auth.json
historial.txt
taximetro.log
__pycache__/
.venv/
🌿 Ramas de Git
main
Contiene la versión integrada y estable actual.
feature/basic-taximeter
Se utilizó durante el desarrollo del taxímetro principal:
- CLI
- gestión de estados
- tiempos
- cálculo de tarifas
- logging
- historial
- configuración
- pruebas
- refactorización OOP
- autenticación
feature/gui
Se utilizó para desarrollar:
- GUI con Tkinter
- precio en tiempo real
- estado visible
- controles gráficos
- autenticación GUI
Después de probarla, feature/gui se fusionó con main.

🧰 Tecnologías y Módulos
- Python
- Tkinter
- JSON
- time
- logging
- datetime
- hashlib
- secrets
- hmac
- os
- getpass
- pytest
- Git
- GitHub
La mayor parte de la aplicación utiliza módulos de la biblioteca estándar de Python.
pytest se utiliza para las pruebas automatizadas.

▶️ Ejecutar el Proyecto
GUI
python main.py
CLI
python -m src.taximetro
Tests
python -m pytest
📊 Estado Actual
🟢 Fase 1 - MVP                       ✅
🟡 Fase 2 - Observabilidad/Persistencia ✅
🔵 Fase 3 - Arquitectura/UX           ✅
La Fase 4 todavía no está implementada.
🔮 Desarrollo Futuro - Fase 4
Los siguientes pasos pueden incluir:
- base de datos relacional
- API REST
- dashboard web
- interfaz de navegador
- despliegue con Docker
- persistencia mediante base de datos
👩‍💻 Autora
Beste Özaydin
Factoría F5 - Bootcamp de Inteligencia Artificial
Barcelona, 2026
