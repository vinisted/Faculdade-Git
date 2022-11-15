import java.util.Scanner;

//Neste programa contem as seguintes tarefas: Variáveis, if...else, switch...case e break

public class Q1 {

    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        int num1, num2; 
        String op;

        System.out.printf("\nCalculadora simples\n");

        System.out.printf("\nDigite 'a' para adicao");
        System.out.printf("\nDigite 's'para subtracao");
        System.out.printf("\nDigite 'm'para multiplicacao");
        System.out.printf("\nDigite 'd'para divisao\n");
        System.out.printf("\n");
        System.out.printf("Operacao matematica:");
        op = ler.next();

        System.out.printf("Informe o primeiro valor: ");
        num1 = ler.nextInt(); 

        System.out.printf("Informe o segundo valor: ");
        num2 = ler.nextInt(); 
          
        switch (op) {
            case "a":
                System.out.printf("%d + %d = %d\n", num1, num2, (num1 + num2));
                break;
            case "s":
                System.out.printf("%d - %d = %d\n", num1, num2, (num1 - num2));
                break;
            case "m":
                System.out.printf("%d * %d = %d\n", num1, num2, (num1 * num2));
                break;
            case "d":
                if (num1%num2==0){
                System.out.printf("%d / %d = %d\n", num1, num2, (num1 / num2));
            }
                else {
                System.out.printf("%d / %d = %6.2f\n", num1, num2, ((double)num1 / num2));
            }
                break;
            default:
                System.out.printf("Caractere invalido");
        }

    }

}