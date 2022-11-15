public class Rev4 {

    public static void main(String[] args) {

        int a = 11; double b = 0; int c = 6; int d; int e;
        
        c += 1;
        System.out.println("C comecou a valer "+ c);
        a /= 2;
        System.out.println("A comecou a valer "+ a);
        b = 4 + 1.7 * a;
        System.out.println("B comecou a valer "+ b);
        e = (int) b;
        System.out.println("E comecou a valer "+ e);
        d = e % c;
        System.out.println("D comecou a valer "+ d);
        c = ++d ;
        System.out.println("\nO valor final de C e "+ c);
    }
}