object main{
    def main(args: Array[String]): Unit = {
        val g = GraphInput.graphInput("AdjMatrix.txt")

        val result = Dijkstra.Dijkstra(g, 0)
    }
}