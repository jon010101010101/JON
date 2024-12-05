/*
Assignment name  : union
Expected files   : union.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes two strings and displays, without doubles, the
characters that appear in either one of the strings.
The display will be in the order characters appear in the command line, and
will be followed by a \n.
If the number of arguments is not 2, the program displays \n.
--------------------------------------------------------------------------------
Escribe un programa que tome dos cadenas y muestre, sin dobles, el
caracteres que aparecen en cualquiera de las cadenas.
La pantalla se mostrará en el orden en que aparecen los caracteres en la línea 
de comando y irá seguido de un \n.
Si el número de argumentos no es 2, el programa muestra \n.

Example:
$>./union zpadinton "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
zpadintoqefwjy$
$>./union ddf6vewg64f gtwthgdwthdwfteewhrtag6h4ffdhsd | cat -e
df6vewg4thras$
$>./union "rien" "cette phrase ne cache rien" | cat -e
rienct phas$
$>./union | cat -e
$
$>
$>./union "rien" | cat -e
$
$>
*/

/* ANA OK*/

#include <unistd.h>

int not_seen_before(char *str, char c, int max_pos)
{
    int i = 0;
    while (i < max_pos)
    {
        if (str[i] == c)
            return (0);
        i++;
    }
    return (1);
}

void ft_union(char *s1, char *s2)
{
    int i = 0;
    int j = 0;

    while (s1[i])
    {
        if (not_seen_before(s1, s1[i], i))
            write(1, &s1[i], 1);
        i++;
    }
    while (s2[j])
    {
        if (not_seen_before(s1, s2[j], i) && not_seen_before(s2, s2[j], j))
            write(1, &s2[j], 1);
        j++;
    }
}

int main(int argc, char **argv)
{
    if (argc == 3)
        ft_union(argv[1], argv[2]);
    write(1, "\n", 1);
    return (0);
}

/* #include <unistd.h>  // Incluye la biblioteca que proporciona la función 'write'.

// Función para verificar si el carácter 'c' no ha sido visto antes en la subcadena de 'str' hasta 'max_pos'.
int not_seen_before(char *str, char c, int max_pos)
{
    int i = 0;  // Inicializa el índice 'i' para recorrer la cadena hasta 'max_pos'.

    // Recorre la cadena hasta 'max_pos'.
    while (i < max_pos)
    {
        // Si el carácter 'c' se encuentra en la subcadena, devuelve 0 (indica que se ha visto antes).
        if (str[i] == c)
            return (0);
        i++;  // Incrementa el índice para continuar con la siguiente posición.
    }

    // Si el carácter 'c' no se encuentra en la subcadena, devuelve 1 (indica que no se ha visto antes).
    return (1);
}

// Función para imprimir la unión de los caracteres únicos de las cadenas 's1' y 's2'.
void ft_union(char *s1, char *s2)
{
    int i = 0;  // Índice para recorrer la cadena 's1'.
    int j = 0;  // Índice para recorrer la cadena 's2'.

    // Recorre la cadena 's1'.
    while (s1[i])
    {
        // Si el carácter en 's1[i]' no ha sido visto antes en la subcadena de 's1' hasta la posición 'i',
        // se escribe en la salida estándar.
        if (not_seen_before(s1, s1[i], i))
            write(1, &s1[i], 1);
        i++;  // Incrementa el índice para continuar con el siguiente carácter en 's1'.
    }

    // Recorre la cadena 's2'.
    while (s2[j])
    {
        // Si el carácter en 's2[j]' no ha sido visto antes en 's1' (hasta la posición 'i') y tampoco en la subcadena de 's2' hasta la posición 'j',
        // se escribe en la salida estándar.
        if (not_seen_before(s1, s2[j], i) && not_seen_before(s2, s2[j], j))
            write(1, &s2[j], 1);
        j++;  // Incrementa el índice para continuar con el siguiente carácter en 's2'.
    }
}

// Función principal del programa.
int main(int argc, char **argv)
{
    // Verifica si el número de argumentos es exactamente 3 (incluyendo el nombre del programa).
    if (argc == 3)
        ft_union(argv[1], argv[2]);  // Llama a la función 'ft_union' con los dos argumentos de la línea de comandos.

    // Imprime un salto de línea en la salida estándar para asegurar un formato limpio en la salida.
    write(1, "\n", 1);

    return (0);  // Devuelve 0 para indicar que el programa terminó correctamente.
} */
