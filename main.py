import pygame
import heapq
import math
import time


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 150, 255)
YELLOW = (255, 255, 0)

MOVES = [
    (-1, 0, 1), (1, 0, 1), (0, -1, 1), (0, 1, 1),  
    (-1, -1, math.sqrt(2)), (-1, 1, math.sqrt(2)), (1, -1, math.sqrt(2)), (1, 1, math.sqrt(2))  # diagonais
]

TAMANHO_CELULA = 50

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def encontrar_posicao(matriz, valor):
    for i, linha in enumerate(matriz):
        for j, val in enumerate(linha):
            if val == valor:
                return (i, j)
    return None

def peso_da_celula(celula):
    if celula == 'S' or celula == 'E':
        return 1
    try:
        return int(celula)
    except:
        return 1

def desenhar_labirinto(tela, matriz, caminho=set(), explorados=set()):
    for i, linha in enumerate(matriz):
        for j, val in enumerate(linha):
            x = j * TAMANHO_CELULA
            y = i * TAMANHO_CELULA

            cor = WHITE
            if val == '1':
                cor = BLACK
            elif val == 'S':
                cor = GREEN
            elif val == 'E':
                cor = RED
            elif (i, j) in caminho:
                cor = YELLOW
            elif (i, j) in explorados:
                cor = BLUE
            elif val.isdigit() and int(val) > 1:
                cor = GRAY

            pygame.draw.rect(tela, cor, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
            pygame.draw.rect(tela, BLACK, (x, y, TAMANHO_CELULA, TAMANHO_CELULA), 1)

def a_star_com_visualizacao(matriz, tela):
    inicio = encontrar_posicao(matriz, 'S')
    fim = encontrar_posicao(matriz, 'E')
    if not inicio or not fim:
        print("Labirinto precisa conter 'S' e 'E'.")
        return None

    n_linhas, n_colunas = len(matriz), len(matriz[0])
    visitados = set()
    heap = []
    heapq.heappush(heap, (heuristica(inicio, fim), 0, inicio, [inicio]))
    explorados = set()

    while heap:
        pygame.event.pump()  
        f, g, atual, caminho = heapq.heappop(heap)

        if atual == fim:
            return caminho

        if atual in visitados:
            continue
        visitados.add(atual)
        explorados.add(atual)

        for dx, dy, custo_base in MOVES:
            ni, nj = atual[0] + dx, atual[1] + dy
            if 0 <= ni < n_linhas and 0 <= nj < n_colunas:
                destino = matriz[ni][nj]
                if destino != '1':
                    custo = custo_base * peso_da_celula(destino)
                    novo_g = g + custo
                    novo_f = novo_g + heuristica((ni, nj), fim)
                    heapq.heappush(heap, (novo_f, novo_g, (ni, nj), caminho + [(ni, nj)]))

        desenhar_labirinto(tela, matriz, set(caminho), explorados)
        pygame.display.flip()
        time.sleep(0.05)

    return None

def main():
    labirinto = [
        ['S', '0', '1', '0', '0'],
        ['0', '2', '1', '0', '1'],
        ['1', '3', '1', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]

    n_linhas = len(labirinto)
    n_colunas = len(labirinto[0])

    pygame.init()
    tela = pygame.display.set_mode((n_colunas * TAMANHO_CELULA, n_linhas * TAMANHO_CELULA))
    pygame.display.set_caption("A* - Labirinto")

    caminho = a_star_com_visualizacao(labirinto, tela)
    if caminho:
        print("Menor caminho (em coordenadas):")
        print(caminho)
    else:
        print("Sem solução.")

    
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
    pygame.quit()

if __name__ == "__main__":
    main()
