# Guion — Teorema de Stokes (un solo video)

**Integrantes:** Carlos Andrés Infante Rocha · Juan Pablo González Guzmán
**Opción 3:** F = ⟨z, x, y⟩, S: z = 4 − x² − y², z ≥ 0, normal hacia arriba → los dos caminos dan **4π**.
**Más:** aplicación en mecatrónica (pinza amperimétrica, ley de Ampère).

## Cómo queda el video

Pantalla dividida: **a la izquierda, ustedes** (la grabación del celular); **a la derecha, el ejercicio
animado**, que se ajusta solo a lo que dure su voz. Vista previa: `salida/video_final.mp4`.

## Cómo grabar (cada uno, ~2 min en total)

- Celular **en vertical**, a la altura de la cara, **luz de frente** (ventana o lámpara delante, no detrás).
- Lugar sin ruido. Pueden mover las manos al explicar; en el clip 02 muestren la **mano derecha con el pulgar arriba**.
- **Un clip por fila** de la tabla, con el nombre exacto (ej. `01_carlos.mp4`). Mándenlos por este chat.
- Duración sugerida entre paréntesis. Si se pasan un poco no importa: el total debe quedar bajo **5:00**.
- Las frases son guía: díganlas **con sus palabras**, no hace falta leerlas exacto.

| Clip | Quién | Qué decir |
|---|---|---|
| `01_carlos` (~30 s) | Carlos | "Hola, somos Carlos Infante y Juan Pablo González. Escogimos la opción 3: el campo F = ⟨z, x, y⟩ sobre el paraboloide z = 4 − x² − y². La elegimos porque el rotacional y la normal sí importan en el cálculo. Vamos a verificar Stokes: la circulación por el borde debe ser igual al flujo del rotacional." |
| `02_juanpablo` (~40 s) | Juan Pablo | "La superficie es como una cúpula. Para hallar el borde la corté con z = 0 y me queda x² + y² = 4, una circunferencia de radio 2. La normal va hacia arriba, entonces con la mano derecha —pulgar arriba— los dedos dicen que el borde se recorre antihorario. Derivé g y armé n dS = ⟨2x, 2y, 1⟩ dA." |
| `03_carlos` (~25 s) | Carlos | "Para el rotacional identifiqué P = z, Q = x, R = y. Apliqué la fórmula y cada componente queda 1 menos 0, así que rot F = ⟨1, 1, 1⟩." |
| `04_juanpablo` (~35 s) | Juan Pablo | "Primer camino, la superficie: hice el producto punto con la normal y da 2x + 2y + 1. Integro sobre el disco de radio 2. Los términos 2x y 2y se cancelan por simetría, y queda el área del disco: 4π." |
| `05_carlos` (~40 s) | Carlos | "Segundo camino, la línea: parametricé el borde como r(t) = ⟨2cos t, 2sin t, 0⟩, lo derivé, reemplacé en F, y el producto punto da 4cos²t. Con la identidad del ángulo doble la integral da 4π." |
| `06_juanpablo` (~20 s) | Juan Pablo | "Los dos caminos dan 4π, así que se cumple el teorema. En palabras simples: todo lo que el campo gira dentro de la cúpula se puede medir solo recorriendo el borde." |
| `07_carlos` (~40 s) | Carlos | "Como somos de mecatrónica, lo aplicamos a algo real: medir la corriente de un motor con una pinza amperimétrica. Dentro del cable el campo magnético es B = k⟨−y, x, 0⟩. La superficie es el corte del cable y el borde es donde lo abraza la pinza. El rotacional es ⟨0, 0, μ₀I/πa²⟩, y por el área πa² da μ₀I." |
| `08_juanpablo` (~35 s) | Juan Pablo | "Por el borde también da μ₀I; con 10 amperios son unos 1,26 × 10⁻⁵ T·m. Esto es la ley de Ampère: la pinza mide la circulación de B, y por Stokes no importa su forma ni si el cable está centrado, solo la corriente que pasa. Por eso se mide la corriente sin cortar el cable. Gracias." |

## Para regenerar (si cambia algo)

```bash
pip install matplotlib numpy
python3 generar/render.py    # animaciones por sección + hoja_de_respuestas.pdf
python3 generar/montaje.py   # junta grabaciones/ + animaciones -> salida/video_final.mp4
```
