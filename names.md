### [2015/09/19]

#### Names

1. host: 0, 1, 2, ... (it starts with number 0)

2. group: 1, 2, 3 ... (it starts with number 1)

3. acc: Accumulation of the number of each group
    * [1,2,43]
    * group1 has 1 item, group2 has 1 thus the accumulation becomes 2
    * (host in group 1) < acc[0]; always smaller
        * in general (host in group N) < acc[N-1] 

4. groupID
    * v : visitor (only 1)
    * s : similar (N)
    * p : people  (N)
    * ma - mz
     
5. groupIDIndex
    * groupID + Index
        * 'v' + 1 -> g(v's group) + (sum of previous groups) + (1 - 0)
        
6. context
    * g1c0b 
        * group1 (v) and it's host 0 (as there is only one host in group v)
        * b means the conext format is in bloomier filter (FBF)

7. JSON file format data     
    * contextTuple
    * `[37, 81, 5233.88, u'g3c69b', 29]`
        * from, to, time, context, size
    * hostContextSummary
        * the summary that each host contains
        * {"name":"g1c0", "sizes":[105,52,29], "fileName":"g1c0.json"}
    } 
   
8. The map JSON contains
    * `"hostToTuplesMap"` stores a map[Int -> List[contextTuple]]
    * `"summaries"` stores a list[hostContextSummary]
        
        
#### conversion names

* contextToGroupIDIndex/groupIDIndexToContext
    * g1c0b -> v1 or vice versa
    * the `hostToTupleMap` has contextTuple who's fourth member is context (i.e., g3c69b)
    * It means that this context is from the host 69, group 3 (p)
    * I'm more familiar with groupIDIndex name (p3)
* hostToGroupIDIndex/groupINIndexTohost
    * 0 -> v1 or vice versa
* hostToGroup
    * Given host returns Group number
        * 0 -> 1
        * 1 -> 2
* hostToGroupID
    * Given host returns GroupID
        * 0 -> v
        * 1 -> s
