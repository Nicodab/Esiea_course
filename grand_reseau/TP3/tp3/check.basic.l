%{
	#include <stdio.h>
	char filename[100];
%}

%%

^interface[ ].*$	{
	printf("%s:%s\n",filename,yytext);
}

(.|\n)	; 

%%

int main(int argc, char **argv ) {

    strncpy(filename,argv[1],strlen(argv[1]));
    filename[strlen(argv[1])] = '\0';

    yyin = fopen(filename, "r" );
    yylex();
    fclose(yyin);
}
