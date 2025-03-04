#include <stdarg.h>
#include <unistd.h>

static int  ft_putchar(char c)
{
	return (write(1, &c, 1));
}

static int ft_putstr(char *str)
{
	int i = 0;
	while (str[i])
		ft_putchar(str[i++]);
	return i;
}

static int ft_putnbr(int n)
{
	int count = 0;
	if (n == -2147483648)
		return ft_putstr("-2147483648");
	if (n < 0)
	{
		count += ft_putchar('-');
		n = -n;
	}
	if (n >= 10)
		count += ft_putnbr(n / 10);
	count += ft_putchar(n % 10 + '0');
	return count;
}

int ft_printf(const char *format, ...)
{
	va_list args;
	int count = 0;

	va_start(args, format);
	while (*format)
	{
		if (*format == '%')
		{
			format++;
			if (*format == 'c')
				count += ft_putchar(va_arg(args, int));
			else if (*format == 's')
				count += ft_putstr(va_arg(args, char *));
			else if (*format == 'd' || *format == 'i')
				count += ft_putnbr(va_arg(args, int));
			else if (*format == '%')
				count += ft_putchar('%');
		}
		else
			count += ft_putchar(*format);
		format++;
	}
	va_end(args);
	return (count);
}
