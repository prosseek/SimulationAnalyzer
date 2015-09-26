from simulationAnalyzer.util.path import *

def writeConfigurationFile(simulationFilePath):
    pass

def readConfigurationFile(simulationName):
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
