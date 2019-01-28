import unittest
import os
import sys
from src.tool import check_taget, get_folder_only_files


class MyTestCheckTarget(unittest.TestCase):
    def test_folder(self):
        tmp_path = os.getcwd()
        self.assertEqual(check_taget(tmp_path), True)

    def test_file(self):
        tmp_file_path = sys.argv[0]
        self.assertEqual(check_taget(tmp_file_path), True)

    def test_raise(self):
        tmp_path = os.path.join(os.getcwd(), '1')
        # self.assertRaises(BaseException, check_taget, tmp_path)
        self.assertRaisesRegex(BaseException, 'Not exist',
                               check_taget, tmp_path)


class MyTestGetFolder(unittest.TestCase):
    def test_get(self):
        tmp_path = os.path.join(os.getcwd(), 'tmp')
        result = {'files_name_list': ['empty.py', ],
                  'files_path_list': [os.path.join(tmp_path, 'empty.py'), ]
                  }
        self.assertEqual(get_folder_only_files(tmp_path), result)

    def test_get_all(self):
        tmp_path = os.path.join(os.getcwd(), 'tmp')
        result = {'files_name_list': ['empty.py',
                                      'empty01.py'
                                      ],
                  'files_path_list': [os.path.join(tmp_path, 'empty.py'),
                                      os.path.join(tmp_path,
                                                   'tmp01',
                                                   'empty01.py'),
                                      ]
                  }
        self.assertEqual(get_folder_only_files(tmp_path, True), result)


if __name__ == '__main__':
    unittest.main()
