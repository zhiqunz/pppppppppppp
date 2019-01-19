import os


class Base:
    def __init__(self, target, fun_get, fun_process, all_flg=False):
        print('*** new obj: {}, all flg: {} ***'.format(target, all_flg))
        self.lines_list = []
        self.files_name_list = []
        self.files_path_list = []

        # 参数检查
        if os.access(target, os.F_OK):
            if not os.access(target, os.R_OK):
                print('access is NOT allowed: {}'.format(target))
                raise BaseException('access is NOT allowed: {}'.format(target))
        else:
            print('Not exist: {}'.format(target))
            raise BaseException('Not exist: {}'.format(target))

        if not hasattr(fun_get, '__call__'):
            print('fun_get must be call: {}'.format(fun_get))
            raise BaseException('fun_get must be call: {}'.format(fun_get))

        if not hasattr(fun_process, '__call__'):
            print('fun_process must be call: {}'.format(fun_process))
            raise BaseException('fun_process must be call: '
                                '{}' .format(fun_process))

        self.target = target
        self.fun_get = fun_get
        self.fun_process = fun_process
        self.all_flg = all_flg

        # 如果target参数是文件夹，获取该文件夹内的所有文件；
        # 如果all_flg参数为true，获取该文件夹和子文件夹内所有文件
        # 如果target参数是文件，获取该文件的所有行
        if os.path.isdir(target):
            if all_flg:
                dir_result = os.walk(target)
                for entry in dir_result:
                    for name in entry[2]:
                        self.files_name_list.append(name)
                        self.files_path_list.append(os.path.join(entry[0],
                                                                 name))
            else:
                dir_result = os.scandir(target)
                for entry in dir_result:
                    self.files_name_list.append(entry.name)
                    self.files_path_list.append(entry.path)
        elif os.path.isfile(target):
            with open(target, 'r', encoding="utf-8") as f:
                for line in f:
                    self.lines_list.append(line)
                    # line = line.replace(os.linesep, '')
                    # if line:
                    #     self.lines_list.append(line)
        else:
            raise BaseException('target must be folder or file: '
                                '{}'.format(target))

    def get_target(self):
        pass

    def process_target(self, process_obj):
        pass

    def run(self):
        print('*** start run {} ***'.format(self.target))
        if self.fun_get and hasattr(self.fun_get, '__call__') and \
           self.fun_process and hasattr(self.fun_process, '__call__'):
            run_result = self.fun_get()
            self.fun_process(run_result)
        print('*** end   run {} ***'.format(self.target))


if __name__ == '__main__':
    cp = os.getcwd()
    test_file_path = os.path.join(cp, 'c0.py')
    test_folder_path = os.path.join(cp, 'templates')

    def func01(*args, **kwargs):
        pass

    def func02(*args, **kwargs):
        pass

    test_obj = Base(test_file_path, func01, func02)
    test_obj.run()
