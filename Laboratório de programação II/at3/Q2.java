import java.util.Scanner;

//Neste programa contem as seguintes tarefas: for e continue

public class Q2 {

    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);
        int num;

        System.out.printf("\nInforme o valor: ");
        num = ler.nextInt();

        System.out.printf("\nNumeros pares de 0 a %d:\n", num);
        int soma = 0, j=0;
        for (int i = 0; i <=num; i++) {

            if(i%2==0){
                ++j;
                System.out.printf("%d num par: %d\n", j, i);
                soma += i;
            }
            else
                continue;

            System.out.printf("Soma dos pares: %d\n", soma);
            System.out.printf("\n");
        }

    }
}