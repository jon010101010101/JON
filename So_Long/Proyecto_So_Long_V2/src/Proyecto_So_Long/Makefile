NAME = so_long
CC = cc
CFLAGS = -Wall -Wextra -Werror -g3 -I./include -I./minilibx-linux -I./libft
LDFLAGS = -L./minilibx-linux -L./libft -lft -lmlx -lX11 -lXext -lm

SRCS = src/main.c src/load_map.c src/load_images.c src/render_game.c \
       src/key_press.c src/player.c src/close_window.c src/error_handling.c \
       src/utils.c src/check_win_condition.c

OBJS = $(SRCS:.c=.o)

LIBFT_DIR = libft
LIBFT = $(LIBFT_DIR)/libft.a
MLX_DIR = minilibx-linux
MLX = $(MLX_DIR)/libmlx.a

all: $(LIBFT) $(MLX) $(NAME)

$(LIBFT):
	$(MAKE) -C $(LIBFT_DIR)

$(MLX):
	$(MAKE) -C $(MLX_DIR)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -L$(LIBFT_DIR) -lft $(MLX) $(LDFLAGS) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(MAKE) -C $(LIBFT_DIR) clean
	$(MAKE) -C $(MLX_DIR) clean
	rm -f $(OBJS)

fclean: clean
	$(MAKE) -C $(LIBFT_DIR) fclean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
