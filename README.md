# Analizador de Composición Nutricional

Prototipo académico desarrollado con **Python, Flask, HTML, CSS y JavaScript**.

## Funciones incluidas en el cascarón

- Catálogo de alimentos con filtro por categoría y búsqueda por nombre.
- Ficha individual con descripción y composición nutricional de ejemplo.
- Comparador de hasta varios alimentos.
- Sección informativa de vitaminas.
- Tabla general de componentes y cantidades.
- Historial de consultas de la sesión actual.
- Navegación adaptable a dispositivos móviles.

## Requisitos

- Python 3.10 o superior.
- pip.

## Instalación y ejecución

1. Descarga o clona este repositorio.
2. Abre una terminal dentro de la carpeta del proyecto.
3. (Opcional, recomendado) crea un entorno virtual:

   ```bash
   python -m venv .venv
   ```

   En Windows PowerShell:

   ```powershell
   .venv\\Scripts\\Activate.ps1
   ```

   En macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

6. Abre `http://127.0.0.1:5000` en tu navegador.

## Estructura

```text
analizador_composicion_nutricional/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── catalogo.html
│   ├── alimento.html
│   ├── comparador.html
│   ├── vitaminas.html
│   ├── componentes.html
│   ├── historial.html
│   └── 404.html
└── static/
    ├── css/styles.css
    └── js/main.js
```

## Consideraciones importantes

- Los datos nutricionales incluidos son **ilustrativos** y sirven únicamente para demostrar la interfaz. Antes de publicar el sistema, deben sustituirse por datos verificados y acompañarse de su fuente, fecha y referencia de porción.
- El historial se conserva únicamente durante la sesión del navegador. No existe todavía una base de datos.
- No se implementó registro ni inicio de sesión real.
- La clave `SECRET_KEY` es temporal. Debe configurarse mediante una variable de entorno antes de desplegar el proyecto.
- El modo `debug=True` es únicamente para desarrollo local.

## Próximas etapas sugeridas

1. Diseñar la base de datos SQLite con las nueve entidades del diagrama.
2. Implementar modelos y operaciones CRUD para categorías, alimentos y nutrientes.
3. Añadir registro e inicio de sesión con contraseñas protegidas mediante hash.
4. Guardar comparaciones e historial en la base de datos.
5. Incorporar fuentes nutricionales confiables y porciones normalizadas.
6. Desarrollar módulos opcionales de seguimiento personal: peso, medidas corporales y entrenamiento semanal.

## Alcance

Este proyecto tiene una finalidad informativa y educativa. No sustituye la valoración ni las recomendaciones de profesionales de la nutrición.
