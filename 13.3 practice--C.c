# include<stdio.h>
main()
{   //printf("***加法运算器***\n");
//	float sum,a,b;
//    printf("请输入a值:\n");scanf("%f",&a);
//	printf("请输入b值:\n");scanf("%f",&b);
//	sum=a+b;
//    printf("a+b = %.f",sum);
//
//
//return(0);
	printf("*****九九乘法表*****\n");
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
