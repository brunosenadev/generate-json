from os import listdir, path
from json import dump
from time import sleep

def generate_json():
    base_path = 'diretorio\\de\\origem'
    output_file = 'diretorio\\de\\destino'
    list = []
    
    for folder in listdir(base_path):
        folder_path = path.join(base_path, folder)

        if path.isdir(folder_path):
            images = [
                f'/EmpresasImagensWebp/{folder}/{file}'
                for file in listdir(folder_path)
                if file.endswith(('.webp'))
            ]
            list.append(
                {
                    "nome": folder,
                    "imagens": images
                }
            )
            
    with open(output_file, 'w', encoding='utf-8') as json_file:
        dump(list, json_file, ensure_ascii=False, indent=4)
    
    print(f"JSON gerado com sucesso em {output_file}!")

    sleep(3)

generate_json()