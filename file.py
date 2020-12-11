def file_write(fname, task):
    with open (fname, "w") as fp:
        for x in task:
            fp.write("%s/n" %x)

def file_read(fname):
    tasks = []
    with open(fname, "a+") as fp:
        t1 = fp.readlines()
        for x in t1:
            tasks.append(x.rstrip('\n'))
    return tasks
