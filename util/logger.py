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
		self.logger.setLevel(logging.DEBUG)
		# 日志输出格式
		self.formatter = logging.Formatter('[%(asctime)s - %(funcName)s line: %(lineno)3d] - %(levelname)s: %(message)s')
		
	def __console(self, level, message):
		# 创建一个FileHandler，用于写到本地
		# fh = logging.FileHandler(self.logname, 'a')  # 追加模式  这个是python2的
		fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
		fh.setLevel(logging.DEBUG)
		fh.setFormatter(self.formatter)
		self.logger.addHandler(fh)
		
		# 创建一个StreamHandler,用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		ch.setFormatter(self.formatter)
		self.logger.addHandler(ch)
		
		if level == 'info':
			self.logger.info(message)
		elif level == 'debug':
			self.logger.debug(message)
		elif level == 'warning':
			self.logger.warning(message)
		elif level == 'error':
			self.logger.error(message)
		# 这两行代码是为了避免日志输出重复问题
		self.logger.removeHandler(ch)
		self.logger.removeHandler(fh)
		# 关闭打开的文件
		fh.close()
	
	def debug(self, message):
		self.__console('debug', message)
	
	def info(self, message):
		self.__console('info', message)
	
	def warning(self, message):
		self.__console('warning', message)
	
	def error(self, message):
		self.__console('error', message)

	
	

