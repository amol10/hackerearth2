package main
import ("fmt")

func main() {
    var n int
    fmt.Scanf("%d", &n)
    stack := make([]int, 100)
    size := 0
    
    var p int = 0
    var i int
    for i = 0; i < n; i++ {
        //if size > 0 {fmt.Println("stack top", stack[size -1])}
        if size > 0 && (stack[size - 1] - p == 1) {
            p = stack[size - 1]
            size = size - 1
            //fmt.Println("from stack", p)
            i--
        } else {
            var t int
            fmt.Scanf("%d", &t)
            if t - p > 1 {
                stack[size] = t
                //fmt.Println("stacked", t)
                size = size + 1
            } else {
                p = t
                //fmt.Println("playlisted", p)
            }
        }
    }
    if p == n {
        fmt.Println("Happy")
    } else {
        fmt.Println("Sad")
    }
}
