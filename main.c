#include <stdio.h>
#include <stdbool.h>
#include <string.h> 

void formatspezifisch() {
    int alter = 29;
    float preis = 19.99;
    double pi = 3.1415898747736;
    char zeichen = '@';
    char name[] = "Jan Werth";

    printf("%d\n",alter);
    printf("%f\n",preis);
    printf("%lf\n",pi);
    printf("%c\n",zeichen);
    printf("%s\n",name);
}
void variablen() {
    //Boolean 
    bool isOnline = true; 
    printf("%d\n",isOnline);


    //Char als String
    char name[] = "Jan Jan";
    printf("Hallo %s\n", name); 

    //Char mit nur einem Zeichen 
    char groesse = 'C'; 
    printf("Die Größe des Schlauches im Regal ist : %c\n ", groesse);
     
    //Double und Floar
    double pi = 3.14159265358979323846264338;
    float pif = 3.14159265358979323846264338;
    printf("Der Wert von Pi ist : %.30f\n",pif);
    printf("Der Wert von Pi ist : %.30lf\n",pi);

    //Integer und Float
    int age = 29;
    float durchschnitt = 2.5;
    float preis = 19.99; 
    printf("Dein Durchschnitt ist : %.1f \n", durchschnitt);
    printf("Der Preis ist : %.2f\n",preis);
    printf("Du bist %d Jahre alt\n ", age );
    printf("I Like Pizza!\n");
    printf("I Like Pizza!");

        bool online = 0;

    if(online){
        printf("Is Online");
    }
    else{
        printf("Is Offline");
    }
}
int main() {
    
    int alter;
    float durchschnitt;
    char buchstabe;
    char name[30]="";  


    printf("Bitte alter eingeben :");
    scanf("%d", &alter);
    printf("%d\n",alter);

    printf("Bitte durschnitt eingeben :");
    scanf("%f", &durchschnitt); 
    printf("%.2f\n",durchschnitt);

    printf("Bitte Buchstabe eingeben :");
    scanf(" %c", &buchstabe); 
    printf("%c\n",buchstabe); 

    getchar();
    printf("Bitte Name eingeben :");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1 ] = "\0";
    printf("%s\n",name); 

     return 0;
    
}