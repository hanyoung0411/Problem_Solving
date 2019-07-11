#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

const int max_line = 100;
int eval(char * string){
	int cnt = 0, flag = 0;
	int i,j,len;
	int begin;
	int expr1, expr2;
	int result;
	char op = '!';
	char * eval_string ; 
	len = strlen(string);

	puts(string);

	for(i=0;i<len;i++){
		if(string[i] == '('){
			if(cnt == 0)begin = i+1;
			cnt ++ ;
		}
		else if(string[i] == ')'){
			cnt -- ;
			if(cnt == 0){
				eval_string = (char*)malloc(sizeof(char) * i-begin);
				for(j=begin;j<i;j++)eval_string[j-begin] = string[j];
				
				result = eval(eval_string);
				
				printf("strcat : ");
				char str[100];
				//puts(string);
	            for(j=i+1;j<len;j++)str[j-(i+1)]=string[j];
				str[j-(i+1)] = 0x0;

				string[begin-1] = (char)(result +'0');
                string[begin] = 0x0;
				//puts(str);
				strcat(string,str);
				puts(string);
				return eval(string);
			}
		}
		else if(string[i] == '+' || string[i] == '-' || string[i] == '*'){
			switch(string[i]){
				case '+' :
					op = '+';
					break;
				case '-' :
					op = '-';
					break;
				case '*' :
					op = '*';
					break;
			}
		}
		else if(string[i] == ' ')continue;
		else if(isdigit(string[i]) && cnt == 0){ // number
			if(op != '!'){
				expr2 = string[i] - '0';
				flag = 1;
				switch (op){
					case '+' :
						return expr1 + expr2;
					case '-' :
						return expr1 - expr2;
					case '*' :
						return expr1 * expr2;
				}
			}
			else {
				expr1 = string[i] - '0';
			}
		}
	}
	if(flag == 0)return expr1;
}

int main(){
	char s[max_line];
	fgets(s,max_line,stdin);
	printf("result : %d\n",eval(s));
	return 0;
}
