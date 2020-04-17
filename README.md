# Graph Visualisation

This uses Scala to run Dijkstra's algorithm on a given graph, and outputting the results into the file `DijkstraOutput.txt`. Then pygame is used to animate the results.

To run the scala algorithm:

```
fsc Graph.scala MinPriorityQueue.scala Dijkstra.scala GraphInput.scala main.scala
scala main > DijkstraOutput.txt
```

To run the pygame animation:

```
python DijkstraVisual.py
```