#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    int a[3],tmp=0;
    scanf("%d%d%d",&a[0],&a[1],&a[2]);

    bool state=true;
    while(state)
    {
        state=false;
        for(int i=0;i<2;i++)
        {
            if(a[i]>a[i+1])
            {
                tmp=a[i];
                a[i]=a[i+1];
                a[i+1]=tmp;
                tmp=0;
                state=true;
            }

        }
    }
    printf("%d ",a[0]);
    printf("%d ",a[1]);
    printf("%d",a[2]);


    return 0;
}
