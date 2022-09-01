#include<stdio.h>
#include <stdlib.h>
#include <string.h>
int hako[3][3];
int x,y;
void print_hyou(void){
    char marubatu[]={' ','o','x'};
    printf(" %c | %c | %c \n",marubatu[hako[0][0]],marubatu[hako[1][0]],marubatu[hako[2][0]]);
    printf("-----------\n");
    printf(" %c | %c | %c \n",marubatu[hako[0][1]],marubatu[hako[1][1]],marubatu[hako[2][1]]);
    printf("-----------\n");
    printf(" %c | %c | %c \n",marubatu[hako[0][2]],marubatu[hako[1][2]],marubatu[hako[2][2]]);
}
void player1(void){
    scanf("%d,%d",&x,&y);
    if(hako[x][y]==0){
        hako[x][y]=1;
        print_hyou();
    }else{
        printf("そこにはもうはもう入っています\n");
        printf("もう一度入力してください:");
        player1();
    }
}
void player2(void){
    scanf("%d,%d",&x,&y);
    if(hako[x][y]==0){
        hako[x][y]=2;
        print_hyou();
    }else{
        printf("そこにはもうはもう入っています\n");
        printf("もう一度入力してください:");
        player2();
    }
}
int hantei(void){
    if(hako[0][0]==hako[1][1]&&hako[1][1]==hako[2][2] || hako[2][0]==hako[1][1] && hako[1][1]==hako[0][2]){
        return hako[1][1];
    }else{
        for(int f=0;f<3;f++){
            if(hako[f][0]==hako[f][1] &&hako[f][1]==hako[f][2]){
                return hako[f][0];
            }else if(hako[0][f]==hako[1][f] && hako[1][f]==hako[2][f]){
                return hako[0][f];
            }
        }
        return 0;
    }
}
int main(void){
    for(int i=0;i<3;i++){
        for(int t=0;t<3;t++){
            hako[i][t]=0;
        }
    }
    char b[1000],c[1000],g[1000],h[10000];
    printf("プレーヤ1の名前を入力してください:");
    scanf("%s",g);
    printf("プレーヤ2の名前を入力してください:");
    scanf("%s",h);
    int i=rand() % 2;
    if(i==0){
        strcpy(b, g);
        strcpy(c,h);
    }else{
        strcpy(b,h);
        strcpy(c,g);
    }
    int e=0;
    for(int d=0;d<5;d++){
        printf("%sの番です:",b);
        player1();
        if(hantei()==1 || hantei()==2){
            if(hantei()==1){
                printf("%sの勝ちです",b);
                
            }else{
                printf("%sの勝ちです",c);
            }
            break;
        }
        e++;
        if(d<4){
            printf("%sの番です:",c);
            player2();
        }
        if(hantei()==1 || hantei()==2){
            if(hantei()==1){
                printf("%sの勝ちです",b);
                
            }else{
                printf("%sの勝ちです",c);
            }
            break;
        }
    }
    if(e==5){
        printf("引き分けです");
    }
}
