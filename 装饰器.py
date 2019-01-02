

def fo(fun):
    print('fo start')
    def tmpfo():  # 子程序
        print("fun before")
        """
        fsdafafdafasdfa
        
        """
        fun()
        print("fun after 报销")
        """
        ''''''''
        """

    print("fo end")
    return tmpfo   # 返回子程序


@fo
def song():  # 子程序
    print("打车")

@fo
def wang():
    print('火车')


# print(type(fo))
#
# print('start')
#
# song = fo(song)

# song()

print("+++++++++++++++++++")
song()

print("+++++++++++++")
wang()