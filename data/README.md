# Dados

Esta pasta fica fora do git: só este ficheiro é versionado.

## Pl@ntNet-300K

- Download (v2): <https://zenodo.org/records/10419064>
- Estrutura esperada, segundo o repositório oficial:

```
plantnet300kv2/
├── images/
│   ├── train/0000/ ... 0999/
│   ├── val/0000/   ... 0999/
│   └── test/0000/  ... 0999/
├── plantnet300K_metadata.csv   # imagem → espécie, split, autor, licença, órgão
└── species_metadata.csv        # espécie → nome científico, género, família, estado IUCN
```

## Como descarregar só as 20 espécies

O `images.zip` tem 41,8 GB, mas o Zenodo aceita downloads parciais (testado a 22/11/2026). Por isso dá para ler o índice do zip remoto e extrair só as pastas `images/<split>/<species_id>/` das 20 espécies (~10 GB), por exemplo com a biblioteca `remotezip`. A extração ainda está por testar no Colab.

- Metadados: `https://zenodo.org/api/records/10419064/files/plantnet300K_metadata.csv/content` e `.../species_metadata.csv/content`
- Imagens: `https://zenodo.org/api/records/10419064/files/images.zip/content`

## Regras

1. Guardar as imagens no Google Drive, não no computador.
2. Filtrar pelos `species_id` e órgãos definidos no README principal; aplicar o teto de treino com uma seed fixa.
3. Registar aqui a data do download e a versão usada, para o relatório.
Os dados não são versionados no git. Descarregar o dataset de:
https://zenodo.org/records/10419064

- `raw/`: ficheiros originais, tal como foram descarregados
- `processed/`: imagens redimensionadas e divisões treino/validação/teste
