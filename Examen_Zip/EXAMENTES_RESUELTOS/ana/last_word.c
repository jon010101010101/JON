// Write a program that takes a string and displays its last word followed by a \n.
// A word is a section of string delimited by spaces/tabs or by the start/end of
// the string.
// If the number of parameters is not 1, or there are no words, display a newline.
// Example:
// $> ./last_word "FOR PONY" | cat -e
// PONY$
// $> ./last_word "this        ...       is sparta, then again, maybe    not" | cat -e
// not$
// $> ./last_word "   " | cat -e
// $
// $> ./last_word "a" "b" | cat -e
// $
// $> ./last_word "  lorem,ipsum  " | cat -e
// lorem,ipsum$
// $>

#include <unistd.h>

int ft_is_space(char c)
{
	return(c == ' ' || c == '\t');
}

int main(int argc, char **argv)
{
	int i;
	int start;

	i = 0;
	start = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			if (argv[1][i + 1] >= 33 && argv[1][i + 1] <= 126 && ft_is_space(argv[1][i]))
				start = i + 1;
			i++;
		}
		while (argv[1][start] >= 33 && argv[1][start] <= 126)
		{
			write(1, &argv[1][start], 1);
			start++;
		}
	}
	write(1, "\n", 1);
	return (0);

}