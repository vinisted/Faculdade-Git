#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Coff{
  char nome[50];
  struct Coff *prox;
} coff;

coff* inicializar(){
  return NULL;
}

void inserir_fim(coff** lista, char nome[50]){
  coff* novo = malloc(sizeof(coff));
  strcpy(novo->nome,nome);
  if(*lista==NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  } else {
    coff* p = *lista;
    while(p->prox!=NULL){
      p = p->prox;
    }
    p->prox = novo;
  }
}

void imprimir(coff* lista){

  int i=2;

  while(lista != NULL){
    printf("O %dº a comprar será: %s\n", i,lista->nome);
    lista=lista->prox;
    i++;
  }
}

void proximo(coff* lista){
  printf("O próximo a comprar o café será: %s\n",lista->nome);
}

void trocar(coff** lista){
  if(*lista != NULL){
    coff* aux = *lista;
    *lista = (*lista)->prox;
    coff* novo = malloc(sizeof(coff));
    novo=aux;
    novo->prox=NULL;
  if(*lista==NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  } else {
    coff* p = *lista;
    while(p->prox!=NULL){
      p = p->prox;
    }
    p->prox = novo;
    }
  }
}

int main(void) {

  printf("\r\n");
  printf("----------- O CLUBE DO CAFÉ -----------\n");
  printf("Controle da compra do café\n");
  printf("\r\n");

  coff* lista = inicializar();
  int ins=1;
  
while (ins!=2){

  char nome [100];

  printf("Deseja digitar um novo contribuinte? SIM=1/NAO=2 ");
  scanf("%d", &ins);
  printf("\r\n");

  if (ins==1){
  printf("Digite um novo contribuinte: (Digite '-' para dar espaço) ");
  scanf("%s", nome);
  printf("\r\n");
  inserir_fim(&lista,nome);
  }

  if (ins==2) {
    break;
  }
}
  
  proximo (lista);
  trocar(&lista);
  imprimir(lista);

  return 0;
}