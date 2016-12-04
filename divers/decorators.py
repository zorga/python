import sys
import inspect

def grantAccessIfOldEnough(func):
    def checker(name, age):
        if(age > 18):
            func(name, age)
        else:
            print('The user is not old enough !')

    return checker

@grantAccessIfOldEnough
def grantAccess(name, age):
    print('The ' + str(age) + ' years old user named : ' + name + ' is allowed to enter !')

def main():
    grantAccess('Goeffroy', 4)

if __name__ == '__main__':
    main()
