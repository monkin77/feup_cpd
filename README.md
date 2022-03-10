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
| 600x600     | 0.251    | 1,72   | 244729954   | 40350020    |
| 1000x1000   | 1,906    | 1,05   | 1233542352  | 314169572   |
| 1400x1400   | 5.535    | 0,99   | 3521438751  | 1409893723  |
| 1800x1800   | 24.720   | 0,472  | 9081385439  | 7716099536  |
| 2200x2200   | 52.085   | 0,409  | 17656947842 | 22620642232 |
| 2600x2600   | 92.081   | 0,382  | 30882100366 | 50572420466 |
| 3000x3000   | 156.076  | 0,346  | 50309367077 | 95269463253 |

#### Java

Java table

### Setup

`sudo sh -c 'echo -1 >/proc/sys/kernel/perf_event_paranoid'`
