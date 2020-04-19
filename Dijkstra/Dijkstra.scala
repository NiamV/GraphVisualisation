object Dijkstra{
    def Dijkstra(g: DirectedGraph, s: Int): (Array[Int], Array[Int]) = {
        val d = new Array[Int](g.n)
        val pi = new Array[Int](g.n)

        val qArray = new Array[(Int, Int)](g.n)

        //Initialisation
        var i = 0
        while(i < g.n){
            d(i) = Int.MaxValue
            pi(i) = -1

            qArray(i) = (i, d(i))
            i += 1
        }

        d(s) = 0
        qArray(s) = (s, 0)

        var q = MinPriorityQueue(qArray)

        var counter = 0

        while(!(q.isEmpty)){
            var u = q.delMin()
            for(v <- 0 until g.n){
                var updated = false
                if(u._2 + g.adjMatrix(u._1)(v) < d(v) && u._2 + g.adjMatrix(u._1)(v) > 0){
                    updated = true
                    d(v) = u._2 + g.adjMatrix(u._1)(v)
                    pi(v) = u._1
                    q.decreaseKey(v, d(v))
                }

                if(g.adjMatrix(u._1)(v) != Int.MaxValue){
                    println("Iteration: " + counter)
                    println(u._1)
                    println(v)
                    println(updated)
                    println(Printing.printArray(d))
                    println(Printing.printArray(pi))
                    println
                    counter += 1
                }                    
            }
        }

        (d, pi)
    }
}


object Printing{
    def printArray(a: Array[Int]): String = {
        var output = ""
        for(elem <- a){
            output += elem.toString
            output += " "
        }
        output
    }
}