NAME = so_long

CFLAGS = -Wall -Wextra -Werror -g3

MLX_PATH = minilibx-linux
MLX_FLAGS = -L./minilibx-linux -lmlx -lXext -lX11 -lm -lz

LIBFT_PATH = libft
LIBFT_A = $(LIBFT_PATH)/libft.a

SRCS_PATH = src
SRCS_FILES = main.c \
              load_map.c \
              map_reader.c \
              map_processor.c \
              map_validation.c \
              map_utils.c \
              init_game.c \
              load_images.c \
              key_press.c \
              close_window.c \
              render_game.c \
              utils.c \
              error_handling.c \
              player.c \
              check_win_condition.c \
              cleanup.c

SRCS = $(addprefix $(SRCS_PATH)/, $(SRCS_FILES))

OBJS_PATH = obj
OBJS_FILES = $(SRCS_FILES:.c=.o)
OBJS = $(addprefix $(OBJS_PATH)/, $(OBJS_FILES))

# Include directories
INC = -I./include -I./$(MLX_PATH) -I./$(LIBFT_PATH) -I.

# Colors for messages
GREEN	= \033[0;32m
RESET	= \033[0m

# make all
all: $(NAME)

# Compile object files from source files
$(OBJS_PATH)/%.o: $(SRCS_PATH)/%.c
	@mkdir -p $(OBJS_PATH)
	@echo "$(GREEN)Compiling: $< $(RESET)"
	@cc $(CFLAGS) $(INC) -c $< -o $@

# Create the library
$(LIBFT_A):
	@echo "$(GREEN)Creating libft.a$(RESET)"
	@make -C $(LIBFT_PATH)
# Link object files to create the executable
$(NAME): $(OBJS) $(LIBFT_A)
	@echo "$(GREEN)Linking objects$(RESET)"
	@cc $(CFLAGS) $(INC) $(OBJS) $(MLX_FLAGS) $(LIBFT_A) -o $(NAME)
# make clean
clean:
	@echo "$(GREEN)Cleaning objects$(RESET)"
	@make clean -C $(LIBFT_PATH)
	@rm -rf $(OBJS_PATH)

# make fclean
fclean: clean
	@echo "$(GREEN)Cleaning executable and library$(RESET)"
	@make fclean -C $(LIBFT_PATH)
	@rm -f $(NAME)

# make re
re: fclean all

.PHONY: all clean fclean re
