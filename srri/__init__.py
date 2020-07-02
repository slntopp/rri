import os
import subprocess


def collect_and_install(supress_output: bool = False) -> bool:
    """Recursively collects requirements.txt (with depth of 1 dir) and installs all of them

    Args:
        supress_output (bool, optional): Produces no output if True. Defaults to False.

    Returns:
        bool: Returns True if requirements were found
    """
    if not supress_output:
        print('Collecting requirements...')

    out = subprocess.run(
        ["find", ".", "-name", "requirements.txt"], stdout=subprocess.PIPE)

    files = list(filter(lambda x: x, out.stdout.decode().split('\n')))
    if not supress_output:
        print('Found:', end=" ")

    try:
        if not files:
            if not supress_output:
                print('Nothing, exiting...')
            return False
        else:
            print()
        for f in files:
            print('>\t', f)
    except:
        pass

    requirements = ' '.join(
        map(lambda file: "-r {}".format(file), files)
    )

    command = "./bin/pip install %s" % requirements

    if not supress_output:
        print('Running: %s' % command)

    subprocess.run(command.split(' '))
    print("Done installing.")
    return True
