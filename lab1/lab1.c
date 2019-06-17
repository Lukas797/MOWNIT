#include <stdio.h>
#include <gsl/gsl_sf_bessel.h>
#include <gsl/gsl_ieee_utils.h>

int main(int argc, char *argv[]){
float a = 1.0/3.0;
double b = 1.0/3.0;

for(int i = 0; i < 46; i++){

printf("float: "); gsl_ieee_printf_float(&a);
printf("\n");

a = a/10.0;

}

for(int i = 0; i < 250; i++){

printf("double: "); gsl_ieee_printf_double(&b);
printf("\n");

b = b/20.0;

}
}