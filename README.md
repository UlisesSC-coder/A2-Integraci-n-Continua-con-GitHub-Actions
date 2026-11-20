# Mini-sistema de videojuegos (Flask)

![CI](https://github.com/UlisesSC-coder/A2-Integraci-n-Continua-con-GitHub-Actions/actions/workflows/ci.yml/badge.svg)
[![Coverage](https://codecov.io/gh/UlisesSC-coder/A2-Integraci-n-Continua-con-GitHub-Actions/branch/main/graph/badge.svg)](https://codecov.io/gh/UlisesSC-coder/A2-Integraci-n-Continua-con-GitHub-Actions)

Aplicación web en Flask para administrar un catálogo de videojuegos.
Usa SQLAlchemy, Flask-Login y una API REST con Flask-RESTful.

## Instalación

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Cómo correr las pruebas

    pytest --cov=app

Las pruebas usan la configuración `TestingConfig`, que trabaja con SQLite en memoria,
por lo que no necesitan MySQL ni XAMPP.

## Integración continua

En cada push o pull request, GitHub Actions (`.github/workflows/ci.yml`):

1. Instala Python 3.13 y las dependencias de `requirements.txt`.
2. Ejecuta las pruebas unitarias con pytest.
3. Genera el reporte de cobertura con pytest-cov y lo envía a Codecov.