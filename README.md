#  PathFinder - Labirinto 2D com Algoritmo A*

##  Sobre o Projeto

Este projeto implementa o algoritmo **A\*** para encontrar o menor caminho entre dois pontos em um labirinto 2D. Ele simula um robô de resgate que deve ir do ponto inicial `S` até o ponto final `E`, evitando obstáculos e considerando os custos dos terrenos.

Além da lógica tradicional, essa versão aprimorada também inclui:
- Movimentos **diagonais com custo √2**.
- **Pesos variáveis** nas células livres (ex: terrenos difíceis).
- Uma **interface gráfica em tempo real com Pygame** mostrando a execução do algoritmo.

##  Tecnologias Utilizadas

- Python 3.8+
- Pygame
- heapq e math

##  Regras do Labirinto

| Símbolo | Significado                       |
|---------|-----------------------------------|
| `S`     | Início                            |
| `E`     | Fim                               |
| `0`     | Caminho livre (custo 1)           |
| `1`     | Obstáculo                         |
| `2+`    | Terreno difícil (custo ≥ 2)       |

##  Funcionamento do Algoritmo A*

O A\* combina:

- `g(n)`: custo do caminho até o nó atual
- `h(n)`: distância de Manhattan ao destino

##  Interface Gráfica

| Cor        | Significado                        |
|------------|------------------------------------|
| 🟩 Verde   | Ponto inicial (S)                  |
| 🟥 Vermelho| Ponto final (E)                    |
| ⬛ Preto    | Obstáculo                          |
| 🟨 Amarelo | Caminho final encontrado            |
| 🟦 Azul    | Células exploradas                 |
| ⚪ Branco  | Caminho livre                       |
| ⚫ Cinza   | Terreno difícil (peso > 1)         |

##  Como Executar

```bash
pip install pygame
python main.py
```

##  Exemplo de Entrada

```python
labirinto = [
    ['S', '0', '1', '0', '0'],
    ['0', '2', '1', '0', '1'],
    ['1', '3', '1', '0', '0'],
    ['1', '0', '0', 'E', '1']
]
```

##  Exemplo de Saída

```text
[(0, 0), (1, 0), (2, 1), (3, 1), (3, 2), (3, 3)]
```

##  Sem Solução?
```
Sem solução.
```

##  Autores

- [Renato Cazzoletti]

