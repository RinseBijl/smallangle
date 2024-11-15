import click
import numpy as np
from numpy import pi
import pandas as pd

#function calculating sin values
def sin(number):
    """calculates sine values from 0 to 2 pi

    Args:
        number (int): the number of steps 
    """    
    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    

#function calculating tangent values
def tan(number):
    """calculates tangents values from 0 to 2pi

    Args:
        number (int): the number of steps
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

@click.group()
def cli():
    """This is a tool for calculating the values of sin en tan by using the commands sine and tangent.
    """    
    pass


@cli.command()
@click.option('-n', 
default=10,
help='number of steps between 0 en 2π'
)
def sine(n):
    """calculates the sin values given a specifick number of steps
    """    
    print(sin(n))


@cli.command()
@click.option('-n',
default=10,
help='number of steps between 0 en 2π'
)
def tangent(n):
    """calculates the tan values given a specifick number of steps
    """    
    print(tan(n))




if __name__ == "__main__":
    sin(10)
    tan(10)
 