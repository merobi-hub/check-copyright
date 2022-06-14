def check_files():

    import os
    import sys

    year = str(sys.argv[1])
    file_type = str(sys.argv[2])
    author = str(sys.argv[3])
    print(f'Checking all .{file_type} files...')

    paths = []
    for (root, dirs, files) in os.walk('.', topdown=True):
        for f in files:
            if f == 'check_files.py':
                continue
            elif len(file_type) == 4:
                if f[-4:] == file_type:
                    path = os.path.join(root, f)
                    with open(path) as t:
                        if f'Copyright {year} contributors to the {author} project' in t.read():
                            continue
                        else:    
                            paths.append(path)
            elif len(file_type) == 3:
                if f[-3:] == file_type:
                    path = os.path.join(root, f)
                    with open(path) as t:
                        if f'Copyright {year} contributors to the {author} project' in t.read():
                            continue
                        else:    
                            paths.append(path)    
            elif len(file_type) == 2:
                if f[-2:] == file_type:
                    path = os.path.join(root, f)
                    with open(path) as t:
                        if f'Copyright {year} contributors to the {author} project' in t.read():
                            continue
                        else:
                            paths.append(path)            

    num_files = len(paths)
    print(f'{num_files} files without copyright found.')
    print(paths)

check_files()


