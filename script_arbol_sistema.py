
import os


os.chdir('c:/Users')
os.getcwd()

def main():
    for dirpath, dirnames, filenames in os.walk('C:/Users'):
        print('Ruta al directorio: ',dirpath)
        print('----------------------------------')
        print('Nombres de directorio: ',dirnames)
        print('----------------------------------')
        print('Nombres de archivo: ',filenames)
        print('----------------------------------')
        print()

if __name__=='__main__':
    main()

