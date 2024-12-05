#include <unistd.h>

int ft_not_seen_before(char *str, char c, int max_pos)
{
	int	i;

	i = 0;
	while (str[i] && (i < max_pos || max_pos == -1))
	{
		if (str[i] == c)
			return (0);
		else 
			i++;	
	}
	return (1);
}

int main (int argc, char **argv)
{
	int i;

	i = 0;
	if (argc == 3)
	{
		while (argv[1][i])
		{
			if (ft_not_seen_before(argv[1], argv[1][i], i) && !ft_not_seen_before(argv[2], argv[1][i], -1))
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
