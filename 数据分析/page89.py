import numpy as np
from matplotlib import  pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t_us = np.loadtxt(us_file_path,delimiter=",",dtype="int")

#取评论的数据
t_us_comments = t_us[:,-1]

#选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments<=5000]

print(t_us_comments.max(),t_us_comments.min())

d = 50

bin_nums = (t_us_comments.max()-t_us_comments.min())//d

#绘图
plt.figure(figsize=(20,8),dpi=80)

plt.hist(t_us_comments,bin_nums)


plt.show()