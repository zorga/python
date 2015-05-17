import os

def main():
    print(os.getcwd())
    os.chdir('home/nico/Dropbox/Cours/SINF13BA')
    print(os.getcwd())

if __name__ == '__main__':
    main()
