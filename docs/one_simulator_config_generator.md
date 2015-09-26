* [2015/09/25]

To run ONE simulator, a configuration file should be given.
For changing parameters, we need to dynamically generate the simulator configuration file. 

#### The header

The first part is header, where the Python has the template, and the configuration files are read and filling in
the variables.

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
    ContextSummary.directory = {directory}
    # Sharing strategy
    ContextSummary.strategy = smcho.{strategy}
    """

The variables are from directory structure

* simulationName - from the enclosing directory
* directory - from the relative location of context
* strategy - from the enclosing directory

Or, from automatically generated

* summaryType - automatically filled with b/l/j

Also read from config.txt file

* transmitRange - config.txt (50)
* endTime - config.txt (10000)

There are only one factors to control, but we can add more easily.

#### The body

The body contains group information is copied from c.txt, so each `Id` implies a simulation
with the group information related.

    #####################
    ##################### GROUP <----
    #####################

    # Scenario groups
    Scenario.nrofHostGroups = 7

    ##################### VISITOR

    Group1.groupID = v
    Group1.nrofHosts = 1
    Group1.speed = 1.2, 1.5

    ...

