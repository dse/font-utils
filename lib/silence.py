import os
stderr_fd = os.dup(2)
def silence(flag=True):
    global stderr_fd
    if flag:
        os.close(2)
    else:
        os.dup2(stderr_fd, 2)
