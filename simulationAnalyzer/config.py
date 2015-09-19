import os

__author__ = 'smcho'

baseDirectory = "/Users/smcho/Desktop/code/ContextSharingSimulation/experiment/simulation"

def getResultFilePath(simulationName, strategy, summaryType):
    simulationDirectory = baseDirectory + "/{}".format(simulationName)
    resultDirectory = simulationDirectory + "/results/"

    abspath = os.path.abspath("{resultDirectory}/result_smcho.{strategy}_{summaryType}.json".format(
        resultDirectory = resultDirectory, strategy = strategy, summaryType = summaryType))
    return abspath

def getConfigurationFilePath(simulationName):
    simulationDirectory = baseDirectory + "/{}".format(simulationName)
    abspath = simulationDirectory + "/c.txt"
    return abspath

def parseConfigurationFile(simulationName):
    """
    From simulation name, returns the configuration in a map

    For example:

    MovementModel.warmup = 10
    Scenario.endTime = 10000
    ContextSummary.summaryType = b

    map['MovementModel.warmup'] = 10
    map['Scenario.endTime'] = 10000
    map['ContextSummary.summaryType'] = 'b'

    """
    def getValue(value):
        if "[" in value:
            value = value[1:-1]

        if "," in value:
            try:
                return [int(x.strip()) for x in value.split(",")]
            except ValueError:
                return [float(x.strip()) for x in value.split(",")]

        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value # string

    c = getConfigurationFilePath(simulationName)
    with open(c, "r") as f:
        lines = f.readlines()
        f.close()

    map = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0: continue
        if line.startswith("#"): continue

        if "=" in line:
            (key, value) = line.split("=")
            map[key.strip()] = getValue(value.strip())
    return map
