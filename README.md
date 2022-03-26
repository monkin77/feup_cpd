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

| Matrix Size | Time (s) | GFlops | DCM1        | DCM2        | DCH2        | DCM2(%) |
| ----------- | -------- | ------ | ----------- | ----------- | ----------- | ------- |
| 600x600     | 0.223    | 1.937  | 244560243   | 7915044     | 238833002   | 3.21    |
| 1000x1000   | 1.474    | 1.357  | 1231990925  | 76969658   | 1061103479  | 6.76   |
| 1400x1400   | 6.263    | 0.876  | 3446520842  | 352133818  | 2747871324  | 11.36   |
| 1800x1800   | 25.860   | 0.451  | 9084128288  | 780837346  | 5808340864  | 11.85   |
| 2200x2200   | 59.384   | 0.359  | 17645799085 | 1537694373 | 10507321345 | 12.77   |
| 2600x2600   | 99.954   | 0.352  | 30895382483 | 3226483656 | 16766181399 | 16.14   |
| 3000x3000   | 161.460  | 0.334  | 50316669133 | 8111919195 | 23242070966 | 25.87   |

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

| Matrix Size | Time (s) | GFlops | DCM1       | DCM2       | DCH2      | DCM2(%) |
| ----------- | -------- | ------ | ---------- | ---------- | --------- | ------- |
| 600x600     | 0.181    | 2.387  | 27194041   | 56806542   | 1474125   | 97.47   |
| 1000x1000   | 0.865    | 2.312  | 126332952  | 252601468  | 8270649   | 96.83   |
| 1400x1400   | 2.401    | 2.286  | 348135868  | 678452276  | 22287109  | 96.82   |
| 1800x1800   | 5.643    | 2.067  | 782482325  | 1457023313 | 56106893  | 96.29   |
| 2200x2200   | 9.090    | 2.343  | 2100630861 | 2636083754 | 197527007 | 93.03   |
| 2600x2600   | 17.486   | 2.010  | 4410117289 | 4356080593 | 471573240 | 90.23   |
| 3000x3000   | 24.264   | 2.226  | 6780271682 | 6703306124 | 709454360 | 90.43   |

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
| 4096x4096 | 0.150 | 2,880 | 9613739176 | 31391827210 |
| 6144x6144 | 0.761 | 2,628 | 32576153172 | 106375361016 |
| 8192x8192 | 2.156 | 2,545 | 74988504152 | 245339805204 |
| 10240x10240 | 4.609 | 2,530 | 152598619562 | 483201881442 |

---

**Block Size 256**
| Matrix Size | Time (s) | GFlops | DCM1 | DCM2 |
| ----------- | -------- | ------ | ---------- | ---------- |
| 4096x4096 | 0.150 | 2,880 | 9060360580 | 22477930670 |
| 6144x6144 | 0.761 | 2,628 | 30584181312 | 76159340711 |
| 8192x8192 | 2.156 | 2,545 | 72749434272 | 175123122444 |
| 10240x10240 | 4.609 | 2,530 | 141872370335 | 344149766392 |

---

**Block Size 512**
| Matrix Size | Time (s) | GFlops | DCM1 | DCM2 |
| ----------- | -------- | ------ | ---------- | ---------- |
| 4096x4096 | 0.150 | 2,880 | 8773977662 | 18644711268 |
| 6144x6144 | 0.761 | 2,628 | 29674235652 | 63012053606 |
| 8192x8192 | 2.156 | 2,545 | 70261413733 | 151291410877 |
| 10240x10240 | 4.609 | 2,530 | 137086086772 | 294480240937 |

---

### Observations

DCM2 values are derived instead of directly measured

To reach a conclusion:

- Analyse with PAPI the level 1 and level2 DCA (data cache accesses, for example)
- papi_avail -a -> show papi registers

### Setup

`sudo sh -c 'echo -1 >/proc/sys/kernel/perf_event_paranoid'`
