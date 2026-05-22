import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
import keyboard

modelo = Model("vosk-model-small-es-0.42")

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

print("Micrófonos disponibles:\n")

print(sd.query_devices())

indice_mic = int(input("\nElige el micrófono: "))

samplerate = int(sd.query_devices(indice_mic, 'input')['default_samplerate'])

rec = KaldiRecognizer(modelo, samplerate)

print("\nPresiona Q para salir")
print("Habla ahora...\n")

with sd.RawInputStream(
    samplerate=samplerate,
    blocksize=8000,
    device=indice_mic,
    dtype='int16',
    channels=1,
    callback=callback
):

    while True:

        if keyboard.is_pressed("q"):
            print("\nGrabación terminada")
            break

        data = q.get()

        if rec.AcceptWaveform(data):

            resultado = json.loads(rec.Result())

            texto = resultado.get("text", "")

            if texto.strip():

                print("Has dicho:", texto)

                with open("transcripcion.txt", "a", encoding="utf-8") as file:
                    file.write(texto + "\n")

import os

os.startfile("transcripcion.txt")