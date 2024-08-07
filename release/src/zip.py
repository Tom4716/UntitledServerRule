import sys
import zipfile
import os

# 接收版本号
version = sys.argv[1]

with zipfile.ZipFile(f'UntitledServerRule-{version}.zip', 'w') as zip_file:
    # 压缩*.md和*.docx
    for name in os.listdir('.'):
        if name.endswith('.md') or name.endswith('.docx'):
            zip_file.write(name)
