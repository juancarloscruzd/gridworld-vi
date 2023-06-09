# Gridworld Value Iteration

Pasos para ejecutar el código

```bash
cd src 
python deterministic.py
python stochastic.py
```
Si quieres cambiar de archivo, puedes modificar la línea `152` del archivo `deterministic.py`

```python
...
if __name__ == '__main__':

    domain_file = './PruebasGrid/FixedGoalInitialState/navigation_1_grid.net'
...
```

Igualmente, en el archivo `stochastic.py`, modificar la línea `160`
```python
...
if __name__ == '__main__':

    domain_file = './PruebasGrid/FixedGoalInitialState/navigation_2_grid.net'
...
```