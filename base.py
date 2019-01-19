import os


class Base:
    def __init__(self, target, fun_get, fun_process, all_flg=False):
        print('** new obj: {}, all flg: {} **'.format(target, all_flg))
        self.lines_list = []
        self.files_name_list = []
        self.files_path_list = []

        # 参数检查
        if os.access(target, os.F_OK):
            if not os.access(target, os.R_OK):
                print('access is NOT allowed: {}'.format(target))
                raise 'access is NOT allowed: {}'.format(target)
        else:
            print('Not exist: {}'.format(target))
            raise 'Not exist: {}'.format(target)

        if not hasattr(fun_get, '__call__'):
            print('fun_get must be call: {}'.format(fun_get))

        if not hasattr(fun_process, '__call__'):
            print('fun_process must be call: {}'.format(fun_process))

        self.target = target
        self.fun_get = fun_get
        self.fun_process = fun_process
        self.all_flg = all_flg

        # 如果处理参数是文件夹，获取该文件夹内的所有文件；
        # 如果参数all_flg为true，递归获取该文件夹和子文件夹内所有文件

        # 如果处理参数是文件，获取该文件的所有行

    def get_folder(self, folder_path=''):
        pass

    def get_file(self, file_path=''):
        pass

    def get_target(self, func=''):
        pass

    def process_target(self, func=''):
        pass

    def run(self):
        print('**start run {}**'.format(self.target))
        if self.fun_get and \
                hasattr(self.fun_get, '__call__') and \
                self.fun_process and \
                hasattr(self.fun_process, '__call__'):
            run_result = self.fun_get()
            self.fun_process(run_result)
        print('**end run {}**'.format(self.target))


if __name__ == '__main__':
    cp = os.getcwd()
    test_file_path = os.path.join(cp, 'c0.py')
    test_folder_path = os.path.join(cp, 'templates')

    def func01():
        pass

    def func02():
        pass

    test_obj = Base(test_folder_path, func01, func02)
