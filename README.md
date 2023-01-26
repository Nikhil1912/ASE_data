# ASE_data
[![Unit tests](https://github.com/Nikhil1912/ASE_data/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/Nikhil1912/ASE_data/actions/workflows/unit-tests.yml)



- To view all command line options run 
    ```python code/Main.py --help True ```

- To Run test cases 
    ```python code/Main.py```


```
Here are the list of options

OPTIONS:
  -d  --dump  on crash, dump stack = False
  -f  --file  name of file         = ../etc/data/auto93.csv
  -g  --go    start-up action      = data
  -h  --help  show help            = False
  -s  --seed  random number seed   = 937162211

To run

python code/Main.py --seed 937162211

```

```
✅PASS : eg_check_nums
✅PASS : eg_check_rands
✅PASS : eg_check_syms
✅PASS : eg_csv
✅PASS : eg_data
y mid {'Lbs-': 2970.42, 'Acc+': 15.57, 'Mpg+': 23.84}
 div {'Lbs-': 846.84, 'Acc+': 2.76, 'Mpg+': 8.34}
x mid {'Clndrs': 5.45, 'Volume': 193.43, 'Model': 76.01, 'origin': 1}
 div {'Clndrs': 1.7, 'Volume': 104.27, 'Model': 3.7, 'origin': 1.3273558482394003}
✅PASS : eg_stats
{'dump': False, 'file': '../etc/data/auto93.csv', 'go': 'data', 'help': False, 'seed': 937162211}
✅PASS : eg_the
```
