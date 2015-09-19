__author__ = 'smcho'

from simulationAnalyzer import Reader as S
from simulationAnalyzer import getResultFilePath

if __name__ == "__main__":
    simulationName = "open_air_book_fair"
    p = S(simulationName, "SimpleShareLogic", "b")

    # When market ma get the context from g1c0
    p.getTime("ma", 1, "v", 1)