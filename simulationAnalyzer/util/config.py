from path import *
from property import *

template = """\
MovementModel.rngSeed = {rngSeed}
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

class Config(Property):
    #
    # def __init__(self, controlFilePath):
    #     super(self.__class__, self).__init__(controlFilePath)

    def writeConfigurationFile(self, controlFilePath, groupsFilePath, control):
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
                     "iteration", "id", "rngSeed"] #MovementModel.rngSeed = 1
            for key in control:
                if not (key in names):
                    print key, key in names, control
                    raise Exception("%s not in names" % key)

        preconditionCheck(control)
        with open(groupsFilePath) as f:
            groups = f.read()

        headers = template.format(**control)

        with open(controlFilePath, "w") as f:
            f.write(headers + "\n\n#--------------------\n# GROUP CONFIGURATION COPY\n\n" + groups)

        return controlFilePath

    def readConfigurationFile(self, propertyFilePath):
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
        d = self.read(propertyFilePath) # returns a dictionary
        for key in d:
            result[key] = getValue(d[key])
        return result
