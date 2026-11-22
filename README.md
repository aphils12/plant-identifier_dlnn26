# plant-identifier_dlnn26

Projeto da 2.ª época de **Deep Learning Neural Networks** (EDSA 2026/27, NOVA IMS), **Grupo 4**.

## Objetivo

Identificar a **espécie de uma planta a partir de uma fotografia** tirada em condições reais.

- **Input:** uma fotografia de uma planta (flor, folha, fruto, casca ou planta inteira).
- **Output:** a espécie, entre as espécies do subconjunto escolhido.

## Decisões (22/11/2026)

Revistas com os metadados do dataset. Exploração completa no [Explorador Pl@ntNet-300K](https://claude.ai/artifact/9nGUrwgrk4SbpkEgSeS6nr).

| Tema | Decisão | Porquê, segundo os dados |
|---|---|---|
| Espécies | **20 espécies em 10 pares do mesmo género** (tabela abaixo) | Pares difíceis e fáceis: mostra se a rede erra sobretudo entre espécies parecidas |
| Limpeza | Sem classes `spp.` nem nomes repetidos; sem os géneros que têm uma classe `spp.` | *Lavandula spp.* e *Pelargonium spp.* sobrepõem-se às espécies desses géneros |
| Treino | **Até 1 000 fotos por espécie** | Equilibra o treino (~20 000 fotos); só *Cucurbita maxima* fica abaixo (~890) |
| Métrica | **Macro-F1**, com accuracy e matriz de confusão | O teste não é equilibrado: de 111 a 766 fotos por espécie |
| Órgãos | Treinar com flor, folha, fruto, planta inteira e casca (sem `other`, `branch`, `scan`, `none`); analisar só **flor vs. folha** | No teste: 4 643 flor, 2 350 folha, 144 fruto, 77 planta inteira, 36 casca. O órgão está ligado à espécie (*T. zebrina* 96% folha) |
| Avaliação | **Teste completo e teste só com fotógrafos novos** | 23% das fotos de teste são de alguém com fotos da mesma espécie no treino (até 36% em *Cirsium arvense*) |
| Split | Split oficial, sem alterações; teste usado uma só vez | Comparável com os resultados publicados |
| Download | Só as pastas das 20 espécies (~10 GB), extraídas do zip remoto | O Zenodo aceita downloads parciais (testado a 22/11) |
| Extensão | Espécies desconhecidas: opcional, no fim | Só se o modelo base estiver pronto até ~11/12 |

### As 20 espécies (`species_id` entre parênteses)

| Género | Espécie A | Espécie B | Família |
|---|---|---|---|
| Cirsium | *Cirsium vulgare* (4) | *Cirsium arvense* (3) | Asteraceae |
| Trifolium | *Trifolium pratense* (112) | *Trifolium repens* (225) | Fabaceae |
| Lamium | *Lamium purpureum* (84) | *Lamium galeobdolon* (171) | Lamiaceae |
| Papaver | *Papaver rhoeas* (200) | *Papaver somniferum* (202) | Papaveraceae |
| Tradescantia | *Tradescantia pallida* (190) | *Tradescantia zebrina* (15) | Commelinaceae |
| Hypericum | *Hypericum perforatum* (11) | *Hypericum calycinum* (406) | Hypericaceae |
| Sedum | *Sedum album* (47) | *Sedum acre* (46) | Crassulaceae |
| Petrosedum | *Petrosedum sediforme* (60) | *Petrosedum rupestre* (186) | Crassulaceae |
| Calendula | *Calendula officinalis* (35) | *Calendula arvensis* (243) | Asteraceae |
| Cucurbita | *Cucurbita pepo* (310) | *Cucurbita maxima* (366) | Cucurbitaceae |

```python
SPECIES = [4, 3, 112, 225, 84, 171, 200, 202, 190, 15, 11, 406, 47, 46, 60, 186, 35, 243, 310, 366]
TRAIN_CAP = 1000
ORGANS = ["flower", "leaf", "fruit", "habit", "bark"]
```

## Dataset

**Pl@ntNet-300K** (Garcin et al., NeurIPS 2021 Datasets and Benchmarks): 306 087 fotografias de 1 000 espécies, tiradas pelos utilizadores da app Pl@ntNet, com split oficial de treino, validação e teste.

- Repositório: <https://github.com/plantnet/PlantNet-300K>
- Download (v2): <https://zenodo.org/records/10419064>
- Artigo: <https://openreview.net/forum?id=eLYinD0TtIt>

Os dados **não** ficam no repositório (ver [`data/README.md`](data/README.md)). Cada imagem tem a sua licença e autor nos metadados; citar o dataset no relatório.

## Estrutura

```
plant-identifier_dlnn26/
├── data/          # dados descarregados (fora do git)
├── notebooks/     # notebooks de exploração e de treino (Colab)
├── src/           # código partilhado: carregar dados, modelos, callbacks
├── report/        # relatório (máx. 5 páginas, Arial 11) e figuras
# 🌿 Plant Identifier — Deep Learning Neural Networks (2026)

Projeto da unidade curricular **Deep Learning** (NOVA IMS · Pós-Graduação em Enterprise Data Science & Analytics, 2.ª época).

O objetivo é desenvolver um modelo de **classificação de imagens** que, a partir de uma fotografia de uma planta, identifique a respetiva espécie. O guião do projeto está disponível no Moodle da cadeira.

---

## 1. Definição da tarefa

| | |
|---|---|
| **Entrada** | Fotografia RGB de uma planta (folha, flor ou planta inteira) |
| **Saída** | Espécie prevista (top-1) e as *k* espécies mais prováveis com a respetiva probabilidade (top-k) |
| **Tipo de problema** | Classificação multiclasse de imagens |
| **Problema real** | Ajudar não especialistas (agricultores, estudantes, curiosos) a identificar plantas a partir de uma foto tirada no campo |

**Âmbito:** _a definir_. Por exemplo, número de espécies, tipo de planta (ornamentais, infestantes, culturas agrícolas, flora portuguesa) e partes da planta consideradas. O âmbito não deve ser nem demasiado estreito nem demasiado largo.

## 2. Dataset

- **Fonte:**(https://zenodo.org/records/10419064)
- **N.º de classes / imagens:** _a definir_
- **Divisão:** treino / validação / teste, estratificada por classe

> ⚠️ Se o dataset vier já pré-processado (por exemplo, do Kaggle), o guião exige **fazer mais**, por exemplo comparar os nossos resultados com soluções publicadas para o mesmo dataset.

## 3. Métricas de avaliação

- **Desempenho:** accuracy (top-1 e top-5), F1-score macro (por causa do desequilíbrio entre classes), matriz de confusão
- **Eficiência:** n.º de parâmetros, tamanho do modelo em disco (MB), tempo de inferência por imagem, tempo de treino

## 4. Abordagem

Plano de experiências, da mais simples para a mais complexa:

1. **Baseline:** CNN simples treinada de raiz
2. **Data augmentation e regularização:** rotações, flips, alterações de cor, dropout, weight decay, early stopping
3. **Transfer learning:** backbones pré-treinados no ImageNet (por exemplo, ResNet, EfficientNet, MobileNet), primeiro com *feature extraction* e depois com *fine-tuning*
4. **Trade-off entre precisão e eficiência:** comparar modelos pesados com modelos leves, pensados para telemóvel

**Desafios esperados:** grande semelhança entre algumas espécies, grande variação dentro da mesma espécie (estação, idade, iluminação, fundo) e classes desequilibradas.

## 5. Análise de erros

- Curvas de treino e validação (loss e accuracy) para detetar overfitting
- Efeito do tamanho do dataset e do data augmentation na generalização
- Classes mais confundidas e exemplos mal classificados
- (Opcional) Grad-CAM para ver em que zonas da imagem o modelo se baseia

## 6. Estrutura do repositório

```
plant-identifier_dlnn26/
├── data/              # dados (não versionados; ver data/README.md)
│   ├── raw/           #   originais descarregados
│   └── processed/     #   imagens preparadas e divisões treino/val/teste
├── notebooks/         # exploração e experiências
├── src/               # código reutilizável
│   ├── config.py      #   caminhos e hiperparâmetros
│   ├── data.py        #   carregamento, divisão e data augmentation
│   ├── models.py      #   CNN baseline e transfer learning
│   ├── train.py       #   ciclo de treino
│   └── evaluate.py    #   métricas de desempenho e eficiência
├── models/            # pesos treinados (não versionados)
├── results/
│   ├── figures/       # gráficos usados no relatório
│   └── tables/        # tabelas usadas no relatório
├── report/            # relatório final (máx. 5 páginas)
├── .gitignore
├── requirements.txt
└── README.md
```

## Como correr

1. Abrir o notebook no Google Colab a partir do GitHub (`File > Open notebook > GitHub`).
2. Descarregar os dados para o Google Drive, seguindo [`data/README.md`](data/README.md).
3. Instalar as dependências: `pip install -r requirements.txt` (no Colab, a maioria já vem instalada).

## Entrega

Até **18 de dezembro**, no Moodle (Turnitin): código, link do dataset e relatório, num único ficheiro `GROUP 4.zip`.

## Grupo 4

- Ana Filipa Filipe
- Ana Rita Carapinha
- Inês Rodrigues
- Madalena Lourenço
- Nuno Pinto
## 7. Como correr

```bash
git clone <url-do-repositorio>
cd plant-identifier_dlnn26
python -m venv .venv
.venv\Scripts\activate        # Windows  (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
```

_Os comandos de treino e avaliação serão adicionados quando o código estiver pronto._

## 8. Entrega

- **Prazo:** 18 de dezembro de 2026, no Moodle (Turnitin)
- **Ficheiro:** um único `.zip`/`.rar` com o número do grupo (ex.: `GROUP 1.rar`)
- **Conteúdo:** código-fonte, link para o dataset e relatório (máx. 5 páginas, Arial 11, sem anexos)
- Preencher também o Excel do docente com os dados do grupo

## 9. Equipa

| Nome | N.º de aluno |
|---|---|
| | |
| | |
| | |
| | |
| | |
