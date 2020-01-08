import logging
import os
import datetime
class TestLogging():
    debugs=[]
    infos=[]
    warnings=[]
    errors=[]
    criticals=[]

    def __init__(self,test_name):
        self.logger=logging.getLogger(test_name)
        now = datetime.datetime.now()
        t = '{}.{}.{}'.format(now.day, now.month, now.year)
        self.dir = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'Logs')
        print("Logs directory:",self.dir)
        self.log_fname = os.path.join(self.dir, '{}-{}.log'.format(test_name, t))
        print ("Log file:",self.log_fname)
        self.c_handler = logging.StreamHandler()
        #self.f_handler = logging.FileHandler('C:/Users/tolos/Documents/GitHub/CH_096_TAQC/Loggs//{}-{}.log'.format(test_name, t))
        self.f_handler = logging.FileHandler(self.log_fname)
        self.c_handler.setLevel(logging.WARNING)
        self.f_handler.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        c_format = logging.Formatter('%(process)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
        f_format = logging.Formatter('%(process)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
        self.c_handler.setFormatter(c_format)
        self.f_handler.setFormatter(f_format)
    def sendreport(self):
        self.logger.addHandler(self.c_handler)
        self.logger.addHandler(self.f_handler)
        for i in self.debugs:
            self.logger.debug(i)
        for i in self.infos:
            self.logger.info(i)
        for i in self.warnings:
            self.logger.warning(i)
        for i in self.errors:
            self.logger.error(i)
        for i in self.criticals:
            self.logger.critical(i)


#loger=TestLogging(__name__)
#category_old='old'
#category_new='new'
#messages_error = ("Category {} was not created".format(category_old),
#                      "Category {} was not edited to {}".format(category_old,category_new),
#                      "Test Failed")
#loger.criticals.append(messages_error[0])
#loger.infos.append("infa")
#loger.errors.append("error_bida")
#for i in loger.criticals:
#    loger.logger.critical(i)
#loger.logger.addHandler(loger.f_handler)
#loger.sendreport()



