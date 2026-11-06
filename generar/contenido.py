# -*- coding: utf-8 -*-
"""Contenido de las diapositivas: cada paso es (expresion matematica, nota "¿qué hice?")."""

NOMBRE = "Tu nombre aquí"  # <- cambia esto por tu nombre completo

OPCION3 = [
    dict(tipo="portada",
         titulo="Teorema de Stokes",
         sub="Opción 3:  $\\mathbf{F}=\\langle z,\\,x,\\,y\\rangle$,   $S:\\ z=4-x^2-y^2,\\ z\\geq 0$",
         dur=8),
    dict(titulo="1. El problema y el teorema",
         pasos=[
             (r"$\mathbf{F}=\langle z,\ x,\ y\rangle$", "Este es el campo vectorial"),
             (r"$S:\ z=4-x^2-y^2,\quad z\geq 0,\quad \mathbf{n}$ hacia arriba", "La superficie: un paraboloide (una cúpula)"),
             (r"$\oint_C \mathbf{F}\cdot d\mathbf{r}\ =\ \iint_S (\mathrm{rot}\,\mathbf{F})\cdot\mathbf{n}\,dS$", "Stokes: circulación en el borde = flujo del rotacional"),
         ], durs=[6, 7, 9]),
    dict(tipo="superficie3d", titulo="2. Superficie, normal y borde", dur=9),
    dict(titulo="2. Superficie, normal y borde",
         pasos=[
             (r"$z=0\ \Rightarrow\ 4-x^2-y^2=0\ \Rightarrow\ x^2+y^2=4$", "Corté la cúpula con el piso z = 0"),
             (r"$C:\ $circunferencia de radio $2$ en el plano $z=0$", "Ese corte es el borde C"),
             (r"$\mathbf{n}$ arriba $\Rightarrow$ $C$ antihorario (visto desde arriba)", "Regla de la mano derecha: pulgar = normal"),
             (r"$g=4-x^2-y^2,\quad g_x=-2x,\quad g_y=-2y$", "Derivé la función de la superficie"),
             (r"$\mathbf{n}\,dS=\langle -g_x,\,-g_y,\,1\rangle\,dA=\langle 2x,\,2y,\,1\rangle\,dA$", "Armé el vector normal (hacia arriba)"),
         ], durs=[7, 6, 8, 6, 8]),
    dict(titulo="3. El rotacional",
         pasos=[
             (r"$P=z,\qquad Q=x,\qquad R=y$", "Identifiqué las componentes de F"),
             (r"$\mathrm{rot}\,\mathbf{F}=\left\langle R_y-Q_z,\ \ P_z-R_x,\ \ Q_x-P_y\right\rangle$", "Escribí la fórmula del rotacional"),
             (r"$=\langle 1-0,\ \ 1-0,\ \ 1-0\rangle$", "Cada derivada da 1 o 0"),
             (r"$\mathrm{rot}\,\mathbf{F}=\langle 1,\ 1,\ 1\rangle$", "El campo gira igual en todo punto"),
         ], durs=[6, 7, 7, 6], resalta_ultimo=True),
    dict(titulo="4. Camino 1: integral de superficie",
         pasos=[
             (r"$(\mathrm{rot}\,\mathbf{F})\cdot\mathbf{n}\,dS=\langle 1,1,1\rangle\cdot\langle 2x,2y,1\rangle\,dA$", "Producto punto: rotacional con la normal"),
             (r"$=(2x+2y+1)\,dA$, sobre el disco $D:\ x^2+y^2\leq 4$", "La sombra de la cúpula en el piso es el disco D"),
             (r"$\iint_D 2x\,dA=0,\qquad \iint_D 2y\,dA=0$", "Por simetría: lo positivo cancela lo negativo"),
             (r"$\iint_D 1\,dA=\mathrm{Área}(D)=\pi(2)^2=4\pi$", "Solo queda el área del disco"),
             (r"$\iint_S(\mathrm{rot}\,\mathbf{F})\cdot\mathbf{n}\,dS=4\pi$", "Resultado del camino 1"),
         ], durs=[7, 7, 8, 7, 5], resalta_ultimo=True),
    dict(titulo="5. Camino 2: integral de línea",
         pasos=[
             (r"$\mathbf{r}(t)=\langle 2\cos t,\ 2\sin t,\ 0\rangle,\quad 0\leq t\leq 2\pi$", "Parametricé el borde (antihorario)"),
             (r"$\mathbf{r}'(t)=\langle -2\sin t,\ 2\cos t,\ 0\rangle$", "Derivé la parametrización"),
             (r"$\mathbf{F}(\mathbf{r}(t))=\langle z,x,y\rangle=\langle 0,\ 2\cos t,\ 2\sin t\rangle$", "Reemplacé x, y, z en el campo"),
             (r"$\mathbf{F}\cdot\mathbf{r}'=0+4\cos^2 t+0=4\cos^2 t$", "Producto punto"),
             (r"$\int_0^{2\pi}4\cos^2 t\,dt=4\int_0^{2\pi}\frac{1+\cos 2t}{2}\,dt=4\pi$", "Identidad del ángulo doble e integré"),
             (r"$\oint_C\mathbf{F}\cdot d\mathbf{r}=4\pi$", "Resultado del camino 2"),
         ], durs=[7, 5, 7, 6, 9, 5], resalta_ultimo=True),
    dict(titulo="6. Conclusión",
         pasos=[
             (r"$\oint_C\mathbf{F}\cdot d\mathbf{r}=4\pi\ \ =\ \ \iint_S(\mathrm{rot}\,\mathbf{F})\cdot\mathbf{n}\,dS=4\pi$", "Los dos caminos coinciden"),
             (r"El giro total del campo dentro de la cúpula", "Lo que gira por dentro…"),
             (r"es igual a lo que se acumula recorriendo su borde.", "…se ve completo en el borde"),
         ], durs=[8, 6, 7], resalta_primero=True),
]

MECATRONICA = [
    dict(tipo="portada",
         titulo="Stokes en mecatrónica",
         sub="La pinza amperimétrica y la ley de Ampère",
         dur=7),
    dict(titulo="1. El problema",
         pasos=[
             (r"Cable de un motor: radio $a$, corriente $I$ a lo largo del eje $z$", "Situación real: medir la corriente de un motor"),
             (r"$\mathbf{B}=\dfrac{\mu_0 I}{2\pi a^2}\,\langle -y,\ x,\ 0\rangle$   (dentro del cable)", "Campo magnético dentro del conductor"),
             (r"Meta: calcular $\oint_C\mathbf{B}\cdot d\mathbf{r}$ alrededor del cable", "Eso es lo que mide una pinza amperimétrica"),
         ], durs=[7, 8, 6]),
    dict(tipo="cable3d", titulo="2. Superficie y borde", dur=7),
    dict(titulo="2. Rotacional y camino 1 (superficie)",
         pasos=[
             (r"$\mathbf{B}=k\,\langle -y,\ x,\ 0\rangle$   con   $k=\dfrac{\mu_0 I}{2\pi a^2}$", "Llamé k a la constante"),
             (r"$\mathrm{rot}\,\mathbf{B}=\langle 0,\ 0,\ k(1-(-1))\rangle=\left\langle 0,\ 0,\ \dfrac{\mu_0 I}{\pi a^2}\right\rangle$", "Rotacional (como en la Fase 3)"),
             (r"$S$: sección del cable $x^2+y^2\leq a^2$ en $z=0$,   $\mathbf{n}=\mathbf{k}$", "La superficie es el corte transversal"),
             (r"$\iint_S(\mathrm{rot}\,\mathbf{B})\cdot\mathbf{n}\,dS=\dfrac{\mu_0 I}{\pi a^2}\cdot\pi a^2=\mu_0 I$", "Rotacional constante × área"),
         ], durs=[6, 8, 7, 8], resalta_ultimo=True),
    dict(titulo="3. Camino 2 (línea) y números",
         pasos=[
             (r"$\mathbf{r}(t)=\langle a\cos t,\ a\sin t,\ 0\rangle,\qquad \mathbf{B}\cdot\mathbf{r}'=k\,a^2=\dfrac{\mu_0 I}{2\pi}$", "Parametricé el borde del cable"),
             (r"$\oint_C\mathbf{B}\cdot d\mathbf{r}=\int_0^{2\pi}\dfrac{\mu_0 I}{2\pi}\,dt=\mu_0 I$", "Coincide con la superficie"),
             (r"Con $I=10\ \mathrm{A}$:   $\mu_0 I=4\pi\times10^{-7}\cdot 10\approx 1.26\times 10^{-5}\ \mathrm{T\cdot m}$", "Valor numérico"),
         ], durs=[8, 7, 8], resalta_segundo=True),
    dict(titulo="4. ¿Para qué sirve?",
         pasos=[
             (r"$\oint_C\mathbf{B}\cdot d\mathbf{r}=\mu_0 I_{\mathrm{encerrada}}$   (ley de Ampère = Stokes)", "Stokes aplicado al campo magnético"),
             (r"La pinza mide la circulación de $\mathbf{B}$ en su borde", "El sensor rodea el cable"),
             (r"y no importa su forma ni si el cable está centrado:", "Solo cuenta la corriente que atraviesa"),
             (r"solo cuenta la corriente $I$ que cruza la superficie.", "Medición de corriente sin cortar el cable"),
         ], durs=[8, 6, 6, 7], resalta_primero=True),
]
