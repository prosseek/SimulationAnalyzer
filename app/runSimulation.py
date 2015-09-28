__author__ = 'smcho'

from unittest import TestCase
from simulationAnalyzer.generator import *
from simulationAnalyzer.util.path import *
from simulationAnalyzer.runner import *

if __name__ == "__main__":
    p = Path("open_air_book_fair", "SimpleShareLogic", "simple_5000")
    controlName = "control1.txt"
    g = Generator(p, controlName)
    configs = g.create()
    r = Runner(p)

    for c in configs:
        r.run(c)