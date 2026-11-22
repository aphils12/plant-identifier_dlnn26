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
