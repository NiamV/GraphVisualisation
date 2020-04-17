object GraphInput{
    def graphInput(fname: String): DirectedGraph = {
        import scala.io.Source

        val file = Source.fromFile(fname).getLines
        val n = file.length

        var m = new Array[Array[Int]](n)
        var j = 0

        for (line <- Source.fromFile(fname).getLines) {
            var row = line.split(", ")
            var rowMat = new Array[Int](n)
            var i = 0
            for(elem <- row){
                if(elem == "MAX"){
                    rowMat(i) = Int.MaxValue
                } else{
                    rowMat(i) = elem.toInt
                }
                i += 1
            }
            m(j) = rowMat
            j += 1
        }

        return DirectedGraph(m)
    }
}