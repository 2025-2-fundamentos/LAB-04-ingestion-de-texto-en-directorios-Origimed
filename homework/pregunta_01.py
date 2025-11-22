# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratorio está almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.

    Descomprima este archivo y construya los archivos CSV:

    - files/output/train_dataset.csv
    - files/output/test_dataset.csv

    Ambos con las columnas:

    - phrase: contenido de cada archivo .txt
    - target: etiqueta según la carpeta (positive, negative, neutral)
    """
    import os
    import zipfile
    import pandas as pd

    zip_path = os.path.join("files", "input.zip")
    extract_root = "files"

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_root)

    output_dir = os.path.join("files", "output")
    os.makedirs(output_dir, exist_ok=True)

    base_input = os.path.join("files", "input")

    for split in ("train", "test"):
        split_dir = os.path.join(base_input, split)

        rows = []

        for label in ("neutral", "positive", "negative"):
            label_dir = os.path.join(split_dir, label)
            if not os.path.isdir(label_dir):
                continue

            for fname in sorted(os.listdir(label_dir)):
                if not fname.endswith(".txt"):
                    continue

                fpath = os.path.join(label_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    text = f.read().strip()

                rows.append(
                    {
                        "phrase": text,
                        "target": label,
                    }
                )

        df = pd.DataFrame(rows, columns=["phrase", "target"])
        out_path = os.path.join(output_dir, f"{split}_dataset.csv")
        df.to_csv(out_path, index=False)

if __name__ == "__main__":
    pregunta_01()