
import os
import sys
import click
from packaging import version


@click.command()
@click.argument('python_version')
def main(python_version):
    """Install Qt packages for python with specific version
    """

    python_version = version.parse(python_version)
    if sys.platform.startswith('linux'):
        os.system('apt-get install -y python-pyside')
    elif sys.platform.startswith('win32'):
        if python_version < version.parse('3.5'):
            os.system('%s -m pip install PySide' % sys.executable)
        else:
            os.system('%s -m pip install PyQt5' % sys.executable)


if __name__ == '__main__':
    main()