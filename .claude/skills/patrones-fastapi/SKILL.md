---
name: patrones-fastapi
description: Aplica el método malo→bueno de esta clase (Especialización en Desarrollo de Software, Universidad del Magdalena) al código de TU propio proyecto final — identifica un problema real, elige el patrón GoF que lo resuelve, documenta el caso malo, refactoriza al caso bueno, y justifica por qué. Úsalo cuando el estudiante pida "aplicar un patrón de diseño", "refactorizar con un patrón", "preparar el proyecto final de patrones" o mencione el mínimo de 5 patrones del curso.
---

# Patrones de diseño: de tu código real a un caso malo→bueno defendible

Este skill replica, sobre TU proyecto, el mismo método que se usó en `estacion-clima`
(`app/` vs. `examples/NN_patron_malo` / `NN_patron_bueno` de este mismo repo — úsalos como
referencia de formato y de nivel de profundidad esperado).

El entregable del curso (Actividad 4, proyecto final, 350 pts) exige: **mínimo 5 patrones GoF**,
cada uno con **caso malo, caso bueno, y la razón de por qué se usó ese patrón**, más una
presentación y el código subido con el link entregado al docente. Este skill existe para que ese
proceso sea metódico, no una excusa para meter patrones donde no hacen falta.

## Regla de oro

**Un patrón se justifica por un problema que ya existe en el código, no al revés.** Si no puedes
señalar la línea exacta donde algo se repite, se acopla, o se vuelve un `if/elif` interminable,
todavía no tienes un caso malo — y sin caso malo no hay nada que justificar.

## Proceso, paso a paso

### 1. Encuentra el problema, no el patrón

Recorre el proyecto del estudiante buscando estas señales concretas (no busques "dónde meter un
patrón" — busca el síntoma primero):

- **Condicionales repetidos por tipo** (`if tipo == "x": ... elif tipo == "y": ...` que aparece
  en más de un lugar) → candidato a **Factory Method**.
- **Acceso a un recurso externo (DB, API, archivo) hardcodeado y repetido** en varias funciones,
  donde cambiar de proveedor implicaría tocar cada una → candidato a **Adapter** o **Bridge**.
- **Un endpoint/función que hace 3+ cosas no relacionadas en el mismo bloque** (validar + guardar
  + notificar + loguear, todo junto) → candidato a **Facade**.
- **Queries o acceso a datos escritos directo en la capa de negocio/HTTP**, difíciles de testear
  sin una base de datos real → candidato a **Repository**.
- **Varias formas de calcular/transformar algo, elegidas con un `if/elif` grande** → candidato a
  **Strategy**.
- **Un cambio de estado que dispara acciones en varios lugares hardcodeados** (enviar email +
  imprimir + loguear, todo llamado a mano) → candidato a **Observer**.
- **El mismo bloque de código (timing, logging, caché, permisos) copiado y pegado en varias
  funciones** → candidato a **Decorator**.

Si el proyecto no tiene ninguna de estas señales todavía, dilo con franqueza — construir un caso
malo de juguete que no representa un problema real del proyecto no cumple el objetivo del curso.

### 2. Preserva el caso malo ANTES de tocar nada

Antes de refactorizar:
1. Copia (o anota vía `git diff`/commit) el código tal como está — este es el "caso malo".
2. Escribe en 2-3 frases **qué problema concreto tiene**: qué se repite, qué se acopla, qué se
   rompe si el proyecto crece. No basta con "no sigue el patrón X" — hay que decir qué duele.

### 3. Refactoriza al caso bueno

Aplica el patrón elegido. Mantén el cambio mínimo y enfocado en resolver el problema del paso 1
— no aproveches para reescribir cosas sin relación. Verifica que el proyecto sigue corriendo
igual que antes desde el punto de vista del usuario (mismos endpoints, mismo comportamiento
observable) — un refactor de patrones no debería cambiar el contrato externo.

### 4. Justifica por escrito

Por cada patrón, un párrafo corto con esta estructura (igual que se explicó en clase):

- **Problema real**: qué encontraste en el paso 1.
- **Patrón aplicado**: cuál y por qué ese y no otro de la misma familia (ej. ¿por qué Adapter y no
  Bridge? ¿por qué Strategy y no un simple `if/elif` bien organizado?).
- **Qué cambió**: 1-2 líneas señalando el antes/después.

### 5. Checklist antes de entregar

- [ ] Mínimo 5 patrones GoF distintos, cada uno con caso malo Y caso bueno documentados.
- [ ] Cada patrón resuelve un problema que existía de verdad en el proyecto (no inventado).
- [ ] El código corre — probado de punta a punta, no solo "compila".
- [ ] Presentación armada (puede seguir el mismo formato malo→bueno diapositiva por diapositiva).
- [ ] Código subido y link entregado al docente.

## Referencia rápida de este repo

- `app/` — los 6 patrones ya aplicados sobre una API real (Factory, Adapter, Facade,
  Repository+Strategy, Observer, Decorator).
- `examples/NN_patron_malo/` y `examples/NN_patron_bueno/`, cada uno con su propio `README.md` —
  el nivel de detalle esperado para "caso malo" y "caso bueno" en la entrega.

No copies estos patrones literalmente a un proyecto que no los necesita — úsalos como plantilla
de *formato y profundidad*, no de contenido.
