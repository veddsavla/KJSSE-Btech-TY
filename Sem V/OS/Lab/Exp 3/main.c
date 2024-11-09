# include <stdio.h>
# include <unistd.h>
# include <fcntl.h>

# define BUFFER_SIZE 1024

int main() {
    int fd_source, fd_dest;
    char *source_path = "readonly.txt";
    char *dest_path = "writeonly.txt";
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read, bytes_written;

    fd_source = open(source_path, O_RDONLY);
    if (fd_source == -1) {
        perror("Cannot open source file");
        return 1;
    }

    fd_dest = open(dest_path, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd_dest == -1) {
        perror("Cannot open destination file");
        close(fd_source);
        return 1;
    }

    while ((bytes_read = read(fd_source, buffer, sizeof(buffer))) > 0) {
        bytes_written = write(fd_dest, buffer, bytes_read);
        if (bytes_written != bytes_read) {
            perror("Cannot copy");
            close(fd_dest);
            close(fd_source);
            return 1;
        }
    }

    if (bytes_read == -1) {
        perror("Cannot read source file");
        close(fd_dest);
        close(fd_source);
        return 1;
    }

    printf("File copied successfully\n");
    close(fd_dest);
    close(fd_source);
    return 0;
}
