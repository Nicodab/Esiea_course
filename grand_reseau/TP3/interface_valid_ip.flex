%{
#include <stdio.h>
char interface[100];
%}

%x INTERFACE

%%

^interface[ ].*$    { 
    snprintf(interface,100,"%s",yytext);
    BEGIN INTERFACE;
    }

<INTERFACE>^[ ]ip[ ]address[ ].*$  { printf("%s : %s\n",interface,yytext);}
<INTERFACE>(.|\n)   ;
<INTERFACE>^!$  {BEGIN INITIAL;}
(.|\n)           ;

%%
int main() {
    yylex();
    return 0;
}