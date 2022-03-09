Ao alterar a ordem no loop de j e k. Fazemos um acesso em linha, utilizando os dados cachados. Ao contrário do outro caso que faz acessos em coluna.

Objetivos:

- Avaliar performance ao alterar a ordem do loop
- Calcular tempo de execução: t=2\*n^3 / Capacidade (Gflops)
- 2\*n^3 -> Complexidade do problema
- PAPI -> Permite obter contadores do sistema (e.g detetar falhas de cache)

Matrix Structure
A: [
[1,1,1],
[1,1,1],
[1,1,1]
]

B: [
[1,1,1],
[2,2,2],
[3,3,3]
]

C: [
[6,6,6],
[6,6,6],
[6,6,6]
]

DCM -> Data Cache Misses

### 1 - Processing Time

#### C++

| Matrix Size | Time (s) | GFlops | DCM1        | DCM2        |
| ----------- | -------- | ------ | ----------- | ----------- |
| 600x600     | 0.252    | 1,71   | 244630657   | 38589488    |
| 1000x1000   | 1.412    |        |             |             |
| 1400x1400   |          |        |             |             |
| 1800x1800   |          |        |             |             |
| 2200x2200   |          |        |             |             |
| 2600x2600   |          |        |             |             |
| 3000x3000   | 142.190  | 0,38   | 50314301321 | 93219371070 |

#### Java

Java table
