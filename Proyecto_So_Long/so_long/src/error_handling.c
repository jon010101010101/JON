#include "../include/so_long.h"
#include "../libft/libft.h"

void error_exit(const char *message)
{
    fprintf(stderr, "Error: %s\n", message);
    exit(1);
}

void warning(const char *message)
{
    fprintf(stderr, "Warning: %s\n", message);
}

void debug_log(const char *message)
{
    #ifdef DEBUG
    printf("Debug: %s\n", message);
    #else
    (void)message; // Evita el warning de parámetro no utilizado
    #endif
}
