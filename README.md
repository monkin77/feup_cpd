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

| Matrix Size | Time (s) | GFlops |
| ----------- | -------- | ------ |
| 600x600     | 0.878    | 0,492  |
| 1000x1000   | 4.167    | 0,480  |
| 1400x1400   | 16.183   | 0,339  |
| 1800x1800   | 36.078   | 0,323  |
| 2200x2200   | 70.971   | 0,300  | 
| 2600x2600   | 126.327  | 0,278  |
| 3000x3000   | 191.421  | 0,282  |

### 2 - Processing Time

#### C++

| Matrix Size | Time (s) | GFlops | DCM1       | DCM2       |
| ----------- | -------- | ------ | ---------- | ---------- |
| 600x600     | 0.150    | 2,880  | 27124251   | 57006518   |
| 1000x1000   | 0.761    | 2,628  | 125811706  | 258184630  |
| 1400x1400   | 2.156    | 2,545  | 346218640  | 697626778  |
| 1800x1800   | 4.609    | 2,530  | 746085489  | 1483259550 |
| 2200x2200   | 8.434    | 2,525  | 2080058295 | 2714588869 |
| 2600x2600   | 14.030   | 2,505  | 4413748362 | 4479046263 |
| 3000x3000   | 21.933   | 2,462  | 6780858121 | 6908756252 |

#### Java

| Matrix Size | Time (s) | GFlops |
| ----------- | -------- | ------ |
| 600x600     | 0.212    | 2,038  |
| 1000x1000   | 1.230    | 1,626  |
| 1400x1400   | 3.334    | 1,646  |
| 1800x1800   | 7.104    | 1,642  |
| 2200x2200   | 8.763    | 2,430  |
| 2600x2600   | 15.660   | 2,245  |
| 3000x3000   | 23.102   | 2,337  | 

### 3 - Processing Time (Block Matrix)

#### C++

**Block Size 128**
| Matrix Size | Time (s) | GFlops | DCM1 | DCM2 |
| ----------- | -------- | ------ | ---------- | ---------- |
| 4096x4096 | 0.150 | 2,880 | 70053193503 | 133853176811 |
| 6144x6144 | 0.761 | 2,628 | 236365178414 | 430766020194 |
| 8192x8192 | 2.156 | 2,545 | 346218640 | 697626778 |
| 10240x10240 | 4.609 | 2,530 | 746085489 | 1483259550 |

---

---

### Setup

`sudo sh -c 'echo -1 >/proc/sys/kernel/perf_event_paranoid'`
