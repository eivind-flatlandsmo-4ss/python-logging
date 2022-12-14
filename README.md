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
also want to know which module the message originates from. 
***


## ***Example - This works*** (how I want it to work)
### In `run.py`
```python
import logging
from sys import stdout
from utils.mass import calc_cube_mass


# Create logger instance
logger = logging.getLogger("root") #NOTE!
```
than in every sub module use:

```python
import logging

logger = logging.getLogger(f"root.{__name__}")
```
This outputs
```
❯ python .\run.py
root - INFO - Start calculating.
root.utils.volume - INFO - Inside func: calc_cube_volume
root.utils.mass - INFO - Inside func: calc_cube_mass
root - INFO - Finished calculating.
```
## :clap:

***


## **One of my mistakes**
I used to give the getLogger() method `__name__` as argument. When
run.py is called `__name__` evaluates to `__main__`. For some reason I don't 
understand, the submodules do not fire log messages to the console. 

## ***Example - This does not work (How I want it to work. )***
I want the all log messages in the entire application to log to the console. 
I also want to know which module the log message originates from. Why?
To make debugging easiser by knowing where the the execution of the program is.
### In `run.py`
```python
import logging
from sys import stdout
from utils.mass import calc_cube_mass


# Create logger instance
logger = logging.getLogger(__name__) 

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

## ***Example - This does not work in applications which imports libraries that are using logging.***
```python
# Or
logger = logging.getLogger("") # will work in this small application. BUT, 
                               # it could result in catching a lot of logs
                               # from other libraries that are using logging.
# Or
logger = logging.getLogger()  # will work in this small application. BUT, 
                              # it could result in catching a lot of logs
                              # from other libraries that are using logging.
```

## :poop:
***



## Conclusion
Give the logger object in the root script (`run.py`)  a spesific name, in this example,
"root" is given. Then in all other sub modules, give the logger
a unique name prefixed with the loggers name set in `run.py`. 
E.g. `logging.getLogger(f"root.{__name__}")`
I use the builtin `__name__` in this case, then the logger hierarchy
mirrors the application sctructure. There is propably better ways to do this, but this works for me. 

### ***Sources***

[Python - Logging HOWTO](https://docs.python.org/3/howto/logging.html)


