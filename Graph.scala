class DirectedGraph(m: Array[Array[Int]]){
    val adjMatrix = m
    val n = m.size

    def printMatrix: Unit = {
        for(list <- adjMatrix){
            for(elem <- list){
                print(elem + " ")
            }
            println
        }
    }
}

object DirectedGraph{
    def apply(m: Array[Array[Int]]) = {
        val g = new DirectedGraph(m)
        g
    }
}

object Graph{
    def main(args: Array[String]): Unit = {
        val g = DirectedGraph(Array(Array(1, Int.MaxValue ,3), Array(2,3,4), Array(3,4,5)))
    
        println(g.n)
    }
}