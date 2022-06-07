
import os


os.chdir('/home/michelle/')
os.getcwd()

def main():
    for dirpath, dirnames, filenames in os.walk('/home/michelle/'):
        print('Ruta al directorio: ',dirpath)
        print('----------------------------------')
        print('Nombres de directorio: ',dirnames)
        print('----------------------------------')
        print('Nombres de archivo: ',filenames)
        print('----------------------------------')
        print()

if __name__=='__main__':
    main()

