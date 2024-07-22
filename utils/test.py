# 读取r_permute_20.npy文件并输出其内容
import numpy as np
random_seed = 42
np.random.seed(random_seed)
# 生成一个随机排列
r_permute = np.random.permutation(78)
# 保存到文件
np.save('/home/liyue/code/AttnSleep/utils/r_permute_153.npy', r_permute)
data = np.load('/home/liyue/code/AttnSleep/utils/r_permute_78.npy')
print(len(data))





