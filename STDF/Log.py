import os
import logging
import time
#时间戳转时间文本

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)   # 设置总日志等级

    format = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y年%m月%d日 %H:%M:%S')  # 日志格式

    cli_handler = logging.StreamHandler()  # 输出到屏幕的日志处理器
    path = os.getcwd()
    if os.path.exists('log'):
        pass
    else:  
        os.mkdir(path+'\\log')
     # 返回当前工作目录
    path=path+'\\log'
    real_time=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(int(time.time())))
    file_handler = logging.FileHandler(filename=path+'\\run_'+real_time+'.log', mode='a', encoding='utf-8')  # 输出到文件的日志处理器

    cli_handler.setFormatter(format)  # 设置屏幕日志格式
    file_handler.setFormatter(format)  # 设置文件日志格式

    cli_handler.setLevel(logging.INFO)  # 设置屏幕日志等级, 可以大于日志记录器设置的总日志等级
    # file_hander.setLevel(logging.DEBUG)  # 不设置默认使用logger的等级

    logger.handlers.clear()  # 清空已有处理器, 避免继承了其他logger的已有处理器
    logger.addHandler(cli_handler)  # 将屏幕日志处理器添加到logger
    logger.addHandler(file_handler)  # 将文件日志处理器添加到logger
    return logger


logger = get_logger('logger')


# logger.debug('调试级别的日志')
# logger.info('信息基本的日志')
# logger.warning('警告级别的日志')
# logger.error('错误级别的日志')
# logger.critical('严重错误级别的日志')
