#include<stdio.h>
#include<omp.h>
#include<stdlib.h>
int main()
{
int i;int j;int z;int x;
double a[500][500],b[500][500],c[500][500];
srand(time(NULL));
#pragma omp parallel for
for(i=0;i<500;i++)
for(j=0;j<500;j++)
{
a[i][j]=rand()%1000000/1000.0; //产生各个随机数 
b[i][j]=rand()%1000000/1000.0; //产生各个随机数
}

#pragma omp parallel for private(z)
for(i=0;i<500;i++)
for(j=0;j<500;j++)
{
for(z=0;z<500;z++)
{
c[i][j]+=a[i][z]*b[z][j];
}
}
}
