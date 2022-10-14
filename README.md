# python-logging

If you are like me, you really never quite understood the python logging module. You managed to use it, and suddenly in an application it did not log what you wantend. You started to miss important logging messages. 
You made some hacks, and hey! Messages got printed to the console! But the next application, still the same problem. Why? Because 
you never really learned it. 

I still do not understand it all, but made some discoveries with help from Martin!


In this case I am only logging to the console. You could log to a file, 
to a file, email, HTTP GET/POST locations etc. 

The purpose of the application is to calculate mass of a cube. 
It consists of a main file `run.py`, which imports a module called `mass.py`.
`mass.py` import `volume.py`. 

I want to recive a message for every function it passes. I
also want to know where in the code the message originates from. 
***


## ***Example - This works*** (how I want it to work)
### In `run.py`
```python
import logging
from sys import stdout
from utils.mass import calc_cube_mass


# Create logger instance
logger = logging.getLogger() #NOTE!
```
than in every sub module use:
```python
import logging

# Create logger instance
logger = logging.getLogger(__name__) 
```
This outputs
```
❯ python .\run.py
root - INFO - Start calculating.
utils.volume - INFO - Inside func: calc_cube_volume
utils.mass - INFO - Inside func: calc_cube_mass
root - INFO - Finished calculating.
```
## :clap:

***


## **One of mistakes**
I used to give the getLogger() method `__name__` as argument. When
run.py is called `__name__` evaluates to `__main__`. For some reason I don't 
understand, the submodules do not fire log messages to the console. 

## ***Example - This does not work***
### In `run.py`
```python
import logging
from sys import stdout
from utils.mass import calc_cube_mass


# Create logger instance
logger = logging.getLogger(__name__) #NOTE!
```
than in every sub module use:
```python
import logging

# Create logger instance
logger = logging.getLogger(__name__) 
```
Which outputs

```
❯ python .\run.py
__main__ - INFO - Start calculating.
__main__ - INFO - Finished calculating.
```

## :poop:
***



## Conclusion
Give the logger object in the root script (`run.py`)  a spesific name or if left empty, like in this example,
"root" is given by default. Then in all other sub modules, give the logger
a unique name. I use the builtin `__name__` in this case, then the logger hierarchy
mirrors the application sctructure.

### ***Sources***

[Python - Logging HOWTO](https://docs.python.org/3/howto/logging.html)


