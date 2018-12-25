
#include <stdio.h>
#include <math.h>

int main()
{
        float a, x;
        int b;  
        scanf("%f", &a);
        scanf("%f", &x);
        scanf("%d", &b);
        switch(b)
        {
                case(1):
                printf("G = %f\n", (4*(-4*pow(a,2)+a*x+5*pow(x,2)))/(-20*pow(a,2)+28*a*x+3*pow(x,2)));
                break;
                case(2):
                printf("F = %f\n", (atan(24*pow(a,2)-25*a*x+6*pow(x,2))));
                break;
                case(3):
                printf("Y = %f \n", (log(2*pow(a,2)-7*a*x+6*pow(x,2)+1)));
                break;
        }
        return 0;
}



