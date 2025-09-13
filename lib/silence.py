import os
stderr_fd = os.dup(2)
disabled = False
def silence(flag=True):
    global disabled
    global stderr_fd
    if disabled:
        return
    elif flag is None:
        disabled = True
        os.dup2(stderr_fd, 2)
    elif flag:
        os.close(2)
    else:
        os.dup2(stderr_fd, 2)
