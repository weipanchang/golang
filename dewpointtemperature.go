package main

import ("fmt"
)
func main() {
   var num int
   fmt.Scanf("%d", &num)
   if num >= 75 {
   fmt.Printf("The temperature is %d, and I feel Extremely uncomfortable\n",  num)
   }
   
   if num >= 70 && num <=74 {
   fmt.Printf("The temperature is %d, and I feel Extremely uncomfortable\n",  num)
   }
   
   if num >= 65 && num <=69 {
   fmt.Printf("The temperature is %d, and I fell Somewhat uncomfortable\n",  num)
   }
   
   if num >= 60 && num <=64 {
   fmt.Printf("The temperature is %d, and I fell OK\n",  num)
   }
   
   if num >= 50 && num <=59 {
   fmt.Printf("The temperature is %d, and I fell Very comfortable\n",  num)
   } 
 
   if num <=49 {
   fmt.Printf("The temperature is %d, and I fell A bit dry\n",  num)
   } 

}