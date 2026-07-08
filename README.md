# SuperGestion

Sistema de gestión de supermercado por consola, desarrollado en Python como proyecto para la materia **Algoritmos y Estructuras de Datos**.

Integrantes:
Chezzi, Fabricio
Escalante, Lucio Matias
Agustin, Andres Leguizamon, Sena
Agustin, Ignacio
Moreyra, Agustin

Comision: ISI K1.2

## Descripción

SuperGestion es una aplicación de consola que resuelve un problema típico de gestión comercial a pequeña escala: permitir a un supermercado **cargar productos y descuentos, buscarlos, calcular el total de una venta (con o sin promociones), registrar esas ventas y obtener reportes** (productos más vendidos y estadísticas generales), todo esto **sin depender de una base de datos externa**, utilizando archivos de texto plano como mecanismo de persistencia.

El sistema distingue dos roles de usuario mediante un login por credenciales fijas:

- **Administrador (`admin`)**: puede cargar productos y descuentos, además de acceder a todas las demás operaciones.
- **Operador (`operador`)**: puede consultar, vender y generar reportes, pero no puede dar de alta productos ni descuentos.

El problema que resuelve, en esencia, es **cómo estructurar y persistir información tabular (productos, descuentos, ventas) usando exclusivamente las herramientas propias de la cátedra**: secuencias, recorridos con `ARR`/`AVZ`, archivos, y algoritmos de búsqueda y ordenamiento implementados "a mano", en lugar de recurrir a estructuras avanzadas de Python (diccionarios, `sorted()`, bases de datos, `try/except`) que un curso introductorio de Algoritmos y Estructuras de Datos todavía no habilita.

## Contexto académico

El proyecto es una aplicación directa de los contenidos centrales de la materia:

| Contenido de la cátedra | Dónde se aplica en el proyecto |
|---|---|
| Noción de secuencia y recorrido (`ARR`/`AVZ`/`FDS`) | Lectura de `archivo.txt`, `descuentos.txt` y `ventas.txt` línea por línea, reconociendo cada registro como una subsecuencia delimitada por la marca `///` |
| Búsqueda secuencial (lineal) | `EsOpcionValida`, `BuscarProductoPorCodigo`, `BuscarDescuentoPorCodigo`, acumulación de ventas por producto en `ProductosMasVendidos` |
| Ordenamiento (método burbuja) | `ProductosMasVendidos`, para ordenar de mayor a menor cantidad vendida |
| Validación de datos de entrada | `EsEnteroValido`, `EsRealValido`, `PedirInt`, `PedirFloat`, `ValidadorOpcion`, todas con esquema "repetir hasta ingreso válido" |
| Registros (estructuras heterogéneas de datos) | Clases `Producto` y `Descuento` en `registros.py`, implementadas como `dataclass` |
| Manejo de archivos secuenciales | Apertura, escritura (`'a'`/`'w'`), lectura (`'r'`) y cierre explícito de archivos en cada operación de persistencia |
| Estructuras de control (`while`, `if/elif`) | Todo el flujo del menú principal y de los submenús de carga de datos |
| Modularización | Separación en `main.py` (control), `funciones.py` (lógica) y `registros.py` (datos) |

Un aspecto particular del código es que evita deliberadamente construcciones "no vistas en clase" (como el operador `in` sobre tuplas, o el manejo de excepciones con `try/except`), reemplazándolas por sus equivalentes explícitos en pseudocódigo de cátedra. Esto está documentado en comentarios `#FIX:` dentro del propio código fuente.

## Objetivos

### Objetivo general

Diseñar e implementar un sistema de gestión de ventas para un supermercado que aplique, de forma práctica, los conceptos fundamentales de secuencias, archivos, búsqueda y ordenamiento vistos en la materia Algoritmos y Estructuras de Datos.

### Objetivos específicos

- Implementar un esquema de persistencia de datos en archivos de texto plano, sin bases de datos ni formatos serializados.
- Aplicar recorridos secuenciales (`ARR`/`AVZ`) para leer, buscar y acumular información almacenada en archivos.
- Implementar un algoritmo de ordenamiento (burbuja) sin utilizar funciones nativas de ordenamiento de Python.
- Validar todas las entradas del usuario sin recurrir a manejo de excepciones.
- Modelar entidades del dominio (`Producto`, `Descuento`) como registros tipados.
- Separar responsabilidades entre control de flujo, lógica de negocio y modelado de datos.
- Generar comprobantes de venta (tickets) persistidos como archivos independientes.

## Tecnologías utilizadas

| Tecnología / módulo | Uso en el proyecto |
|---|---|
| **Python 3** | Lenguaje de implementación |
| `os` (estándar) | Limpiar la consola (`cls`/`clear`) y verificar existencia de archivos (`os.path.exists`) |
| `datetime` (estándar) | Obtener fecha y hora del sistema para ventas y tickets |
| `dataclasses` (estándar) | Definición simplificada de los registros `Producto` y `Descuento` |
| Archivos de texto plano (`.txt`) | Persistencia de productos, descuentos, ventas, numeración de tickets y tickets generados |

No se utilizan librerías externas ni gestores de bases de datos: toda la persistencia se resuelve con las operaciones básicas de archivos del lenguaje.

## Estructura del proyecto

```
SuperGestion/
├── main.py                    # Punto de entrada: login, menú y bucle principal
├── funciones.py                # Lógica de negocio, validaciones, E/S de archivos
├── registros.py                # Definición de los registros Producto y Descuento
├── archivo.txt                 # "Tabla" de productos (persistencia)
├── descuentos.txt               # "Tabla" de descuentos (persistencia)
├── ventas.txt                  # "Tabla" de ventas registradas (persistencia)
├── numeroticket.txt             # Contador correlativo de tickets
├── ticket_XXXX.txt              # Comprobantes generados por cada venta (uno por operación)
├── comentarios opcion7.txt      # Bitácora de la implementación de promociones
└── mensajeultimoedit.txt        # Bitácora de la última tanda de cambios
```

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Orquesta la ejecución: muestra el menú, gestiona el login y el estado de sesión (`admin`/`operador`/`salir`), y despacha cada opción a la función correspondiente de `funciones.py` |
| `funciones.py` | Concentra toda la lógica: autenticación, validación de entradas, alta y búsqueda de productos/descuentos, cálculo de ventas, promociones, generación de tickets y reportes estadísticos |
| `registros.py` | Define los registros del dominio (`Producto`, `Descuento`) usando `@dataclass`, equivalentes a un `REGISTRO` de cátedra con campos tipados |
| `archivo.txt` / `descuentos.txt` / `ventas.txt` | Actúan como "tablas" persistentes, cada una con sus registros delimitados por la marca `///` |
| `numeroticket.txt` | Guarda el próximo número de ticket a utilizar (secuencia de un único valor) |

## Funcionamiento del sistema

1. Al iniciar, `main.py` limpia la consola y muestra el mensaje de bienvenida.
2. Se solicita un usuario y contraseña mediante `Login()`. Según las credenciales, la función retorna:
   - `'a'` si es administrador (`admin` / `admin123`)
   - `'o'` si es operador (`operador` / `operador123`)
   - `'s'` si el usuario ingresa `salir`
   - el mismo estado anterior si las credenciales son incorrectas (permitiendo reintentar)
3. Si el login es válido, se muestra el **menú principal** con 8 opciones (7 funcionalidades + salir).
4. El usuario ingresa una opción, que se valida mediante **búsqueda secuencial** contra la lista de opciones válidas (`EsOpcionValida`) y luego se convierte a entero (`StraInt`).
5. Según la opción elegida, se ejecuta la operación correspondiente:
   - **1 - Cargar producto** *(solo admin)*: pide datos, valida y persiste el producto en `archivo.txt`.
   - **2 - Cargar descuento** *(solo admin)*: pide datos, valida y persiste el descuento en `descuentos.txt`.
   - **3 - Buscar producto**: busca por código con recorrido secuencial sobre `archivo.txt` y muestra sus datos.
   - **4 - Calcular total de venta**: permite cargar varios productos, valida stock, aplica un descuento opcional, genera el ticket y registra cada ítem vendido en `ventas.txt`.
   - **5 - Productos más vendidos**: lee todo el historial de ventas, acumula cantidades por producto y las ordena de mayor a menor con burbuja.
   - **6 - Estadísticas de ventas**: calcula totales, unidades vendidas, promedio por venta y fechas de primera/última venta.
   - **7 - Promoción mayorista/minorista**: permite aplicar promociones (2x1, 3x2 o 43% de descuento mayorista) sobre los productos de una venta.
6. Si el usuario ingresa `salir` en el login, el programa finaliza el bucle principal y muestra un mensaje de despedida.

## Algoritmos y estructuras de datos utilizadas

### Secuencias y archivos como estructura de persistencia

Cada "tabla" (`archivo.txt`, `descuentos.txt`, `ventas.txt`) se trata como una **secuencia de líneas**, donde cada registro es una **subsecuencia impura** delimitada por la marca `'///'` (no se conoce de antemano dónde termina un registro; se reconoce por la marca de fin, tal como se ve en la noción de Secuencia de la cátedra). El patrón de lectura es siempre el mismo:

```
ARR(archivo)            -> abrir y leer todas las líneas
MIENTRAS i < total:
    SI linea[i] == '///' ENTONCES
        AVZ por cada campo del registro (nombre, precio, stock, codigo...)
        AVZ hasta pasar la marca de cierre '///'
    SINO
        AVZ
FDS
```

Esto se aplica en `BuscarProductoPorCodigo`, `BuscarDescuentoPorCodigo` y `LeerVentas`.

- **Complejidad:** O(n), donde *n* es la cantidad de líneas del archivo (proporcional a la cantidad de registros × campos por registro), ya que en el peor caso se recorre el archivo completo una sola vez.

### Búsqueda secuencial (lineal)

Se utiliza en varios puntos del sistema en lugar del operador `in` de Python, siguiendo el enfoque de recorrido explícito de la cátedra:

- `EsOpcionValida`: valida que la opción ingresada exista en la lista de opciones del menú.
- `BuscarProductoPorCodigo` / `BuscarDescuentoPorCodigo`: recorren el archivo hasta encontrar el código buscado o llegar al final.
- `ProductosMasVendidos`: busca si un producto ya fue acumulado en la lista de resultados parciales, para sumarle la cantidad en lugar de duplicarlo.

- **Complejidad:** O(n) en el peor caso (recorrido completo sin encontrar coincidencia), O(1) en el mejor caso (coincidencia en la primera posición).

### Ordenamiento burbuja (Bubble Sort)

Implementado manualmente en `ProductosMasVendidos()` para ordenar la lista de productos vendidos de mayor a menor cantidad, mediante comparaciones e intercambios adyacentes con dos bucles anidados:

```python
i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if acumulado[j][2] < acumulado[j + 1][2]:
            # intercambio
        j = j + 1
    i = i + 1
```

- **Complejidad temporal:** O(n²) en el caso promedio y peor caso, O(n) en el mejor caso si ya estuviera ordenado (aunque esta implementación no incorpora la optimización de corte temprano).
- **Complejidad espacial:** O(1) adicional, ya que el ordenamiento es in-place.
- Se eligió deliberadamente sobre `sorted()` o `list.sort()` para practicar la implementación manual del algoritmo, tal como se exige en la cátedra.

### Validación de entradas sin manejo de excepciones

En lugar de `try/except` (no contemplado como estructura de cátedra en esta etapa), la validación de números enteros y reales se resuelve con funciones booleanas (`EsEnteroValido`, `EsRealValido`) que analizan carácter por carácter usando `isdigit()`, combinadas con un esquema **REPETIR...HASTA QUE sea válido**:

```python
while EsEnteroValido(valor_texto) == False:
    print('Error...')
    valor_texto = input(mensaje)
```

- **Complejidad:** O(k), donde *k* es la longitud del texto ingresado, por cada verificación.

### Registros (estructuras heterogéneas)

`Producto` y `Descuento`, definidos en `registros.py` mediante `@dataclass`, representan el equivalente a un `REGISTRO` de cátedra: una agrupación de campos de distinto tipo (alfanumérico, real, entero) bajo un mismo nombre lógico. Esto permite manipular cada producto o descuento como una unidad, en vez de trabajar con variables sueltas.

### Listas como estructuras temporales

Se usan listas (y listas de listas) como estructuras auxiliares en memoria durante la ejecución:

- `items` en `CalcularTotal` y `CalcularPromociones`: acumula los productos de una venta en curso (`[codprod, nombre, cantidad, subtotal]`).
- `acumulado` en `ProductosMasVendidos`: acumula cantidades vendidas por producto antes de ordenar.
- `ventas` retornado por `LeerVentas`: representa toda la secuencia de ventas históricas, ya convertida en memoria para poder recorrerla varias veces (una vez para acumular, en el caso de las estadísticas).

### Acumuladores y recorridos completos

`EstadisticasDeVentas` recorre **toda** la secuencia de ventas (a diferencia de las búsquedas, que se detienen al primer resultado) para acumular totales de unidades y montos facturados, un patrón clásico de recorrido secuencial completo con acumuladores.

- **Complejidad:** O(n), con *n* la cantidad de ventas registradas.

## Características principales

- Autenticación con dos roles (administrador y operador) y permisos diferenciados.
- Alta de productos y descuentos, restringida al rol administrador.
- Búsqueda de productos por código.
- Cálculo de venta con múltiples productos, validación de stock y descuento opcional aplicado sobre el total.
- Promociones configurables por producto: 2x1, 3x2 (minorista) o 43% de descuento (mayorista, a partir de 4 unidades).
- Registro persistente de cada venta realizada, con fecha.
- Reporte de productos más vendidos, ordenado de mayor a menor.
- Estadísticas generales de ventas: total facturado, unidades vendidas, promedio por venta, primera y última venta registrada.
- Generación automática de un ticket de compra en formato `.txt`, con numeración correlativa persistente.
- Validación robusta de todas las entradas numéricas y de opciones de menú.

## Ejemplos de uso

```
BIENVENIDO A GESTIONSUPER
ingrese _salir_ para terminar el programa
Ingrese el usuario: admin
Ingrese la contraseña: admin123

1) Cargar producto
2) Cargar descuento
3) Buscar producto
4) Calcular total de venta
5) Productos mas vendidos
6) Estadisticas de ventas
7) Promocion mayorista y minorista
0) Salir
Ingrese una opcion: 3
Ingrese el codigo del producto a buscar: 10
Nombre: agua
Precio: $100.0
Stock: 20
Codigo: 10
```

```
Ingrese una opcion: 4
Ingrese el codigo del producto: 89
Ingrese la cantidad: 3
coca cola x3 -> $36000.0
¿Desea agregar otro producto? (s/n): n

Subtotal de la venta: $36000.0
¿Desea aplicar un descuento? (s/n): n
TOTAL A PAGAR: $36000.0

Tiket generado correctamente: ticket_0004.txt
```

## Instalación y ejecución

### Requisitos

- Python 3.x instalado (no requiere librerías externas).

### Pasos

1. Clonar o descargar el repositorio:
   ```bash
   git clone https://github.com/luto-esc/SuperGestion.git
   cd SuperGestion
   ```
2. Ejecutar el programa principal:
   ```bash
   python main.py
   ```
3. Ingresar las credenciales de acceso:
   - Administrador: `admin` / `admin123`
   - Operador: `operador` / `operador123`
4. Navegar el menú ingresando el número de la opción deseada.
5. Para finalizar el programa, ingresar `salir` en el campo de usuario.

> Los archivos `archivo.txt`, `descuentos.txt`, `ventas.txt` y `numeroticket.txt` se crean/actualizan automáticamente en el mismo directorio del proyecto a medida que se usan las distintas opciones.

## Conclusiones

El desarrollo de SuperGestion permitió aplicar de forma concreta los pilares de la materia Algoritmos y Estructuras de Datos: el manejo de **secuencias y archivos** como mecanismo de persistencia, la **búsqueda secuencial** como estrategia central para localizar información, y el **ordenamiento burbuja** como ejemplo de algoritmo clásico implementado sin apoyarse en funciones nativas del lenguaje.

Trabajar sin `try/except` y sin estructuras avanzadas de Python (como diccionarios o `sorted()`) obligó a resolver los mismos problemas con las herramientas vistas en clase, lo cual reforzó la comprensión de conceptos como la validación manual de datos, el recorrido de secuencias con marcas de fin, y la diferencia entre una búsqueda que se detiene al encontrar un resultado y un recorrido que debe completarse por completo para acumular información (como en las estadísticas de ventas).

Asimismo, la separación en módulos (`main.py`, `funciones.py`, `registros.py`) permitió practicar buenas prácticas de organización de código, incluso en un proyecto de complejidad introductoria, separando el control de flujo, la lógica de negocio y el modelado de datos.

## Mejoras futuras

- Incorporar edición y baja de productos y descuentos (actualmente solo se pueden dar de alta y consultar).
- Reemplazar el recorrido lineal de archivos por una estructura indexada en memoria (por ejemplo, un diccionario código→producto) para búsquedas más eficientes en catálogos grandes, evaluando el trade-off académico entre O(n) y O(1).
- Implementar un algoritmo de ordenamiento más eficiente (por ejemplo, quicksort o mergesort) para comparar su complejidad frente al método burbuja actual.
- Agregar control de stock automático al confirmar una venta (actualmente se valida el stock disponible pero no se descuenta del archivo de productos).
- Migrar la persistencia a un formato estructurado (JSON o CSV) o a una base de datos, una vez incorporados esos contenidos en la cursada.
- Incorporar pruebas automatizadas (unitarias) para las funciones de validación y cálculo.
- Registrar el usuario que realizó cada venta, aprovechando el sistema de login ya existente.
