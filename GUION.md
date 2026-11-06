# Guion — Teorema de Stokes (un solo video)

**Integrantes:** Carlos Andrés Infante Rocha · Juan Pablo González Guzmán
**Opción 3:** F = ⟨z, x, y⟩, S: z = 4 − x² − y², z ≥ 0, normal hacia arriba → los dos caminos dan **4π**.
**Más:** aplicación en mecatrónica (pinza amperimétrica, ley de Ampère).

## Cómo queda el video

Pantalla dividida: **a la izquierda, quien habla** (la grabación del celular); **a la derecha, el
ejercicio animado**, que se ajusta solo a lo que dure su voz.
Primero habla **Carlos** (partes 1 a 4, seguidas) y después **Juan Pablo** (partes 5 a 8, seguidas).

## Cómo grabar: UN solo video por persona (~2 min cada uno)

- **Carlos** graba un video con las partes **1, 2, 3 y 4** en orden → `carlos.mp4`.
- **Juan Pablo** graba un video con las partes **5, 6, 7 y 8** en orden → `juanpablo.mp4`.
- Entre parte y parte: **quédense callados 2–3 segundos** mirando a la cámara. Con esas pausas
  sincronizo cada parte con su animación.
- Si se equivocan, hagan la pausa y repitan esa parte completa; me avisan cuál repitieron.
- Celular **en vertical**, a la altura de la cara, **luz de frente** (ventana o lámpara delante, no detrás).
- Lugar sin ruido. Pueden mover las manos al explicar.
- Las frases son guía: díganlas **con sus palabras**, no hace falta leerlas exacto.

---

## 🎥 Carlos — partes 1, 2, 3 y 4

**Parte 1 · Presentación (~30 s)**
"Hola, somos Carlos Infante y Juan Pablo González. Escogimos la opción 3: el campo F = ⟨z, x, y⟩ sobre el paraboloide z = 4 − x² − y². La elegimos porque el rotacional y la normal sí importan en el cálculo. Vamos a verificar Stokes: la circulación por el borde debe ser igual al flujo del rotacional."

*(pausa 2–3 s)*

**Parte 2 · Superficie y borde (~40 s)** — *mostrar la mano derecha con el pulgar arriba*
"La superficie es como una cúpula. Para hallar el borde la corté con z = 0 y me queda x² + y² = 4, una circunferencia de radio 2. La normal va hacia arriba, entonces con la mano derecha, pulgar arriba, los dedos dicen que el borde se recorre antihorario. Derivé g y armé n dS = ⟨2x, 2y, 1⟩ dA."

*(pausa 2–3 s)*

**Parte 3 · Rotacional (~25 s)**
"Para el rotacional identifiqué P = z, Q = x, R = y. Apliqué la fórmula y cada componente queda 1 menos 0, así que rot F = ⟨1, 1, 1⟩."

*(pausa 2–3 s)*

**Parte 4 · Camino 1: superficie (~35 s)**
"Primer camino, la superficie: hice el producto punto con la normal y da 2x + 2y + 1. Integro sobre el disco de radio 2. Los términos 2x y 2y se cancelan por simetría, y queda el área del disco: 4π. Ahora Juan Pablo hace el otro camino."

---

## 🎥 Juan Pablo — partes 5, 6, 7 y 8

**Parte 5 · Camino 2: línea (~40 s)**
"Ahora el segundo camino, por la línea: parametricé el borde como r(t) = ⟨2cos t, 2sin t, 0⟩, lo derivé, reemplacé en F, y el producto punto da 4cos²t. Con la identidad del ángulo doble la integral da 4π."

*(pausa 2–3 s)*

**Parte 6 · Conclusión (~20 s)**
"Los dos caminos dan 4π, así que se cumple el teorema. En palabras simples: todo lo que el campo gira dentro de la cúpula se puede medir solo recorriendo el borde."

*(pausa 2–3 s)*

**Parte 7 · Mecatrónica: problema y superficie (~40 s)**
"Como somos de mecatrónica, lo aplicamos a algo real: medir la corriente de un motor con una pinza amperimétrica. Dentro del cable el campo magnético es B = k⟨−y, x, 0⟩. La superficie es el corte del cable y el borde es donde lo abraza la pinza. El rotacional es ⟨0, 0, μ₀I/πa²⟩, y multiplicado por el área πa² da μ₀I."

*(pausa 2–3 s)*

**Parte 8 · Mecatrónica: línea y aplicación (~35 s)**
"Por el borde también da μ₀I; con 10 amperios son unos 1,26 × 10⁻⁵ T·m. Esto es la ley de Ampère: la pinza mide la circulación de B, y por Stokes no importa su forma ni si el cable está centrado, solo la corriente que pasa. Por eso se mide la corriente sin cortar el cable. Gracias."

---

## Alternativa aprobada por el profesor: foto + voz

En vez de video, cada uno manda una **foto de frente** (`carlos.jpg`, `juanpablo.jpg`) y **un solo
audio** con su voz real (`carlos.m4a`, `juanpablo.m4a`), con sus partes en orden y las mismas pausas.

## Para regenerar (si cambia algo)

```bash
pip install matplotlib numpy
python3 generar/render.py    # animaciones por sección + hoja_de_respuestas.pdf
python3 generar/montaje.py   # junta grabaciones/ + animaciones -> salida/video_final.mp4
```
