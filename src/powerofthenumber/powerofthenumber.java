package powerofthenumber;
import java.util.Scanner;


public class powerofthenumber {
	    public static void main(String [] args) {
	    	Scanner in = new Scanner(System.in);
	    	int num = in.nextInt();
	    	System.out.println(num + " to the power of 2 " + (int)Math.pow(num, 2));
	    	in.close();
	    	       //System.out.println("Hello World"); // prints Hello World)
	    }

}
