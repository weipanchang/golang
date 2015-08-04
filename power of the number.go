package main

import ("fmt"
        "math"
)

func main() {
   var num int
   fmt.Scanf("%d", &num)
   i := num * num
   f := float64(num)
   j := math.Pow(f, 2)
   fmt.Println(i)
   fmt.Printf("%d power of 2 is %f \n", num, j)
   fmt.Printf("%d power of 2 is %d \n", num, int(j))
}