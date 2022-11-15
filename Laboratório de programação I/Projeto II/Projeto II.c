#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>



typedef struct agenda{
    char nome[40];
    char cad[15];
    struct agenda *prox;
    struct tel *t;
    struct cel *c;
    struct mail *m;
}Agenda;
typedef struct tel{
       char telefone[15];
       struct tel *prox;
}Tel;
typedef struct cel{
       char celular[15];
       struct tel *prox;
}Cel;
typedef struct mail{
       char email[40];
       struct mail *prox;
}Mail;
struct agenda* criaAgenda (){
     return NULL;
}
struct tel* criaTel(){
     return NULL;
}
struct cel* criaCel(){
     return NULL;
}
struct mail*criaMail(){
       return NULL;
}
void insereTel(struct tel **t,char tel[]){
     Tel *p,*q;

      p=(struct tel*)malloc(sizeof(struct tel));
      strcpy(p->telefone,tel);
      p->prox=*t;
      *t=p;
}
void insereCel(struct cel **c,char cel[]){
     Cel *p,*q;

      p=(struct cel*)malloc(sizeof(struct cel));
      strcpy(p->celular,cel);
      p->prox=*c;
      *c=p;
}
void insereMail(struct mail **m,char mail[]){
     Mail *p;
      p=(struct mail*)malloc(sizeof(struct mail));

      strcpy(p->email,mail);
      p->prox=*m;
      *m=p;
}
void inserePessoa (struct agenda **L, struct tel *T,struct cel *C,struct mail *M, char n[], char end[]){
     struct agenda *p;

     p=(struct agenda*)malloc(sizeof(struct agenda));

     strcpy(p->cad,n); strcpy(p->nome,end);
     p->prox=*L;
     p->t=T;
     p->c=C;
     p->m=M;
     *L=p;
}
struct agenda* localiza(struct agenda *L,char n[]){
     struct agenda *p;
     struct tel *auxt;
     struct cel *auxc;
     struct mail *auxm;
     int cont=0;
     p=L;
     auxt=p->t;
     auxc=p->c;
     auxm=p->m;
     while(p!=NULL){
        if (strcmp(p->cad,n)!=0)
            p=p->prox;
          else{
                  printf("\n\n Cadastro -> %s",p->cad);
                  printf("\n Nome -> %s",p->nome);
                  while(auxt!=NULL){
                     printf("\n Telefone -> %s",auxt->telefone);
                     auxt =auxt->prox;
                  }
                  while(auxc!=NULL){
                     printf("\n Celular -> %s",auxc->celular);
                     auxc =auxc->prox;
                  }
                  while (auxm!=NULL){
                     printf("\n Email -> %s",auxm->email);
                     auxm=auxm->prox;
                  }

           return p;
           }

     }
     return NULL;
}
void listarTodos(struct agenda *L){
     struct agenda *p;
     struct tel *auxt;
     struct cel *auxc;
     struct mail *auxm;
     p=L;
     auxt=p->t;
     auxc=p->c;
     auxm=p->m;
     while (p!=NULL){
             printf("\n\nCadastro -> %s",p->cad);
             printf("\n\nNome -> %s",p->nome);
             while(auxt!=NULL){
                    printf("\n\nTelefone -> %s",auxt->telefone);
                    auxt =auxt->prox;
                  }
             while(auxc!=NULL){
                    printf("\n\nCelular -> %s",auxc->celular);
                    auxc =auxc->prox;
              }

              while (auxm!=NULL){
                    printf("\n\nEmail -> %s",auxm->email);
                    auxm=auxm->prox;
              }
           p=p->prox;
           printf("\n\n=================\n\n");
     }
}

void listaLetra(struct agenda *L,char n){
     struct agenda *p;
     struct tel *auxt;
     struct cel *auxc;
     struct mail *auxm;
     p=L;
     auxt=p->t;
     auxt=p->c;
     auxm=p->m;
     while (p!=NULL){
           if(p->cad[0]!=n)
              p=p->prox;
           else{
             printf("\n\nCadastro -> %s",p->cad);
             printf("\n\nNome -> %s",p->nome);
             while(auxt!=NULL){
                     printf("\n\nTelefone -> %s",auxt->telefone);
                     auxt=auxt->prox;
                  }

                  while (auxm!=NULL){
                     printf("\n\nEmail -> %s",auxm->email);
                     auxm=auxm->prox;
                  }
             p=p->prox;
             printf("\n\n======================\n\n");
             }
     }
}
void alterarDados(struct agenda *L,char n[]){
     int cont=0;
     struct agenda *p;
     struct tel *auxt;
     struct cel *auxc;
     struct mail *auxm;
     auxt=p->t;
     auxt=p->c;
     auxm=p->m;
     p=localiza(L,n);
        if(p==NULL)
        printf("\nCadastro não encontrado");
        else{
                printf("\n\nDigite o novo nome:");
                scanf("%s",&p->nome);

                while (auxt!=NULL){
                      printf("\n\n Digite o novo telefone:");
                      scanf("%s",&auxt->telefone);
                      auxt=auxt->prox;
                }
                while (auxc!=NULL){
                      printf("\n\n Digite o novo celular:");
                      scanf("%s",&auxc->celular);
                      auxc=auxc->prox;
                }
               while (auxm!=NULL){
                     printf("\n\n Digite o novo email:");
                     scanf("%s",&auxm->email);
                     auxm=auxm->prox;
               }
    }
}
struct agenda* removercadastro(struct agenda *L,char n[]){
    struct agenda *p, *q;
    p=localiza(L,n);
    if (p==NULL)
        printf("\n\n Cadastro não encontrado !");
    else{
        q=L;
        if(q==p){
            L=p->prox;
            free(p);
        }else{
        while (q->prox!=p)
            q=q->prox;

         q->prox=p->prox;
         free(p);
        }
        printf("\n\n Cadastro removido com sucesso !");
    }
    return L;
}
void LimpaLista(struct agenda *L){
    struct agenda *p, *q;
    p=L;
    q=L;
    if (p==NULL)
        printf("\n\n Lista vazia");
    else{
        q=L;
        if(q==p){
            L=p->prox;
            free(p);
        }else{
        while (q->prox!=p)
            q=q->prox;

         q->prox=p->prox;
         free(p);
        }
        printf("\n\n Lista limpa !");
    }
    //return L;
}



int main(void){
    setlocale(LC_ALL, "portuguese");

    struct agenda *Lista;
    struct tel *Tel;
    struct cel *Cel;
    struct mail *Mail;
    int op;
    char cad[15], nome[40], telefone[15],celular[15], email[40];
    char no;

    Lista=criaAgenda();
    Tel=criaTel();
    Mail=criaMail();

    do{
          system("cls");
          printf("\n<<<< AGENDA >>>>>\n");
          printf("\n[1] - Cadastrar Contato ");
          printf("\n[2] - Listar todos ");
          printf("\n[3] - Pesquisar contato (Codigo do Cadastro)");
          printf("\n[4] - Excluir contato");
          printf("\n[5] - Excluir Agenda");
          printf("\n[6] - Sair da agenda");


          printf("\n\nDigite -> ");
          fflush(stdin);
          scanf("%d",&op);

      switch (op){
         case 1: printf("\nCodigo do cadastro -> ");
                 fflush(stdin);
                 scanf("%s",cad);
                 printf("\nNome -> ");
                 fflush(stdin);
                 scanf("%s",nome);

                 do{
                    printf("\nTelefone -> ");
                    fflush(stdin);
                    scanf("%s",telefone);
                    insereTel(&Tel,telefone);
                    printf("\nPossui mais telefones? -> [1] Sim [2] Nao\n");
                    scanf("%d",&op);
                 }while(op!=2);

                 do{
                    printf("\nCelular -> ");
                    fflush(stdin);
                    scanf("%s",celular);
                    insereTel(&Cel,celular);
                    printf("\nPossui outro celular? -> [1] Sim [2] Nao\n");
                    scanf("%d",&op);
                    }while(op!=2);

                 do{
                    printf("\nEmail -> ");
                    fflush(stdin);
                    scanf("%s", email);
                    insereMail(&Mail,email);
                    printf("\nPossui mais emails? [1] Sim [2] Nao\n");
                    scanf("%d",&op);
                    }while(op!=2);

                     inserePessoa(&Lista,Tel,Cel,Mail,cad,nome);
              break;

         case 2:      if(Lista==NULL)
                      printf("\nAgenda vazia");
                      else
                      listarTodos(Lista);
                      getch();
                      break;

         case 3:      if(Lista==NULL)
                      printf("\nAgenda vazia");
                      else{
                      printf("\n Digite um cadastro -> ");
                      fflush(stdin);
                      scanf("%s",cad);
                    if(localiza(Lista,cad)==NULL)
                      printf("\n codigo não encontrado na agenda");
                      }
                      getch();
                    break;

         case 4:      if(Lista==NULL)
                      printf("\nAgenda vazia");
                      else{
                        printf("\nDigite o codigo do aluno que deseja remover -> ");
                        scanf("%s",cad);
                        Lista=removercadastro(Lista,cad);
                        getch();
                      }
         case 5:      if(Lista==NULL)
                      printf("\nAgenda vazia");
                      else
                      LimpaLista(Lista);
                      getch();
                      break;
         case 6:
                    printf("\nSaindo da agenda\n");
        default:
                    printf("Opção invalida\n\n");


      }
    }while(op!=6);


    printf("\n\n");
    return 0;
}