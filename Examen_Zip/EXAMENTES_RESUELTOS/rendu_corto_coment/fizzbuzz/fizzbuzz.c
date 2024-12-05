/*
Assignment name  : fizzbuzz
Expected files   : fizzbuzz.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that prints the numbers from 1 to 100, each separated by a
newline.
If the number is a multiple of 3, it prints 'fizz' instead.
If the number is a multiple of 5, it prints 'buzz' instead.
If the number is both a multiple of 3 and a multiple of 5, it prints 'fizzbuzz' instead.
--------------------------------------------------------------------------------
Escribe un programa que imprima los números del 1 al 100, cada uno separado por un
nueva línea.
Si el número es múltiplo de 3, en su lugar imprime 'fizz'.
Si el número es múltiplo de 5, en su lugar imprime "buzz".
Si el número es múltiplo de 3 y múltiplo de 5, en su lugar imprime 'fizzbuzz'.

Example:
$>./fizzbuzz
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
[...]
97
98
fizz
buzz
$> 
*/

#include <unistd.h>

void print_nbr(int i)
{
    char    *digits;

    digits = "0123456789";
    if(i > 9)
        print_nbr(i / 10);
    write(1, &digits[i % 10], 1);
}

int main(void)
{
    int     i = 1;

    while (i < 101)
    {
        if ((i % 15) == 0)
            write(1, "fizzbuzz", 8);
        else if((i % 5) == 0)
            write(1, "fizz", 4);
        else if((i % 3) == 0)
            write(1, "buzz", 4);
        else
            print_nbr(i);
        write(1, "\n", 1);
        i++;
    }
    return (0);
}