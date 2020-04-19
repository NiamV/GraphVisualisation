class MinPriorityQueue(max: Int){
    private val MAX = max + 2
    private val elems = new Array[(Int, Int)](MAX)
    private var size = 0

    override def toString = {
        var output = ""
        var i = 0
        while(i < size){
            output += elems(i).toString
            output += " "
            i += 1
        }
        output
    }

    def clear: Unit = size = 0

    def isEmpty: Boolean = (size == 0)

    def insert(x: Int, d: Int): Unit = {
        require(size < MAX)
        var i = size
        elems(i) = (x, d)
        var parent = (i-1)/2
        while (i > 0 && d < elems(parent)._2) {
            elems(i) = elems(parent)
            i = parent; parent = (i-1)/2
        }
        elems(i) = (x, d)
        size += 1
    }

    def delMin(): (Int, Int) = { 
        require(size > 0)

        val result = elems(0)
        size -= 1
        elems(0) = elems(size)

        heapify(0)
        result
    }

    private def heapify(ind: Int): Unit =   {
        var i = ind
        var ch = 2*i + 1 
        while (ch < size) {
            if (ch+1 < size && elems(ch)._2 > elems(ch+1)._2) ch += 1

            if (elems(i)._2 <= elems(ch)._2) return 

            val temp = elems(i)
            elems(i) = elems(ch)
            elems(ch) = temp
            i = ch; ch = 2*i+1
        }
    }

    def decreaseKey(v: Int, d: Int): Unit = {
        var i = 0
        while(i < size && elems(i)._1 != v){
            i += 1
        }

        var parent = (i-1)/2
        while (i > 0 && d < elems(parent)._2) {
            elems(i) = elems(parent)
            i = parent
            parent = (i-1)/2
        }
        elems(i) = (v, d)
    }
}

object MinPriorityQueue{
    def apply(el: Array[(Int, Int)]): MinPriorityQueue = {
        val pq = new MinPriorityQueue(el.size)
        for (x <- el) pq.insert(x._1, x._2)
        pq 
    }
}