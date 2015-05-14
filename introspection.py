import sys
  
def main():

    def compose_greet_func(name):
        def get_message():
            return 'Hello there ! ' + name

        return get_message

    ## Functions definitions
    def eat(food):
        cake, pie = 'miam miam ', 'om nom nom'
        print('Let\'s eat ! : ' + cake + pie)
        print locals()

    def foo(x, y = 42):
        """foo(x, y = 42) : y is an optional parameter
        """
        return x - y

    ## Function closures
    def bigFunction(x, attribute = 'little'):
        def littleFunction():
            if (attribute):
                print('This is a ' + attribute + ' number : ' + str(x))
            else:
                print('This is a big number : ' + str(x))
        return littleFunction

    ## Decorators !
    def outer(some_func):
        def inner():
            ret = some_func()
            return ret + 1
        return inner

    def lol():
        return 1

    ## More useful decorator !

    ## Functions calls
    print('[' + 5*'=' + "RANDOM SHIT" + 5*'=' + ']')
    greet = compose_greet_func("snuff snuff")
    print greet()
    print('[' + 5*'=' + "FUNCTION PROPERTIES" + 5*'=' + ']')
    eat('french fries')
    print(foo(50, 20)) # print 30
    print(foo(50))     # print 8
    print(foo(y = 5, x = 2))
    theFunctionResult = bigFunction(5000) #Same as theFunctionResult = littleFunction
    theFunctionResultII = bigFunction(300, 'middle')
    theFunctionResult()
    theFunctionResultII()
    print('[' + 5*'=' + "DECORATORS" + 5*'=' + ']')
    print('non-decorated : ' + str(lol()))
    lol = outer(lol) # foo = inner -> which returns 2 because foo returns 1
    # Now calling the decorated version of lol
    print('decorated : ' + str(lol()))

if __name__ == '__main__':
    main()
