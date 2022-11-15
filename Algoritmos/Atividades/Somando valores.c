int main()
{
    double val, soma;
    int contagem;

    Soma = 0.0;

    contagem = 1;

    while (contagem <= 5) {
        printf("\nDigite o %do. numero: ", contagem);
        scanf ("%lf", &val);
        soma += val;
        contagem++;
    }
    printf ("\nO resultado da soma eh: %.2f", soma);
    system("pause");
    return 0;

}