NAME = so_long
CC = cc
CFLAGS = -Wall -Wextra -Werror -g3 -I./include -I../../minilibx-linux -I./libft
MLX_FLAGS = -L../../minilibx-linux -lmlx -lX11 -lXext -lm

SRCS = src/main.c src/load_map.c src/load_images.c src/render_game.c \
       src/key_press.c src/player.c src/close_window.c src/error_handling.c \
       src/utils.c src/check_win_condition.c src/validate_map.c

OBJS = $(SRCS:.c=.o)

LIBFT_DIR = libft
LIBFT = $(LIBFT_DIR)/libft.a

all: $(LIBFT) $(NAME)

$(LIBFT):
	$(MAKE) -C $(LIBFT_DIR)

$(NAME): $(OBJS) $(LIBFT)
	$(CC) $(CFLAGS) $(OBJS) $(LIBFT) $(MLX_FLAGS) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(MAKE) -C $(LIBFT_DIR) clean
	rm -f $(OBJS)

fclean: clean
	$(MAKE) -C $(LIBFT_DIR) fclean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
