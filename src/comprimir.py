#!/bin/python3

import ZipFile
import json

def getCompresion(objBase64):
    with zipfile.ZipFile("MiArchivo.zip", "w") as f:
        f.write(objBase64)
    return json.dumps({"status": "ok"})
