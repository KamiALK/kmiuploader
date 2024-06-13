import os
from PyPDF2 import PdfMerger


def merge_pdfs_in_folder(folder_path, output_path):
    merger = PdfMerger()

    # Recorre todos los archivos en la carpeta
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".pdf"):
                file_path = os.path.join(root, filename)
                merger.append(file_path)

    # Guarda el PDF combinado en un archivo de salida
    with open(output_path, "wb") as output_file:
        merger.write(output_file)


# Ruta de la carpeta que contiene los PDFs
folder_path = "/home/kamilo/Descargas/catedra/"

# Ruta de salida para el PDF combinado
output_path = "./archivo_combinado.pdf"

# Llama a la función para unir los PDFs
merge_pdfs_in_folder(folder_path, output_path)

print("Los PDFs se han unido exitosamente.")
