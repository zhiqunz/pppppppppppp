import os

class Base:
    def __init__(self, target='', fun_get='', fun_process='',all_flg=False):
        print('**new obj :{}, all flg:{}**'.format(target, all_flg))
        self.lines_list = []
        self.files_name_list = []
        self.files_path_list = []

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

    def process_target(self,func=''):
        pass

    def run(self):
        print('**start run {}**'.format(self.target))
        result = self.fun_get()
        self.fun_process(result)
        print('**end run {}**'.format(self.target))


if __name__ == '__main__':
    test_obj = Base('dd')