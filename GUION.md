# Guion — Teorema de Stokes (un solo video)

**Integrantes:** Carlos Andrés Infante Rocha · Juan Pablo González Guzmán
**Ejercicio 1 (Opción 3):** F = ⟨z, x, y⟩, S: z = 4 − x² − y², z ≥ 0, normal hacia arriba → los dos caminos dan **4π**.
**Ejercicio 2 (propio, mecatrónica):** sensor de corriente en el cable de un motor, a = 2 mm, I = 10 A → los dos caminos dan **1,2566 × 10⁻⁵ T·m = μ₀I**.

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
- Las frases son guía: díganlas **con sus palabras**. Lean a ritmo normal (~130 palabras/min); la animación se ajusta sola a lo que dure su voz, así que no se desincroniza.

---

## 🎥 Carlos — partes 1, 2, 3 y 4 (~2:20)

**Parte 1 · Presentación y Ejercicio 1 (~40 s)**
"Hola, somos Carlos Andrés Infante Rocha y Juan Pablo González Guzmán, estudiantes de ingeniería mecatrónica. En este video vamos a resolver dos ejercicios con el Teorema de Stokes. El primero es la opción 3 de la guía: el campo F igual a z, x, y, sobre el paraboloide z igual a 4 menos x al cuadrado menos y al cuadrado, con la normal hacia arriba. El segundo ejercicio lo planteamos nosotros, aplicado a mecatrónica. Stokes dice que la circulación por el borde es igual al flujo del rotacional, y lo vamos a comprobar por dos caminos."

*(silencio 3 s)*

**Parte 2 · Superficie, normal y borde (~45 s) — mano derecha, pulgar arriba**
"La superficie es como una cúpula con el punto más alto en z igual a 4. Para encontrar el borde la corté con el piso, z igual a cero. Queda x al cuadrado más y al cuadrado igual a 4: una circunferencia de radio 2 en el plano z igual a cero. Como la normal va hacia arriba, uso la regla de la mano derecha: pulgar arriba, y los dedos dicen que el borde se recorre en sentido antihorario visto desde arriba. Para la normal derivé g: g sub x es menos 2x y g sub y es menos 2y, entonces n dS es 2x, 2y, 1, por dA."

*(silencio 3 s)*

**Parte 3 · Rotacional (~30 s)**
"Ahora el rotacional. Identifiqué las componentes del campo: P igual a z, Q igual a x y R igual a y. La fórmula es R sub y menos Q sub z, P sub z menos R sub x, y Q sub x menos P sub y. Cada componente queda 1 menos 0. Entonces el rotacional de F es 1, 1, 1. Es constante: el campo gira igual en todos los puntos."

*(silencio 3 s)*

**Parte 4 · Camino 1: superficie (~40 s)**
"Primer camino, la integral de superficie. Hago el producto punto entre el rotacional, 1, 1, 1, y la normal, 2x, 2y, 1. Eso da 2x más 2y más 1. Integro sobre la sombra de la cúpula, el disco de radio 2. Las integrales de 2x y de 2y dan cero por simetría. Solo queda la integral de 1, que es el área del disco: pi por 2 al cuadrado, o sea 4 pi. Ahora Juan Pablo hace el otro camino."

---

## 🎥 Juan Pablo — partes 5, 6, 7 y 8 (~2:25)

**Parte 5 · Ejercicio 1, camino 2: línea (~45 s)**
"Gracias, Carlos. Ahora el segundo camino, la integral de línea por el borde. Parametricé la circunferencia como r de t igual a 2 coseno de t, 2 seno de t, 0, con t de cero a 2 pi, que es el sentido antihorario. La derivada es menos 2 seno de t, 2 coseno de t, 0. Reemplacé en el campo y, como en el borde z vale cero, queda 0, 2 coseno de t, 2 seno de t. El producto punto da 4 coseno cuadrado de t. Con la identidad del ángulo doble, la integral de 0 a 2 pi da 4 pi."

*(silencio 3 s)*

**Parte 6 · Ejercicio 1, conclusión (~25 s)**
"Los dos caminos dan 4 pi, así que se cumple el Teorema de Stokes. En palabras simples: todo lo que el campo gira dentro de la cúpula se puede medir solamente recorriendo su borde."

*(silencio 3 s)*

**Parte 7 · Ejercicio 2 (mecatrónica): planteamiento y superficie (~50 s)**
"El segundo ejercicio es de mecatrónica. Queremos medir la corriente del cable de un motor con una pinza, sin cortarlo. El cable tiene radio a igual a 2 milímetros y lleva 10 amperios. Dentro del cable el campo magnético es B igual a k por menos y, x, 0, donde k es mu cero por I sobre 2 pi a al cuadrado; con nuestros datos k da 0,5 tesla por metro. La superficie es el corte del cable y el borde es donde la pinza lo abraza. El rotacional es 2k, o sea 1 tesla por metro. Multiplicado por el área, pi por 0,002 al cuadrado, da 1,2566 por 10 a la menos 5 tesla metro."

*(silencio 3 s)*

**Parte 8 · Ejercicio 2: línea e interpretación (~45 s)**
"Por el otro camino parametricé el borde como a coseno de t, a seno de t, 0. El producto punto de B con la derivada da k por a al cuadrado al cuadrado, que es 2 por 10 a la menos 6. Por 2 pi da otra vez 1,2566 por 10 a la menos 5. Ese número es exactamente mu cero por I: es la ley de Ampère, que sale directo de Stokes. Por eso una pinza amperimétrica funciona: mide la circulación del campo magnético alrededor del cable; por Stokes no importa su forma ni si el cable está centrado, solo la corriente que pasa. Gracias por su atención."

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
