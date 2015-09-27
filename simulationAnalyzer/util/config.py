from path import *
from property import *

template = """\
##################### CONTROL FOR SIMULATION
btInterface.transmitRange = {transmitRange}
Scenario.endTime = {endTime}
ContextSummary.summaryType = {summaryType}

##################### SIMULATION CONTROL
Scenario.name = {simulationName}
Scenario.simulateConnections = true
Scenario.updateInterval = 0.01

# Define new application
contextSharingApp.type = ContextSharingApplication

# Set Ping app for all nodes
Group.nrofApplications = 1
Group.application1 = contextSharingApp

# Add report for Context Sharing App
Report.nrofReports = 2
Report.report2 = ContextSharingAppReporter

#################### OTHER STUP
MovementModel.warmup = 10

##################### DIRECTORY & STRATEGY
# ContextSummary storage directory
# directory where the contexts are located
ContextSummary.contextDirectory = {contextDirectory}
ContextSummary.resultFilePath = {resultFilePath}
# Sharing strategy
ContextSummary.strategy = smcho.{strategy}
"""

def writeConfigurationFile(destinationFilePath, groupsFilePath, control):
    """
    simulationName
    strategy

    transmitRange
    endTime

    summaryType

    directory

    :param destinationFilePath:
    :param groupsFilePath:
    :param control:
    :return:
    """
    def preconditionCheck(control):

        # I don't use iteration/id in the template, but it is given from control
        names = ["simulationName", "strategy", "transmitRange","endTime",\
                 "summaryType", "contextDirectory", "resultFilePath", \
                 "iteration", "id"]
        for key in control:
            if not (key in names):
                print key, key in names, control
                raise Exception("%s not in names" % key)

    preconditionCheck(control)
    with open(groupsFilePath) as f:
        groups = f.read()

    headers = template.format(**control)

    with open(destinationFilePath, "w") as f:
        f.write(headers + "\n\n#--------------------\n# GROUP CONFIGURATION COPY\n\n" + groups)

    return destinationFilePath

def readConfigurationFile(propertyFilePath):
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
    result = {}
    p = Property(propertyFilePath)
    d = p.read() # returns a dictionary
    for key in d:
        result[key] = getValue(d[key])
    return result

    # c = getConfigurationFilePath(simulationName)
    # with open(c, "r") as f:
    #     lines = f.readlines()
    #     f.close()
    #
    # map = {}
    # for line in lines:
    #     line = line.strip()
    #     if len(line) == 0: continue
    #     if line.startswith("#"): continue
    #
    #     if "=" in line:
    #         (key, value) = line.split("=")
    #         map[key.strip()] = getValue(value.strip())
    # return map
