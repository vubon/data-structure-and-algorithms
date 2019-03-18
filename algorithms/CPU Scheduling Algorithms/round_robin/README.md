## Round Robin Problem 
|   Process |   Burst Time  |   Quantum Time | Arrival Time |
|   :---:   |     :---:     |      :---:     |     :---:    |
| P1        |     `7`       |       `2`      |      `0`     |
| P2        |     `5`       |       `2`      |      `5`     |
| P3        |     `2`       |       `2`      |      `10`    |
| P4        |     `3`       |       `2`      |      `7`     |
| P5        |     `8`       |       `2`      |      `3`     |


## Solution:
Quantum Time: 3

| Process   | Arrival Time| Burst Time | RT(Remaining time) | CT(Completion time) | TAT(Turn Around Time)[CT- AT] |  WT(Waiting time)[TAT - BT]  | 
|    :---:  |     :---:   |     :---:  |      :---:         |       :---:        |            :---:              |      :---:                   |
|    P1     |     `0`     |     `7`    |      [4, 1, 0]     |       `23`         |           23 - 0  = `23`      |      23 - 7 = `16`           |
|    P2     |     `5`     |     `5`    |      [2, 0]        |       `22`         |           22 - 5  = `17`      |      17 - 5 = `12`           |
|    P3     |     `10`    |     `2`    |      [0]           |       `14`         |           14 - 10 = `4`       |      4 - 2  = `2`            |
|    P4     |     `7`     |     `3`    |      [0]           |       `12`         |           12 - 7  = `5`       |      5 - 3  = `2`            |
|    P5     |     `3`     |     `8`    |      [5,2, 0]      |       `25`         |           25 - 3  = `22`      |      22 - 8 = `14`           |

Average Waiting Time(AWT): (16 + 12 + 2 + 2 + 14)/ 5 = 9.2 


Ready Queue=[~~P1~~ , ~~P5~~ , ~~P2~~ , ~~P4~~ , ~~P3~~ , ~~P1~~ , ~~P5~~ , ~~P2~~ , ~~P1~~ , ~~P5~~ ]

## Gantt Chart 
| Process No.|  P1   |  P5   |  P2   | P4   |  P3   |  P1   | P5    | P2    | P1    | P5    |
|     :---:  | :---: | :---: | :---: | :---:| :---: | :---: | :---: | :---: | :---: | :---: |
| Time       |  3    |  6    | 9     | 12   | 14    | 17    | 20    | 22    | 23    | 25    |