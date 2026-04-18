
# Función CERRADURA para Ítems LR(0)

## Descripción

Implementación de la función CERRADURA (Closure) para conjuntos de ítems LR(0) como parte del proceso de construcción de autómatas LR(0) para análisis sintáctico ascendente.

Este programa permite calcular automáticamente la cerradura de cualquier conjunto de ítems LR(0) dada una gramática libre de contexto.

## Requisitos

- Python 3.6 o superior
- No requiere bibliotecas externas

## Estructura del Proyecto

```
.
├── cerradura_lr0.py      # Implementación principal
├── README.md             # Este archivo
└── video_explicativo/    # Carpeta para el video (ver sección Video)
```

## Uso

### Ejecución básica

```bash
python cerradura_lr0.py
```

### Definir una gramática

```python
g = Gramatica({
    "S'": [["S"]],
    "S":  [["S", "S", "+"], ["S", "S", "*"], ["a"]]
})
```

### Calcular cerradura

```python
items_iniciales = [ItemLR0("S'", ["S"], 0)]
resultado = mostrar_cerradura(items_iniciales, g, "I0")
```

## Gramáticas de prueba incluidas

El programa incluye cuatro gramáticas de prueba:

1. **Gramática 1:** `S → SS+ | SS* | a`
2. **Gramática 2:** `S → (S) | ε`
3. **Gramática 3:** `S → L, L → aL | a`
4. **Ejemplo de clase:** `E → E+T | T, T → T*F | F, F → (E) | id`

## Formato de salida

Para cada conjunto de ítems, el programa muestra:

- Los ítems de entrada (núcleo)
- El proceso paso a paso de cálculo de la cerradura
- Cada ítem agregado durante el proceso
- La cerradura completa con los ítems del núcleo marcados

### Ejemplo de salida

```
I0 = CERRADURA({S' → •S})

Items de entrada:
  S' → • S

  Calculando cerradura...
  Items iniciales:
    S' → • S

  Iteración 1: Agregando S → • S S +
    desde S' → • S
  Iteración 1: Agregando S → • S S *
    desde S' → • S
  Iteración 1: Agregando S → • a
    desde S' → • S

  Tamaño de cerradura: 4 items

Cerradura completa:
  S' → • S  ← núcleo
  S → • S S +
  S → • S S *
  S → • a
```

## Regla de cerradura implementada

```
Si A → α • B β está en el conjunto y B → γ es una producción,
entonces agregar B → • γ al conjunto.
```

El algoritmo se repite hasta que no se puedan agregar más ítems.

## Video Explicativo

[![Video Explicativo](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://youtu.be/VIDEO_ID)

**Contenido del video:**
- Explicación del concepto de cerradura LR(0)
- Recorrido por la estructura del código
- Demostración de ejecución con las gramáticas de prueba
- Análisis de resultados obtenidos

