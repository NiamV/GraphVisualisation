object main{
    def main(args: Array[String]): Unit = {
        val g = DirectedGraph( Array(
            Array(Int.MaxValue, 4, 2, Int.MaxValue, Int.MaxValue),
            Array(Int.MaxValue, Int.MaxValue, 3, 2, 1),
            Array(Int.MaxValue, 1, Int.MaxValue, 4, 5),
            Array(Int.MaxValue, Int.MaxValue, Int.MaxValue, Int.MaxValue, Int.MaxValue),
            Array(Int.MaxValue, Int.MaxValue, Int.MaxValue, 1, Int.MaxValue)
        ) )

        val result = Dijkstra.Dijkstra(g, 0)

        // for(i <- 0 until g.n){
        //     print(i + " " + result._1(i) + " " + result._2(i))
        //     println
        // }
    }
}