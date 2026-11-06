# Guion del video — Teorema de Stokes

**Opción elegida: 3** → F = ⟨z, x, y⟩, S: z = 4 − x² − y², z ≥ 0, normal hacia arriba.
Resultado: los dos caminos dan **4π**.

> **Requisito de la guía:** cada integrante aparece en cámara **con el rostro visible**
> (iluminación frontal), habla al menos una vez, y explica con sus propias palabras.
> Video MP4 de **máximo 5 minutos**, nombres en la primera pantalla.

## Cómo armarlo

1. Grábate **de frente** (celular horizontal) para la presentación y la conclusión.
2. Para la parte de cálculos usa `salida/video_opcion3.mp4` como pantalla y graba tu voz
   encima (o grábate con la mano escribiendo/señalando la hoja).
3. Envíame tus grabaciones y yo las uno con las animaciones, corto silencios y exporto el MP4.

Las frases son una guía: dilas **con tus palabras**, no hace falta leerlas exacto.

---

## Video principal (Opción 3) — ~4:00

| Tiempo | En pantalla | Qué decir |
|---|---|---|
| 0:00–0:20 | **Tú en cámara** (rostro) | "Hola, soy ___. Escogí la opción 3 porque el rotacional no es constante en una sola dirección y la normal sí cambia el cálculo, así que se ve mejor cómo funciona Stokes." |
| 0:20–0:28 | Portada (animación) | — |
| 0:28–0:50 | 1. El problema | "Tenemos el campo F = ⟨z, x, y⟩ y la superficie es un paraboloide, como una cúpula, que llega a z = 4. Stokes dice que la circulación por el borde es igual al flujo del rotacional por la superficie." |
| 0:50–1:35 | 2. Superficie y borde (3D + pasos) | "Para hallar el borde corté la cúpula con z = 0: me queda x² + y² = 4, una circunferencia de radio 2. Como la normal va hacia arriba, con la mano derecha —**pulgar arriba** (muéstralo con tu mano)— los dedos indican que C se recorre antihorario. Luego derivé g y armé n dS = ⟨2x, 2y, 1⟩ dA." |
| 1:35–2:01 | 3. Rotacional | "Identifiqué P = z, Q = x, R = y. Aplicando la fórmula cada componente da 1 − 0, entonces rot F = ⟨1, 1, 1⟩." |
| 2:01–2:35 | 4. Camino 1 | "Hago el producto punto con la normal: 2x + 2y + 1. Integro sobre el disco de radio 2. Los términos 2x y 2y se cancelan por simetría, y lo que queda es el área del disco, 4π." |
| 2:35–3:14 | 5. Camino 2 | "Ahora por el borde: parametricé r(t) = ⟨2cos t, 2sin t, 0⟩, derivé, reemplacé en F y el producto punto da 4cos²t. Con la identidad del ángulo doble la integral da 4π." |
| 3:14–3:35 | 6. Conclusión | "Los dos caminos dan 4π, entonces se verifica el teorema." |
| 3:35–4:00 | **Tú en cámara** | "En palabras simples: todo lo que el campo gira dentro de la cúpula se puede medir solo recorriendo el borde. No importa la forma de la superficie, importa su borde." |

## Segmento de mecatrónica — ~1:00 a 1:50

Si lo pones en el mismo video, acórtalo para no pasar de 5 min (o entrégalo aparte).

| En pantalla | Qué decir |
|---|---|
| Portada / 1. El problema | "Como estudiante de mecatrónica, apliqué Stokes a algo real: medir la corriente de un motor con una pinza amperimétrica. Dentro del cable el campo magnético es B = k⟨−y, x, 0⟩." |
| 2. Superficie y borde (3D) | "La superficie es el corte del cable y el borde es donde lo abraza la pinza." |
| Rotacional y camino 1 | "El rotacional es ⟨0, 0, μ₀I/(πa²)⟩; multiplicado por el área πa² da μ₀I." |
| Camino 2 y números | "Por el borde también da μ₀I. Con 10 amperios son unos 1,26 × 10⁻⁵ T·m." |
| ¿Para qué sirve? (**tú en cámara** al final) | "Eso es la ley de Ampère: la pinza mide la circulación de B, y por Stokes no importa su forma ni si el cable está centrado; solo cuenta la corriente que pasa. Por eso puedo medir corriente sin cortar el cable." |
