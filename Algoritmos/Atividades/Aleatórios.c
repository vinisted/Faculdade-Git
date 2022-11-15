#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(void)
{
  int ale, num;
  
  printf("Gerando 10 valores aleatorios:\n\n");

  srand(time(NULL));
  
  for (ale=0; ale < 10; i++)
  {
    printf("%d ", rand() % 100);
  
  printf("Digite um possivel número: ");
  scanf("%d", &num);

  while (num != ale){
      printf("Não acertou o número, tente novamente: ");
      scanf("%d", &num)
  }
  
  }
  

  getch();
  return 0;
}