import sys
  
def main():
    print("=== DECORATORS ====")

    def compose_greet_func(name):
        def get_message():
            return 'Hello there ! ' + name

        return get_message

    greet = compose_greet_func("snuff snuff")
    print greet()

    ## Functions definitions
    def eat(food):
        cake, pie = 'miam miam ', 'om nom nom'
        print('Let\'s eat ! : ' + cake + pie)
        print locals()

    def foo(x, y = 42):
        """foo(x, y = 42) : y is an optional parameter
        """
        return x - y

    ## Functions calls
    eat('french fries')
    print(foo(50, 20)) # print 30
    print(foo(50))     # print 8

if __name__ == '__main__':
    main()
