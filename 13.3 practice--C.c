# include<stdio.h>
main()
{   //printf("***�ӷ�������***\n");
//	float sum,a,b;
//    printf("������aֵ:\n");scanf("%f",&a);
//	printf("������bֵ:\n");scanf("%f",&b);
//	sum=a+b;
//    printf("a+b = %.f",sum);
//
//
//return(0);
	printf("*****�žų˷���*****\n");
	int a;a = 1;
	while(a<=9)
	{	int b = 1;
		while(b<=a)
		{
		int c;
		c = b*a;
		printf("%d * %d = %d\t",a,b,c);
		b += 1;
		}
	a += 1;
	printf("\n");}
}
