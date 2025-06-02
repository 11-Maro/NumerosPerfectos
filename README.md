# Búsqueda Distribuida de Números Perfectos

---

**Apertura:** martes, 20 de mayo de 2025, 07:01
**Cierre:** sábado, 7 de junio de 2025, 18:01

---

## Integrantes

- Nicolás Jimenez
- Juan Rosero
- Juan Ocampo
- Manuel Rojas

---

## Utilizando ICE y el Modelo Cliente-Maestro-Trabajadores

---

### Objetivo

Implementar un sistema distribuido para encontrar números perfectos en un rango dado, utilizando el modelo Cliente-Maestro-Trabajadores (Master-Workers) con llamadas asíncronas sobre ICE (Internet Communications Engine). El sistema debe escalar la computación distribuyendo el trabajo entre varios nodos trabajadores y permitir al cliente consultar los resultados de manera eficiente.

---

### Descripción del Problema

Un **número perfecto** es aquel que es igual a la suma de sus divisores propios positivos, excluyéndose a sí mismo.Por ejemplo:

> 28 es perfecto porque 1 + 2 + 4 + 7 + 14 = 28.

El objetivo es encontrar todos los números perfectos en un rango específico, de forma eficiente y paralela.

Debido a la alta complejidad computacional (_O(n√n)_), se utilizará una arquitectura distribuida:

- **Cliente:** Solicita encontrar todos los números perfectos en un rango determinado.
- **Maestro:** Divide el rango en subrangos para ser procesados.
- **Trabajadores:** Procesan cada subrango y devuelven los números perfectos encontrados al maestro.

---

### Requisitos Funcionales

#### Cliente

- Permitir ingresar el rango de búsqueda (inicio y fin).
- Enviar una petición al maestro indicando el rango.
- Esperar de forma asíncrona la respuesta con los números perfectos encontrados.
- Mostrar al usuario el resultado final y el tiempo de ejecución.

#### Maestro

- Recibir las solicitudes del cliente.
- Dividir el rango en partes iguales entre el número de trabajadores disponibles.
- Enviar a cada trabajador un subrango para procesar.
- Recibir las respuestas de los trabajadores de forma asíncrona.
- Consolidar los resultados y enviarlos al cliente.

#### Trabajador

- Recibir un subrango (inicio, fin).
- Calcular todos los números perfectos dentro del subrango.
- Devolver la lista de números perfectos encontrados al maestro.

---

### Implementación Técnica

- Utilizar **ICE (ZeroC)** como middleware para comunicaciones distribuidas.
- Las llamadas entre maestro y trabajadores deben ser **asíncronas**.
- Manejar errores de comunicación y fallos de nodos de forma robusta.
- Permitir modificar fácilmente el número de trabajadores.
- Organizar el código en módulos: **Cliente**, **Maestro**, **Trabajador** y definición de interfaces en **Slice**.

---

### Pruebas y Evaluación

- Realizar pruebas con distintos rangos de búsqueda (por ejemplo: hasta 10,000; 100,000; 1,000,000).
- Evaluar el rendimiento y escalabilidad variando el número de trabajadores (2, 4, 8...).
- Medir y reportar el tiempo total de procesamiento y la eficiencia.
- Verificar que el sistema entrega correctamente los números perfectos en cada rango.

---

### Entregables

1. **Informe final en PDF** que incluya:
   - Descripción del problema y análisis del algoritmo utilizado.
   - Arquitectura general del sistema distribuido.
   - Detalle del diseño Cliente-Maestro-Trabajadores con ICE.
   - Explicación del mecanismo de distribución del rango y coordinación.
   - Resultados experimentales y análisis de rendimiento.
   - Conclusiones y posibles mejoras.
2. **Código fuente completo:**
   - Interfaces Slice.
   - Implementaciones del Cliente, Maestro y Trabajadores.
   - Scripts para compilar y ejecutar el sistema distribuido.
3. **Instrucciones de ejecución:**
   - Detalles para compilar el Slice.
   - Cómo correr cada componente.
   - Parámetros que deben ingresarse al cliente.

---

### Notas Adicionales

- Se valorará positivamente la **modularidad**, **claridad del código** y uso correcto de las interfaces ICE.
- Se recomienda implementar primero una versión **sincrónica** para pruebas y luego transformarla a asincronía.
- Puede utilizar herramientas de **logging** para ver el progreso de cada trabajador.
- Si se desea, puede implementar una **interfaz gráfica** para el cliente (opcional).
