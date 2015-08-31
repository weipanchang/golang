package dewpointtemperature;
import java.util.Scanner;



public class dewpointtemperature {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int num = in.nextInt();
		if (num >= 75) {
		   System.out.printf("The temperature is %d, and I feel Extremely uncomfortable\n", num);
		}
		if ((num >= 70) && (num <= 74)) {
		   System.out.printf("The temperature is %d, and I feel Extremely uncomfortable\n", num);
			}
		if ((num >= 65) && (num <= 69)) {
		   System.out.printf("The temperature is %d, and I fell Somewhat uncomfortable\n", num);
				}
		if ((num >= 60) && (num <= 64)) {
		   System.out.printf("The temperature is %d, and I fell OK\n", num);
				}
		if ((num >= 50) && (num <= 59)) {
			   System.out.printf("The temperature is %d, and I fell Very comfortable\n",  num);
		   }
		if (num <= 49) {
		   System.out.printf("The temperature is %d, and I fell A bit dry\n", num);
					}
	}
}
