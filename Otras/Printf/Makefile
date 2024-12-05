NAME = libftprintf.a

SRCS = \
	ft_printf.c ft_printf_basic.c ft_printf_base.c ft_printf_pointer.c\

OBJS = $(SRCS:.c=.o)

CC = gcc

CFLAGS = -c -Wall -Werror -Wextra

%.o: %.c
	$(CC) $(CFLAGS) $< -o $@

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) -rcs $(NAME) $(OBJS)

.PHONY: all clean re fclean bonus
re: fclean all

clean:
	rm -f $(OBJS) $(BONUSOBJS)

fclean: clean
	rm -rf $(NAME)
