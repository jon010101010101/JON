#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int *ft_rrange(int start, int end)
{
	int i;
	long len;
	int	*matrix;

	i = 0;
	if (start > end)
		len = (long)start - (long)end + 1;
	if (start < end)
		len = (long)end - (long)start + 1;
	if (start == end)
		len = 1;
	matrix = (int *)malloc(sizeof(int) * (len));
	if (!matrix)
		return (NULL);
	while (i < len)
	{
		if (end >= start)
		{
			matrix[i] = end;
			i++;
			end--;
		}
		else 
	
		{
			matrix[i] = end;
			i++;
			end++;
		}
	}
	return(matrix);
}
/* int main(void)
{
    int *array;
    int start = -1;
    int end = 2;
    int i = 0;
    int len;

    array = ft_rrange(start, end);
    if (array)
    {
        if (start <= end)
            len = end - start + 1;
        else
            len = start - end + 1;

        while (i < len)
        {
            printf("%d ", array[i]);
            i++;
        }
        printf("\n");
        free(array);
    }
    return (0);
} */