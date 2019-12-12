version = 1.0
import pathlib
import shutil
import os 
import gzip
import time
sline = ('\n' + '--------------------------------' + '\n')
print(sline)
log_folder = input('請輸入 log 路徑: ')
files = []
key = []
logt = []
count = 0
start_time = time.time()
print(sline)
print('讀取中，請稍等')
print(sline)

data = {}
for file in [f for f in pathlib.Path(log_folder).glob('*.log.gz')]:
    f = gzip.open(file, 'rt')
    file_content = f.readlines()
    data[file.stem] = file_content

end_time = time.time()
print(sline)
print('檔案讀取結束，總共有', len(data), '筆資料，搜尋時間', round((end_time - start_time), 2), '秒')
print(sline)

while True:
    search = input('關鍵字搜尋，輸入 q 結束: ')
    print (sline)

    if search == 'q':
        break

    result = []
    for file in data:
        for line in data[file]:
            if search in line:
                result.append(file + line) 

    for i in result:
        print(i + "\n")A

    print('共有',len(result),'筆資料提到:', search)
    print(sline)
print('感謝您使用由 Nekoret 所製作的搜尋功能')
print(sline)
