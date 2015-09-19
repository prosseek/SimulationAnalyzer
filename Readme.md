### [2015/09/19]

The `hostToTupleMap` has a map to string to contexts, but the dictionary format is not necessary. 

    "hostToTuplesMap":{
      "0":[

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