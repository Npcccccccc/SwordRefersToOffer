#include <stdio.h>
#include<stdlib.h>
int main()
{
	int array[100];
	int array1[100];
	int i = 0, j, k, x, y = 0, z, n;
	printf("请输入数组元素个数：");
	scanf("%d", &n);
	printf("请输入各元素值：");
	while (i < n) {
		scanf("%d", &array[i]);
		i++;
	}
	printf("该数组中重复的元素为：");
	for (j = 0; j < n; j++) {
		x = array[j];
		z = 0;
		for (k = 0; k < y + 1; k++) {
			if (x == array1[k])
				z++;
		}
		if (z == 0) {
			array1[y] = x;
			y++;
		}
		else {
			printf("%d ", x);
		}
	}


}
