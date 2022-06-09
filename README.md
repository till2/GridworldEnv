# GridworldEnv-QTableLearning

## _A custom toy gridworld for Quality Learning._

## Files

| File | Desc |
| ------ | ------ |
|  gridworld_env.py  | Custom little 3x3 gridworld with bad and good terminal states |
|  agent.py  | Includes the QTableAgent for solving small discrete environments like this gridworld |
|  train.py  | Train the QTableAgent. |
|  play.py  | Let the agent navigate in the environment by using the pretrained q_table! |
|  q_table.npy | Pretrained q_table, can be loaded in play.py. |


## Sample episode
Here the __QTableAgent__ jeff was run with __gamma = 0.9__.

```
> python3.9 play.py

Showing jeff with gamma = 0.9:

***
***
a-+

my choices are:
right is worth -1.0
up is worth 0.73
choosing greedy action up in state (0, 0)

***
a**
*-+
(0, 1) 0 False

my choices are:
up is worth 0.66
right is worth 0.81
down is worth 0.66
choosing greedy action right in state (0, 1)

***
*a*
*-+
(1, 1) 0 False

my choices are:
right is worth 0.9
down is worth -1.0
left is worth 0.73
up is worth 0.73
choosing greedy action right in state (1, 1)

***
**a
*-+
(2, 1) 0 False

my choices are:
right is worth 0
left is worth 0.81
down is worth 1.0
up is worth 0.81
choosing greedy action down in state (2, 1)

***
***
*-a
(2, 0) 1 True

Episode terminated.
```
