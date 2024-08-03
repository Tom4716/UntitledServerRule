#
# Created by MC着火的冰块 on 2024/8/3
#
# All:在文末加上release时间 #16
#

import datetime
import os

# 获取当前时间
now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")
tag_name = now.strftime("v%Y.%m.%d.%H.%M.%S")
# 输出，供后续使用
print(f'::set-output name=time::{time}')
print(f'::set-output name=tag_name::{tag_name}')

# 遍历目录下文件
for name in os.listdir('.'):
    # 若为md，末尾添加时间
    if name.endswith('.md'):
        with open(name, 'a', encoding='utf-8') as f:
            f.write(f'\n\n---\n更新于 {time}')
