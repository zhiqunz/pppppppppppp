import os


# all_flg=False 获取文件夹内所有对应的文件名（带路径名，或者 单纯文件名）
# all_flg=True  获取文件夹内及子文件夹内的所有的文件名（带路径名，或者 单纯文件名）
def get_folder_only_files(folder_path='', all_flg=False):
    # files_name_list = []
    files_path_list = []

    check_taget(folder_path)
    if all_flg:
        dir_result = os.walk(folder_path)
        for entry in dir_result:
            for name in entry[2]:
                # files_name_list.append(name)
                files_path_list.append(os.path.join(entry[0], name))
    else:
        dir_result = os.scandir(folder_path)
        for entry in dir_result:
            if entry.is_file():
                # files_name_list.append(entry.name)
                files_path_list.append(entry.path)

    return files_path_list


# 检查文件或者文件夹是否存在，是否有权限
# 不存在或者没有权限，抛出异常
def check_taget(target):
    if os.access(target, os.F_OK):
        if not os.access(target, os.R_OK):
            print('access is NOT allowed: {}'.format(target))
            raise BaseException('access is NOT allowed: {}'.format(target))
    else:
        print('Not exist: {}'.format(target))
        raise BaseException('Not exist: {}'.format(target))

    return True
