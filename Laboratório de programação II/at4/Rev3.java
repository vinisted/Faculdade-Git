public class Rev3 {

    public static void main(String[] args) {

        int num1 = 2, num2 = 3, num3 = 0, num4 = 4;
        num1 = (num2 + num1) % 2;
        num2 = (num2 - num3) * num1;
        num3 = num1 + num4/2 - 3;

        System.out.printf("Num1 = %d\n", num1);
        System.out.printf("Num2 = %d\n", num2);
        System.out.printf("Num3 = %d\n", num3);
        System.out.printf("Num4 = %d\n", num4);

    }
}