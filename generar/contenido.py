# -*- coding: utf-8 -*-
"""Contenido de las diapositivas: cada paso es (expresion matematica, nota "¿qué hice?")."""

INTEGRANTES = ["Carlos Andrés Infante Rocha", "Juan Pablo González Guzmán"]
NOMBRE = "Infante Rocha  ·  González Guzmán"

OPCION3 = [
    dict(tipo="portada",
         titulo="Teorema de Stokes",
         sub="Ej. 1 (Opción 3):  $\\mathbf{F}=\\langle z,\\,x,\\,y\\rangle$,   $S:\\ z=4-x^2-y^2,\\ z\\geq 0$",
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
    dict(titulo="Ejercicio 2 (mecatrónica): sensor de corriente",
         pasos=[
             (r"Cable de un motor: radio $a=2\ \mathrm{mm}$, corriente $I=10\ \mathrm{A}$", "Datos reales de un motor pequeño"),
             (r"$\mathbf{B}=k\,\langle -y,\ x,\ 0\rangle,\quad k=\dfrac{\mu_0 I}{2\pi a^2}=0.5\ \mathrm{T/m}$", "Campo magnético dentro del cable"),
             (r"$S$: sección del cable $x^2+y^2\leq a^2$, $z=0$, $\mathbf{n}=\mathbf{k}$", "La superficie es el corte del cable"),
         ], durs=[5, 7, 5]),
    dict(tipo="cable3d", titulo="Ejercicio 2: superficie y borde", dur=5),
    dict(titulo="Ejercicio 2: rotacional y superficie",
         pasos=[
             (r"$P=-ky,\quad Q=kx,\quad R=0$", "Componentes del campo"),
             (r"$\mathrm{rot}\,\mathbf{B}=\langle 0,\ 0,\ k-(-k)\rangle=\langle 0,\ 0,\ 2k\rangle=\langle 0,0,1\rangle\ \mathrm{T/m}$", "Rotacional constante"),
             (r"$\iint_S(\mathrm{rot}\,\mathbf{B})\cdot\mathbf{n}\,dS=1\cdot\pi a^2=\pi(0.002)^2$", "Rotacional por el área"),
             (r"$=1.2566\times10^{-5}\ \mathrm{T\cdot m}$", "Resultado camino 1"),
         ], durs=[4, 6, 5, 4], resalta_ultimo=True),
    dict(titulo="Ejercicio 2: integral de línea",
         pasos=[
             (r"$\mathbf{r}(t)=\langle a\cos t,\ a\sin t,\ 0\rangle,\quad \mathbf{r}'=\langle -a\sin t,\ a\cos t,\ 0\rangle$", "Parametricé el borde"),
             (r"$\mathbf{B}\cdot\mathbf{r}'=k a^2(\sin^2 t+\cos^2 t)=k a^2=2\times10^{-6}$", "Producto punto"),
             (r"$\oint_C\mathbf{B}\cdot d\mathbf{r}=2\pi\cdot 2\times10^{-6}=1.2566\times10^{-5}\ \mathrm{T\cdot m}$", "Resultado camino 2"),
         ], durs=[6, 6, 5], resalta_ultimo=True),
    dict(titulo="Ejercicio 2: interpretación",
         pasos=[
             (r"$1.2566\times10^{-5}=\mu_0 I=4\pi\times10^{-7}\cdot 10$   (ley de Ampère)", "Los dos caminos coinciden"),
             (r"La pinza amperimétrica mide la circulación de $\mathbf{B}$", "El sensor rodea el cable"),
             (r"y no importa su forma ni si el cable está centrado:", "Solo cuenta lo que atraviesa"),
             (r"solo la corriente que cruza la superficie.", "Medir sin cortar el cable"),
         ], durs=[6, 5, 5, 5], resalta_primero=True),
]
