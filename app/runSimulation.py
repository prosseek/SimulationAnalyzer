__author__ = 'smcho'

from simulationAnalyzer.config_generator import *
from simulationAnalyzer.context_generator import *
from simulationAnalyzer.buffer_size_generator import *
from simulationAnalyzer.runner import *

import glob
import os

def removeDirectory(directory):
    files = glob.glob(directory + os.sep + "*.*")
    for f in files:
        os.unlink(f)

def purge(simName, sta, id):
    p = Path(simName, sta, id)
    directories = [p.getConfigDirectory(), p.getContextDirectory(), p.getReportDirectory(), p.getResultDirectory()]
    for d in directories:
        removeDirectory(d)

if __name__ == "__main__":
    simName = "open_air_book_fair"
    sta = "SimpleShareLogic"
    id = "simple_5000"
    controlName = "control1.txt"

    purge(simName, sta, id)

    cfg = ConfigGenerator(simName, sta, id, controlName)
    configs = cfg.create()

    r = Runner(cfg.getPath())

    for c in configs:
        cxg = ContextGenerator(simName, sta, id)
        cxg.create()
        bfg = BufferSizeGenerator(simName, sta, id)
        bfg.create()
        r.run(c)
