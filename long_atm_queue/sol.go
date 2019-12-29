package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	var i int
	var p int
	var c int = 1

	for i = 0; i < n; i++ {
		var t int
		fmt.Scanf("%d", &t)
		if t < p {
			c = c + 1
		}
		p = t
	}

	fmt.Println(c)

}
