def mydeco(fn):
    def fx():
        print("++++++++++++++")
        fn()
        print('--------------')
    return fx

def myfunc():
    print("myfunc函数被调用")

myfunc=mydeco(myfunc)

myfunc()
myfunc()
myfunc()
