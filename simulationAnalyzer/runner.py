__author__ = 'smcho'

"""
This script executes the one simulator

#! /bin/sh
HOME=../out/production/one_simulator/
LIBS=../lib/ECLA.jar:../lib/DTNConsoleConnection.jar:../lib/lift-json_2.11-2.6.2.jar
SCALA=/Users/smcho/.ivy2/cache/org.scala-lang/scala-library/jars/scala-library-2.11.7.jar
CHITCHAT=../out/production/contextprocessor/:../out/production/contextsummary/
java -Xmx512M -cp $HOME:$LIBS:$SCALA:$CHITCHAT core.DTNSim -b 1 experiment/simulation/open_air_book_fair/cl.txt
java -Xmx512M -cp $HOME:$LIBS:$SCALA:$CHITCHAT core.DTNSim -b 1 experiment/simulation/open_air_book_fair/cj.txt
java -Xmx512M -cp $HOME:$LIBS:$SCALA:$CHITCHAT core.DTNSim -b 1 experiment/simulation/open_air_book_fair/cb.txt

"""
import subprocess
import os
import sys

class Runner(object):

    def __init__(self, path):
        self.path = path
        self.pathBaseDirectory = path.getBaseDirectory()

    def run(self, configFilePath):
        baseDirectory = self.pathBaseDirectory + "../../"
        simulationDirectory = baseDirectory + "one_simulator/"

        paths = {
            "HOME":"{}/out/production/one_simulator/".format(baseDirectory),
            "LIBS":"{baseDirectory}/lib/ECLA.jar:{baseDirectory}/lib/DTNConsoleConnection.jar:{baseDirectory}/lib/lift-json_2.11-2.6.2.jar".format(baseDirectory=baseDirectory),
            "SCALA":"/Users/smcho/.ivy2/cache/org.scala-lang/scala-library/jars/scala-library-2.11.7.jar",
            "CHITCHAT":"{baseDirectory}/out/production/contextprocessor/:{baseDirectory}/out/production/contextsummary/".format(baseDirectory=baseDirectory)
        }

        backup = os.getcwd()
        os.chdir(simulationDirectory)
        cmd = ['java', '-Xmx512M', '-cp', "{HOME}:{LIBS}:{SCALA}:{CHITCHAT}".format(**paths), 'core.DTNSim', \
           '-b', '1', configFilePath]
        #print cmd
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in iter(p.stdout.readline, ''):
            print line,
            sys.stdout.flush()
        p.wait()

        os.chdir(backup)

# if __name__ == "__main__":
#     configFilePath="/Users/smcho/Desktop/code/ContextSharingSimulation/experiment/simulation/bookfair/SimpleShareLogic/simple/output/configs/cj.txt"
#     runSimulation(configFilePath)