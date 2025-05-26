import random

def movimentos_validos(x, y, maze, n, m):
    moves = []
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#':
            moves.append((nx, ny))
    return moves

def simula_uma_execucao(maze, tunel_map, start, n, m, max_passos=20000):
    x, y = start
    for _ in range(max_passos):
        celula = maze[x][y]
        if celula == '*':
            return False  # morreu 
            
        elif celula == '%':
            return True   # escapou 

        if (x, y) in tunel_map:
            x, y = tunel_map[(x, y)]
            continue

        moves = movimentos_validos(x, y, maze, n, m)
        if not moves:
            return False
        x, y = random.choice(moves)
    return False

def resolver_labirinto(n, m, k, maze, tunnels, sim=1000):
    start = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'A':
                start = (i, j)

    
    tunel_map = {}
    for i1, j1, i2, j2 in tunnels:
        if maze[i1][j1] != 'O' or maze[i2][j2] != 'O':
            continue
        tunel_map[(i1, j1)] = (i2, j2)
        tunel_map[(i2, j2)] = (i1, j1)

    sucesso = 0
    for _ in range(sim):
        if simula_uma_execucao(maze, tunel_map, start, n, m):
            sucesso += 1
    return sucesso / sim

def gerar_labirinto(n, m):
    elementos = ['O'] * 5 + ['#', '*', '%']
    labirinto = [''.join(random.choice(elementos) for _ in range(m)) for _ in range(n)]
    i, j = random.randint(0, n-1), random.randint(0, m-1)
    linha = list(labirinto[i])
    linha[j] = 'A'
    labirinto[i] = ''.join(linha)
    return labirinto
def gerar_tuneis(k, n, m):
    tuneis = set()
    while len(tuneis) < k:
        i1, j1 = random.randint(0, n-1), random.randint(0, m-1)
        i2, j2 = random.randint(0, n-1), random.randint(0, m-1)
        if (i1 != i2 or j1 != j2):
            tuneis.add((i1, j1, i2, j2))
    return list(tuneis)
def main():
    n, m, k = 5, 6, 2
    maze = gerar_labirinto(n, m)
    tunnels = gerar_tuneis(k, n, m)
    print("Maze:")
    for linha in maze:
        print(linha)
    print("Tunnels:", tunnels)
    resultado = resolver_labirinto(n, m, k, maze, tunnels)
    print("Probabilidade de fuga:", resultado)

if __name__ == "__main__":
    main()
