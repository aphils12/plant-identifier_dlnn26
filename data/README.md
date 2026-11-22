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

## Sugestão

1. Descarregar primeiro só os dois ficheiros de metadados e escolher o subconjunto de espécies.
2. Guardar as imagens no Google Drive, não no computador (são vários GB).
3. Registar aqui a data do download e a versão usada, para o relatório.
