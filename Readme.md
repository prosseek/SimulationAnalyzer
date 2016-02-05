# The code

This is code for the analysis of simulation results from ONE simulator execution.

### [2015/09/19]

The three information to search for the results JSON file

* simulationName
* strategy
* summaryType

The `hostToTupleMap` has a map to string to contexts, but the dictionary format is not necessary. 

    "hostToTuplesMap":{
      "0":[

This is the context information that host 56 receives

     dict['56']
    
     [[0, 0, 0.0, u'g3c56b', 29],
      [19, 56, 4722.22, u'g2c40b', 29],
      [39, 56, 6849.11, u'g3c56b', 29],
      [65, 56, 5933.99, u'g2c27b', 29]],

  This method returns the group information of host 56 from
  1. u'g3c56b'
  2. configuration file
     Group3.groupID = p
     Group3.nrofHosts = 40


### [2015/09/18]

Remove the old jsonAnalyzer

1. `/Library/Python/2.7/site-packages`
2. remove: simulationAnalyzer-0.1-py2.7.egg
3. remove: `easy-install.pth`
    * `./simulationAnalyzer-0.1-py2.7.egg`

### [2015/09/15]

#### Setup

python setup build
python setup develop
python setup install
python setup sdist

#### References

* <http://learnpythonthehardway.org/book/ex46.html>
* <http://www.scotttorborg.com/python-packaging/minimal.html>
