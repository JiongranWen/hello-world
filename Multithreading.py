import threading


i = 10000000
#具体做啥事,写在函数中
def run(number):
    print(threading.currentThread().getName() + '\n')
    print(number)

if __name__ == '__main__':
    while True:
        i = i - 1
        #注意这,开始咯,指明具体的方法和方法需要的参数
        my_thread = threading.Thread(target=run, args=(i,))
        #一定不要忘记
        my_thread.start()
