# -*- coding: utf-8 -*-
"""Genera los videos de apoyo (sin voz) y la hoja de respuestas en PDF.

Uso:  python3 generar/render.py
Salida en ./salida/
"""
import os
import shutil
import subprocess
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from contenido import NOMBRE, INTEGRANTES, OPCION3, MECATRONICA  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "salida")
TMP = os.path.join(RAIZ, ".tmp_frames")
FPS = 24
W, H = 19.2, 10.8  # pulgadas -> 1920x1080 a dpi 100

FONDO = "#FBFAF6"
TINTA = "#1F2A37"
VERDE = "#2F6B4F"
AZUL = "#1F5A8A"
NOTA = "#8A4B12"
RESALTE = "#FFF2B3"
CAJA = "#E3F1E8"

plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "DejaVu Serif",
    "text.color": TINTA,
})


# ---------------------------------------------------------------- diapositivas
def _marco(fig, titulo, pie):
    fig.patch.set_facecolor(FONDO)
    fig.add_artist(FancyBboxPatch((0, 0.89), 1, 0.11, boxstyle="square,pad=0",
                                  transform=fig.transFigure, color=VERDE))
    fig.text(0.04, 0.945, titulo, fontsize=40, color="white", va="center", weight="bold")
    fig.text(0.04, 0.03, pie, fontsize=18, color="#6B7280")


def diapositiva(sec, n_visibles, pie, ruta):
    fig = plt.figure(figsize=(W, H), dpi=100)
    _marco(fig, sec["titulo"], pie)
    pasos = sec["pasos"]
    alto = 0.74 / max(len(pasos), 4)
    fig.text(0.705, 0.84, "¿Qué hice?", fontsize=24, color=NOTA, style="italic", weight="bold")
    for i, (mat, nota) in enumerate(pasos[:n_visibles]):
        y = 0.80 - alto * (i + 0.5)
        nuevo = i == n_visibles - 1
        caja = (sec.get("resalta_ultimo") and i == len(pasos) - 1) or \
               (sec.get("resalta_primero") and i == 0) or \
               (sec.get("resalta_segundo") and i == 1)
        if caja:
            fig.add_artist(FancyBboxPatch((0.035, y - alto * 0.38), 0.63, alto * 0.76,
                                          boxstyle="round,pad=0.004", transform=fig.transFigure,
                                          facecolor=CAJA, edgecolor=VERDE, lw=3))
        elif nuevo:
            fig.add_artist(FancyBboxPatch((0.035, y - alto * 0.38), 0.63, alto * 0.76,
                                          boxstyle="round,pad=0.004", transform=fig.transFigure,
                                          facecolor=RESALTE, edgecolor="none"))
        fig.text(0.05, y, mat, fontsize=32, va="center")
        fig.text(0.705, y, ("→ " if nuevo else "") + nota, fontsize=20, va="center",
                 color=NOTA if nuevo else "#9CA3AF", wrap=True)
    fig.savefig(ruta, facecolor=FONDO)
    plt.close(fig)


def portada(sec, pie, ruta):
    fig = plt.figure(figsize=(W, H), dpi=100)
    fig.patch.set_facecolor(VERDE)
    fig.text(0.5, 0.62, sec["titulo"], fontsize=80, color="white", ha="center", weight="bold")
    fig.text(0.5, 0.48, sec["sub"], fontsize=36, color="white", ha="center")
    for i, n in enumerate(INTEGRANTES):
        fig.text(0.5, 0.33 - 0.07 * i, n, fontsize=40, color="#FFE9A8", ha="center")
    fig.text(0.5, 0.12, "Cálculo vectorial — Guía: Teorema de Stokes", fontsize=24,
             color="#D1E7DA", ha="center")
    fig.savefig(ruta, facecolor=VERDE)
    plt.close(fig)


# ---------------------------------------------------------------- figuras 3D
def _flecha_circ(ax, R, z, t0, color):
    t = np.linspace(t0, t0 + 0.45, 2)
    x, y = R * np.cos(t), R * np.sin(t)
    ax.quiver(x[0], y[0], z, x[1] - x[0], y[1] - y[0], 0, color=color, lw=6,
              arrow_length_ratio=1.2)


def fig_paraboloide(azim, ruta=None, fig=None, rect=(0.0, 0.03, 0.62, 0.86)):
    propia = fig is None
    if propia:
        fig = plt.figure(figsize=(W, H), dpi=100)
        _marco(fig, "2. Superficie, normal y borde", f"{NOMBRE}  ·  Opción 3")
        fig.text(0.62, 0.74, r"$S:\ z=4-x^2-y^2,\ \ z\geq 0$", fontsize=34)
        fig.text(0.62, 0.62, r"Borde $C$: $x^2+y^2=4$, $z=0$", fontsize=32, color="#B91C1C")
        fig.text(0.62, 0.50, r"Normal $\mathbf{n}$ hacia arriba", fontsize=32, color=AZUL)
        fig.text(0.62, 0.38, "Mano derecha: pulgar arriba,", fontsize=28, color=NOTA)
        fig.text(0.62, 0.32, "dedos → C antihorario", fontsize=28, color=NOTA)
    ax = fig.add_axes(rect, projection="3d")
    ax.set_facecolor(FONDO)
    r = np.linspace(0, 2, 30)
    t = np.linspace(0, 2 * np.pi, 60)
    R, T = np.meshgrid(r, t)
    X, Y = R * np.cos(T), R * np.sin(T)
    ax.plot_surface(X, Y, 4 - R ** 2, cmap="viridis", alpha=0.75, linewidth=0)
    ax.plot_surface(X, Y, 0 * R, color="#9CA3AF", alpha=0.18, linewidth=0)
    ax.plot(2 * np.cos(t), 2 * np.sin(t), 0 * t, color="#B91C1C", lw=4)
    for t0 in (0.3, 0.3 + 2 * np.pi / 3, 0.3 + 4 * np.pi / 3):
        _flecha_circ(ax, 2, 0, t0, "#B91C1C")
    ax.quiver(0, 0, 4, 0, 0, 1.6, color=AZUL, lw=4, arrow_length_ratio=0.25)
    ax.text(0.15, 0, 5.7, r"$\mathbf{n}$", color=AZUL, fontsize=30)
    ax.text(2.3, -0.4, 0.2, r"$C$", color="#B91C1C", fontsize=30)
    ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5); ax.set_zlim(0, 5.5)
    ax.set_xlabel("x", fontsize=18); ax.set_ylabel("y", fontsize=18); ax.set_zlabel("z", fontsize=18)
    ax.view_init(elev=24, azim=azim)
    ax.set_box_aspect((1, 1, 0.9))
    if propia:
        fig.savefig(ruta, facecolor=FONDO)
        plt.close(fig)


def fig_cable(azim, ruta=None, fig=None, rect=(0.0, 0.03, 0.62, 0.86)):
    propia = fig is None
    if propia:
        fig = plt.figure(figsize=(W, H), dpi=100)
        _marco(fig, "Ejercicio 2: superficie y borde", f"{NOMBRE}  ·  Ejercicio 2 (mecatrónica)")
        fig.text(0.62, 0.74, r"Corriente $I$ por el eje $z$", fontsize=32, color="#B45309")
        fig.text(0.62, 0.62, r"$S$: sección del cable (radio $a$)", fontsize=28)
        fig.text(0.62, 0.50, r"Borde $C$: donde abraza la pinza", fontsize=30, color="#B91C1C")
        fig.text(0.62, 0.38, r"$\mathbf{n}=\mathbf{k}$  → $C$ antihorario", fontsize=30, color=AZUL)
    ax = fig.add_axes(rect, projection="3d")
    ax.set_facecolor(FONDO)
    t = np.linspace(0, 2 * np.pi, 60)
    z = np.linspace(-2, 2, 10)
    T, Z = np.meshgrid(t, z)
    ax.plot_surface(np.cos(T), np.sin(T), Z, color="#D97706", alpha=0.35, linewidth=0)
    r = np.linspace(0, 1, 10)
    Rr, Tt = np.meshgrid(r, t)
    ax.plot_surface(Rr * np.cos(Tt), Rr * np.sin(Tt), 0 * Rr, color="#60A5FA", alpha=0.55, linewidth=0)
    ax.plot(np.cos(t), np.sin(t), 0 * t, color="#B91C1C", lw=4)
    for t0 in (0.3, 0.3 + 2 * np.pi / 3, 0.3 + 4 * np.pi / 3):
        _flecha_circ(ax, 1, 0, t0, "#B91C1C")
    ax.quiver(0, 0, -2.6, 0, 0, 5.2, color="#B45309", lw=4, arrow_length_ratio=0.08)
    ax.text(0.15, 0, 2.8, r"$I$", color="#B45309", fontsize=30)
    ax.quiver(0, 0, 0, 0, 0, 1.2, color=AZUL, lw=3, arrow_length_ratio=0.25)
    ax.text(1.15, -0.2, 0.1, r"$C$", color="#B91C1C", fontsize=30)
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6); ax.set_zlim(-2.6, 2.8)
    ax.set_xlabel("x", fontsize=18); ax.set_ylabel("y", fontsize=18); ax.set_zlabel("z", fontsize=18)
    ax.view_init(elev=22, azim=azim)
    ax.set_box_aspect((1, 1, 1.4))
    if propia:
        fig.savefig(ruta, facecolor=FONDO)
        plt.close(fig)


# ---------------------------------------------------------------- video
def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def clip_imagenes(lista, salida_mp4):
    """lista = [(png, segundos)] -> mp4"""
    txt = salida_mp4 + ".txt"
    with open(txt, "w") as f:
        for png, d in lista:
            f.write(f"file '{png}'\nduration {d}\n")
        f.write(f"file '{lista[-1][0]}'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", txt,
         "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-preset", "medium",
         "-crf", "20", salida_mp4])


def clip_secuencia(patron, salida_mp4):
    run(["ffmpeg", "-y", "-framerate", str(FPS), "-i", patron,
         "-vf", "format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20", salida_mp4])


def construir(nombre, secciones, etiqueta, fig3d):
    d = os.path.join(TMP, nombre)
    os.makedirs(d, exist_ok=True)
    pie = f"{NOMBRE}  ·  {etiqueta}"
    clips = []
    for k, sec in enumerate(secciones):
        tipo = sec.get("tipo")
        mp4 = os.path.join(d, f"clip{k:02d}.mp4")
        if tipo == "portada":
            png = os.path.join(d, f"s{k:02d}.png")
            portada(sec, pie, png)
            clip_imagenes([(png, sec["dur"])], mp4)
        elif tipo in ("superficie3d", "cable3d"):
            n = int(sec["dur"] * FPS)
            for i in range(n):
                fig3d(-60 + 360 * i / n, os.path.join(d, f"r{k:02d}_{i:04d}.png"))
            clip_secuencia(os.path.join(d, f"r{k:02d}_%04d.png"), mp4)
        else:
            lista = []
            for j, dur in enumerate(sec["durs"], start=1):
                png = os.path.join(d, f"s{k:02d}_{j}.png")
                diapositiva(sec, j, pie, png)
                lista.append((png, dur))
            clip_imagenes(lista, mp4)
        clips.append(mp4)
        print("  listo:", sec["titulo"])
    seg = os.path.join(SALIDA, "segmentos")
    os.makedirs(seg, exist_ok=True)
    for k, c in enumerate(clips):
        shutil.copy(c, os.path.join(seg, f"{nombre}_{k:02d}.mp4"))


# ---------------------------------------------------------------- PDF
def hoja_pdf(ruta):
    A4 = (8.27, 11.69)
    with PdfPages(ruta) as pdf:
        for nombre_bloque, secciones, fig3d in (
                ("Opción 3:  F = ⟨z, x, y⟩,  S: z = 4 − x² − y², z ≥ 0, normal hacia arriba", OPCION3, fig_paraboloide),
                ("Ejercicio 2 (mecatrónica): sensor de corriente en el cable de un motor", MECATRONICA, fig_cable)):
            fig = plt.figure(figsize=A4)
            fig.patch.set_facecolor("white")
            y = 0.95
            fig.text(0.07, y, "Hoja de respuestas — Teorema de Stokes", fontsize=15, weight="bold", color=VERDE)
            y -= 0.03
            fig.text(0.07, y, "Integrantes: " + ",  ".join(INTEGRANTES), fontsize=10)
            y -= 0.035
            fig.text(0.07, y, nombre_bloque, fontsize=10.5, weight="bold", color=AZUL)
            y -= 0.02
            fig3d(-55, fig=fig, rect=(0.55, y - 0.20, 0.42, 0.21))
            for sec in secciones:
                if sec.get("tipo"):
                    continue
                if y < 0.12:
                    pdf.savefig(fig); plt.close(fig)
                    fig = plt.figure(figsize=A4); y = 0.95
                y -= 0.035
                fig.text(0.07, y, sec["titulo"], fontsize=12, weight="bold", color=VERDE)
                for mat, nota in sec["pasos"]:
                    y -= 0.034
                    fig.text(0.09, y, mat, fontsize=10.5)
                    y -= 0.017
                    fig.text(0.11, y, "· " + nota, fontsize=8, color=NOTA, style="italic")
            pdf.savefig(fig); plt.close(fig)


if __name__ == "__main__":
    os.makedirs(SALIDA, exist_ok=True)
    print("Opción 3 …")
    construir("op3", OPCION3, "Ejercicio 1 (Opción 3)", fig_paraboloide)
    print("Mecatrónica …")
    construir("mec", MECATRONICA, "Ejercicio 2 (mecatrónica)", fig_cable)
    hoja_pdf(os.path.join(SALIDA, "hoja_de_respuestas.pdf"))
    print("PDF listo")
    shutil.rmtree(TMP, ignore_errors=True)
