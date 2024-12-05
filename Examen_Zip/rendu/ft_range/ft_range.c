#include <unistd.h>
#include <stdlib.h>

int *ft_range(int start, int end)
{
    int len;
    int *matrix;
    int i = 0;

    if(start > end)
        len = start - end +1;
    else
        len = end - start +1;

    matrix=(int *)malloc(sizeof(int) * len);
    if(!matrix)
        return(NULL);

    while(i < len)
    {
        matrix[i]=start;
        if(start > end)
            start--;
        else
            start++;
        i++;
    }
    return(matrix);
}
/* #include <stdio.h>

int main(void)
{
    int len;
    int *result;
    int i = 0;
    int start = -1;
    int end = 2;

    if(start > end)
        len = start - end +1;
    else
        len = end - start +1;

    result = ft_range(start, end);

    while(i < len)
    {
        printf("%d ", result[i]);
        i++;
    }

    free(result);

    return(0);
} */