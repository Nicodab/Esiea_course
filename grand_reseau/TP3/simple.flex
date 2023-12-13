%{
#include <stdio.h>
%}

DIGIT [0-9]

%%
{DIGIT}+    { printf("Entier trouvé : %s\n", yytext); }
.           ;

%%
int main() {
    yylex();
    return 0;
}