object main{
    def main(args: Array[String]): Unit = {
        val g = GraphInput.graphInput("AdjMatrix.txt")

        val result = Dijkstra.Dijkstra(g, 0)

        // for(i <- 0 until g.n){
        //     print(i + " " + result._1(i) + " " + result._2(i))
        //     println
        // }
    }
}