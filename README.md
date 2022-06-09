# GridworldEnv-QTableLearning

### _A little toy gridworld for Q-Learning._

### The environment looks like this:

|‎|‎|‎|
| --- | --- | --- |
| [0,2] | [1,2] | [2,2] |
| [0,1] | [1,1] | [2,1] |
| [0,0] init | [1,0] 🔥| [2,0] ⭐ |

### Rewards:

|‎|‎|‎|
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 0 | 0 |
| 0 | -1 | +1 |

### Learned values with gamma = 0.9:

|‎|‎|‎|
| --- | --- | --- |
| 0.66 | 0.73 | 0.81 |
| 0.73 | 0.81 | 0.9 |
| 0.66 | -1.0 | 1.0 |

## Files

| File | Desc |
| ------ | ------ |
|  ![gridworld_env](gridworld_env.py)  | Little 3x3 gridworld. |
|  ![agent](agent.py)  | QTableAgent for solving small discrete environments like this gridworld |
|  ![train](train.py)  | Train the QTableAgent. |
|  ![play](play.py)  | Let the agent navigate in the environment by using the pretrained q_table! |
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
