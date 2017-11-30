#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
int main()
{
int i;int j,tid;
double a[500000],b[500000];
srand(time(NULL));
#pragma omp parallel for
for(i=0;i<500000;i++)
a[i]=rand()%1000000/1000.0; //产生各个随机数 
#pragma omp parallel for
for(j=0;j<500000;j++)
b[j]=rand()%1000000/1000.0; //产生各个随机数 　
#pragma omp parallel for
for(i=0;i<500000;i++)
{
tid = omp_get_thread_num();
printf("mul=%f tid = %d\n",a[i]*b[i],tid);
}}
