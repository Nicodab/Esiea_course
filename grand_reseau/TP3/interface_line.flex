%{
#include <stdio.h>
%}

%%

^interface[ ].*$    { printf("Ligne Interface : %s\n",yytext);}
(.|\n)           ;

%%
int main() {
    yylex();
    return 0;
}