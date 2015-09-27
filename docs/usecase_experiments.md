* [2015/09/26]

## Use case experiment 1 - Generator

### Q: How the app can use the Generator to make the ONE Simulator configuration file simply?

Let's test it. 
    p = Path(simName, strategy, id)
    g = Generator(p, controlFileName)
    g.create("b")