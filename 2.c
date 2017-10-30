#include<stdio.h>
#include<math.h>
int main()
{
	float b=3.000,a=1.000,c=-5.600,e=0.000;
	if((b*b-4*a*c)<0){printf("此方程无解");}
	if((b*b-4*a*c)==0){e = -b/2*a;printf("只有一个解为：%.3lf\n",e);}
	if((b*b-4*a*c)>0){e=sqrt(b*b-4*a*c);printf("有两个解分别为：%.3lf 和 %.3lf\n",(-b+e)/2*a,(-b-e)/2*a);}
return 0;
}
