import os
import logging, time


# 当前文件路径
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)

# -------------------------------------------------------------------------------
# 类名称：Log
# 类的目的：写日志
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：谢殿俊
# 创建时间：2019/05/18
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------
class Log():
	def __init__(self):
		#log_path是存放日志的路径
		log_path = os.path.join(os.path.dirname(cur_path),"log")
		print(log_path)
		#如果不存在log文件夹，那就自动创建一个
		if not os.path.exists(log_path):
			os.mkdir(log_path)
			
		# 文件的命名
		self.logname = os.path.join(log_path,"{}".format(time.strftime("%Y_%m_%d")))
		self.logger = logging.getLogger()
		
		

