#  PathFinder - Labirinto 2D com Algoritmo A*

##  Descrição Geral

Este projeto tem como objetivo implementar uma simulação de um **robô de resgate autônomo** que percorre um **labirinto 2D** do ponto de partida `S` até o destino `E`, **evitando obstáculos**, **considerando pesos variados nas células** e utilizando o **algoritmo A\*** como estratégia de busca.

Além disso, o sistema exibe uma **visualização gráfica em tempo real** utilizando a biblioteca **Pygame**, evidenciando o funcionamento do algoritmo durante a exploração do caminho.

##  Conceitos Envolvidos

- Busca heurística com A\* (A-star)
- Heurística de Manhattan para estimar custo
- Movimentos em 8 direções (vertical, horizontal e diagonal)
- Custos diferenciados por tipo de terreno
- Interface gráfica para visualização do processo de busca
- Manipulação de eventos com Pygame

##  Tecnologias Utilizadas

- **Python 3.8+**
- **Pygame**
- **heapq** (fila de prioridade)
- **math** (para cálculo de custo diagonal)

##  Estrutura do Labirinto

A matriz do labirinto é composta por diferentes símbolos, cada um com uma função e custo distintos:

| Símbolo | Significado                       | Custo      |
|---------|-----------------------------------|------------|
| `S`     | Início                            | 1          |
| `E`     | Fim                               | 1          |
| `0`     | Caminho livre                     | 1          |
| `1`     | Obstáculo                         | ∞ (intransitável) |
| `2+`    | Terreno difícil                   | ≥ 2        |

##  Funcionamento do Algoritmo A\*

O algoritmo A\* combina duas funções para calcular o custo total de um caminho:

- `g(n)`: Custo real do caminho do início até o nó atual.
- `h(n)`: Estimativa (heurística) do custo até o destino. Neste caso, usamos a **Distância de Manhattan**.
- `f(n) = g(n) + h(n)`: Função de avaliação total.

Além disso:
- Os **movimentos diagonais** são permitidos e possuem custo √2 multiplicado pelo peso da célula de destino.
- Células com custo maior (ex: `2`, `3`, etc) penalizam o caminho, influenciando a decisão do algoritmo.

##  Interface Gráfica

A execução do algoritmo é visualizada em tempo real via **Pygame**, com as seguintes representações:

| Cor        | Significado                        |
|------------|------------------------------------|
| 🟩 Verde   | Ponto inicial (`S`)                |
| 🟥 Vermelho| Ponto final (`E`)                  |
| ⬛ Preto    | Obstáculo (`1`)                    |
| ⚪ Branco  | Caminho livre (`0`)                |
| ⚫ Cinza   | Terreno difícil (`2+`)             |
| 🟦 Azul    | Células exploradas pelo algoritmo  |
| 🟨 Amarelo | Caminho final encontrado            |

## Exemplo de Código

```python
labirinto = [
    ['S', '0', '1', '0', '0'],
    ['0', '2', '1', '0', '1'],
    ['1', '3', '1', '0', '0'],
    ['1', '0', '0', 'E', '1']
]
```

### Explicação:

- **S**: ponto de partida em (0,0).
- O caminho tenta evitar as células `1` (obstáculos) e minimizar o custo total mesmo passando por células `2` ou `3`.
- **E**: ponto final em (3,3).

### Resultado esperado (menor caminho):

```text
[(0, 0), (1, 0), (2, 1), (3, 1), (3, 2), (3, 3)]
```

Neste caso, o robô se desloca por células de menor custo, mesmo atravessando terrenos difíceis (`2`, `3`) quando necessário para evitar obstáculos.

##  Possível Saída Sem Caminho

Quando não há caminho viável do início ao fim, o programa exibirá:

```text
Sem solução.
```

##  Como Executar o Projeto

1. **Instale o Python 3** (se ainda não tiver):
   https://www.python.org/downloads/

2. **Clone o repositório:**

```bash
git clone https://github.com/renatoctti/Trabalho-em-grupo-1.git
```

3. **Instale o pygame:**

```bash
pip install pygame
```

4. **Execute o programa principal:**

```bash
python main.py
```

##  Autores

- Renato Cazzoletti
