#include <unistd.h>

void print_nbr(int i)
{
    char    *digits;

    digits = "0123456789";
    if (i > 9)
        print_nbr(i / 10);
    write(1, &digits[i % 10], 1);
}

int main (void)
{
    int     i = 1;

    while (i < 101)
    {
        if ((i % 28) == 0)
            write(1, "buzzfizz", 8);
        else if ((i % 7) == 0)
            write(1, "buzz", 4);
        else if ((i % 4) == 0)
            write(1, "fizz", 4);
        else
            print_nbr(i);
        write(1, "\n", 1);
        i++;
    }
    return (0);
}

/*Escribe un programa que imprima los números del 1 al 100, cada uno separado por un
nueva línea.
Si el número es múltiplo de 4, en su lugar imprime 'buzz'.
Si el número es múltiplo de 7, en su lugar imprime "fizz".
Si el número es múltiplo de 4 y múltiplo de 7, en su lugar imprime 'buzzfizz'.

Example:
$>./fizzbuzz
1
2
3
buzz
5
6
fizz
buzz
9
10
11
buzz
13
fizz
15
buzz
17
18
19
buzz
fizz
22
23
buzz
25
26
27
fizzbuzz
29
30
[...]
97
fizz
99
buzz
$> */
