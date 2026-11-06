# -*- coding: utf-8 -*-
"""Monta el video final en pantalla dividida.

Izquierda (640x1080): la grabación real de quien habla (celular en vertical).
Derecha (1280x720):   la animación del ejercicio, ajustada a la duración de la voz.

Pon las grabaciones en ./grabaciones/ con estos nombres (mp4 o mov):
    01_carlos.mp4, 02_juanpablo.mp4, 03_carlos.mp4, ...  (ver SEGMENTOS)
Alternativa sin video: una foto de cada uno (carlos.jpg, juanpablo.jpg) y la voz
de cada clip como audio (01_carlos.m4a, 02_juanpablo.m4a, ...).
Si falta una grabación, se pone un recuadro "GRABAR AQUÍ" (vista previa).

Uso:  python3 generar/montaje.py      ->  salida/video_final.mp4
"""
import glob
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEG = os.path.join(RAIZ, "salida", "segmentos")
GRAB = os.path.join(RAIZ, "grabaciones")
TMP = os.path.join(RAIZ, ".tmp_frames", "montaje")
FUENTE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FUENTE_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

NOMBRES = {"carlos": "Carlos Andrés Infante Rocha", "juanpablo": "Juan Pablo González Guzmán"}

# (numero, quien, clips de animación, parte)
SEGMENTOS = [
    (1, "carlos",    ["op3_00", "op3_01"],           "Presentación y problema"),
    (2, "juanpablo", ["op3_02", "op3_03"],           "Superficie, normal y borde"),
    (3, "carlos",    ["op3_04"],                     "Rotacional"),
    (4, "juanpablo", ["op3_05"],                     "Camino 1: superficie"),
    (5, "carlos",    ["op3_06"],                     "Camino 2: línea"),
    (6, "juanpablo", ["op3_07"],                     "Conclusión"),
    (7, "carlos",    ["mec_00", "mec_01", "mec_02"], "Mecatrónica: problema y superficie"),
    (8, "juanpablo", ["mec_03", "mec_04"],           "Mecatrónica: línea y aplicación"),
]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-2000:])
    return r.stdout


def duracion(f):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "csv=p=0", f]).strip())


def tiene_audio(f):
    out = run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
               "stream=index", "-of", "json", f])
    return bool(json.loads(out).get("streams"))


def esc(t):
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’")


def grabacion(n, quien):
    for ext in ("mp4", "mov", "MP4", "MOV", "m4v", "webm"):
        hits = glob.glob(os.path.join(GRAB, f"{n:02d}_{quien}.{ext}"))
        if hits:
            return hits[0]
    return None


def foto_y_audio(n, quien):
    """Alternativa: una foto (jpg/png) + la voz real grabada (m4a/mp3/wav/ogg/opus)."""
    foto = audio = None
    for ext in ("jpg", "jpeg", "png", "JPG", "JPEG", "PNG", "heic"):
        hits = glob.glob(os.path.join(GRAB, f"{quien}.{ext}")) + \
               glob.glob(os.path.join(GRAB, f"{n:02d}_{quien}.{ext}"))
        if hits:
            foto = hits[0]
    for ext in ("m4a", "mp3", "wav", "ogg", "opus", "aac", "M4A", "MP3", "WAV"):
        hits = glob.glob(os.path.join(GRAB, f"{n:02d}_{quien}.{ext}"))
        if hits:
            audio = hits[0]
    return (foto, audio) if foto and audio else (None, None)


def segmento(n, quien, clips, parte):
    lista = os.path.join(TMP, f"anim{n}.txt")
    with open(lista, "w") as f:
        for c in clips:
            f.write(f"file '{os.path.join(SEG, c + '.mp4')}'\n")
    anim = os.path.join(TMP, f"anim{n}.mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", anim])
    A = duracion(anim)

    cam = grabacion(n, quien)
    foto, audio = (None, None) if cam else foto_y_audio(n, quien)
    if foto:
        # foto fija con un acercamiento lento + la voz real
        cam_v = os.path.join(TMP, f"foto{n}.mp4")
        D0 = duracion(audio)
        frames = int(D0 * 24) + 24
        run(["ffmpeg", "-y", "-loop", "1", "-i", foto, "-i", audio, "-filter_complex",
             f"[0:v]scale=1280:2160:force_original_aspect_ratio=increase,crop=1280:2160,"
             f"zoompan=z='min(1+0.0004*on,1.15)':d={frames}:x='iw/2-(iw/zoom/2)':"
             f"y='ih/2-(ih/zoom/2)':s=640x1080:fps=24[v]",
             "-map", "[v]", "-map", "1:a", "-t", f"{D0}", "-c:v", "libx264", "-preset", "fast",
             "-c:a", "aac", "-pix_fmt", "yuv420p", cam_v])
        cam = cam_v
    D = duracion(cam) if cam else A
    nombre = NOMBRES[quien]
    titulo = esc(f"Teorema de Stokes  ·  {parte}")

    if cam:
        izq = (f"[1:v]scale=640:1080:force_original_aspect_ratio=increase,"
               f"crop=640:1080,fps=24,setsar=1[c]")
        entradas = ["-i", anim, "-i", cam]
    else:
        izq = (f"color=c=0x374151:s=640x1080:d={D}:r=24,"
               f"drawtext=fontfile={FUENTE_B}:text='GRABAR AQUÍ':fontsize=48:fontcolor=white:"
               f"x=(w-tw)/2:y=440,"
               f"drawtext=fontfile={FUENTE}:text='{esc(nombre.split()[0] + ' ' + nombre.split()[1])}':"
               f"fontsize=34:fontcolor=0xFFE9A8:x=(w-tw)/2:y=520,"
               f"drawtext=fontfile={FUENTE}:text='clip {n:02d}_{quien}.mp4':fontsize=28:"
               f"fontcolor=0xD1D5DB:x=(w-tw)/2:y=580[c]")
        entradas = ["-i", anim]

    filtro = ";".join([
        f"[0:v]setpts=PTS*{D / A:.6f},fps=24,scale=1280:720,setsar=1[a]",
        izq,
        f"color=c=0xFBFAF6:s=1920x1080:d={D}:r=24[bg]",
        "[bg][c]overlay=0:0[t1]",
        "[t1][a]overlay=640:180:shortest=0[t2]",
        f"[t2]drawtext=fontfile={FUENTE_B}:text='{titulo}':fontsize=40:fontcolor=0x2F6B4F:"
        f"x=640+(1280-tw)/2:y=80,"
        f"drawbox=x=0:y=990:w=640:h=90:color=black@0.55:t=fill,"
        f"drawtext=fontfile={FUENTE}:text='{esc(nombre)}':fontsize=28:fontcolor=white:"
        f"x=(640-tw)/2:y=1022,"
        f"trim=duration={D},format=yuv420p[v]",
    ])
    cmd = ["ffmpeg", "-y", *entradas]
    if cam and tiene_audio(cam):
        amap = ["-map", "1:a:0", "-af", "loudnorm=I=-16:TP=-1.5,aresample=48000"]
    else:
        cmd += ["-f", "lavfi", "-t", f"{D}", "-i", "anullsrc=r=48000:cl=stereo"]
        amap = ["-map", f"{len(entradas) // 2}:a"]
    out = os.path.join(TMP, f"seg{n:02d}.mp4")
    cmd += ["-filter_complex", filtro, "-map", "[v]", *amap, "-t", f"{D}",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", "24",
            "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2", out]
    run(cmd)
    estado = "grabación" if cam else "FALTA grabación"
    print(f"  {n:02d} {quien:<10} {D:6.1f}s  ({estado})  {parte}")
    return out, D


def main():
    os.makedirs(TMP, exist_ok=True)
    os.makedirs(GRAB, exist_ok=True)
    partes, total = [], 0.0
    for s in SEGMENTOS:
        out, d = segmento(*s)
        partes.append(out)
        total += d
    lista = os.path.join(TMP, "final.txt")
    with open(lista, "w") as f:
        for p in partes:
            f.write(f"file '{p}'\n")
    final = os.path.join(RAIZ, "salida", "video_final.mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy",
         "-movflags", "+faststart", final])
    m, s = divmod(int(round(total)), 60)
    print(f"VIDEO FINAL: {final}  ({m}:{s:02d})")
    if total > 300:
        print("  ATENCIÓN: pasa de 5 minutos; hay que acortar alguna grabación.")


if __name__ == "__main__":
    main()
