#coding=utf8
__author__ = 'wangjp'

import os
import sys
import datetime as dt
import configparser as cp

import mysql.connector

import numpy as np
import pandas as pd

from DataReaderModule.Constants import ALIAS_FIELDS, ALIAS_TABLES,DatabaseNames,rootPath


class Calendar:

    _tradeDates = None
    HeadDate = None
    TailDate = None

    def __init__(self, dateSource='h5'):
        cfp = cp.ConfigParser()
        self.dateSource = dateSource
        if self.dateSource=='mysql':
            cfp.read(os.path.join(rootPath, 'Configs', 'loginInfo.ini'))
            loginfoMysql = dict(cfp.items('Mysql'))
            self.connMysqlRead = mysql.connector.connect(user=loginfoMysql['user'],
                                                         password=loginfoMysql['password'],
                                                         host=loginfoMysql['host'])
        else:
            cfp.read(os.path.join(rootPath, 'Configs', 'dataPath.ini'))
            self.h5File = os.path.join(cfp.get('data','h5'),'{}.h5'.format(ALIAS_TABLES.TRDDATES))
        self._load_trade_dates()

    def _load_trade_dates(self):
        if Calendar._tradeDates is None:
            if self.dateSource=='mysql':
                mysqlCursor = self.connMysqlRead.cursor()
                mysqlCursor.execute('SELECT * FROM {0}.{1}'.format(DatabaseNames.MysqlDaily, ALIAS_TABLES.TRDDATES))
                tDates = pd.DataFrame(mysqlCursor.fetchall(), columns=[ALIAS_FIELDS.DATE])
            else:
                tDates = pd.read_hdf(path_or_buf=self.h5File,
                                     key=ALIAS_TABLES.TRDDATES,
                                     columns=[ALIAS_FIELDS.DATE],
                                     mode='r')
            tDates.sort_values(by = ALIAS_FIELDS.DATE, inplace=True)
            Calendar._tradeDates = tDates.values[:,0]
            Calendar.HeadDate = Calendar._tradeDates[0]
            Calendar.TailDate = Calendar._tradeDates[-1]

    def _calibrate_date(self, currDate, currSide='left'):
        currDate = str(currDate)
        if currDate not in self._tradeDates:    # curr 非交易日，先进行校准
            if currDate > self._tradeDates[-1]:
                currDate = self._tradeDates[-1]
            elif currDate < self._tradeDates[0]:
                currDate = self._tradeDates[0]
            else:
                currDate = self._tradeDates[self._tradeDates<currDate][-1] if currSide=='left' else self._tradeDates[self._tradeDates>currDate][0]
        return currDate

    def tdaysoffset(self, num, currDates, currSide='left'):
        """
        计算 根据 currDate 日期, 移动 num 日 所得到的 交易日
        :param num:
        :param currDate:
        :param currSide: 如果currDate 不是交易日，将起始日期 设置为距离currDate 左边 还是 右边
        :return:
        """
        singleDate = False
        if not (isinstance(currDates,np.ndarray) or isinstance(currDates, list)):
            singleDate = True
            currDates = np.array([str(currDates)])
        totDayNum = self._tradeDates.shape[0]
        currDates = [self._calibrate_date(currDate=crd, currSide=currSide) for crd in currDates ]   # calibrate first
        currPos = np.array([np.sum(self._tradeDates<crd) for crd in currDates])
        changedPos = currPos + num
        changedPos[changedPos<0] = 0
        changedPos[changedPos>totDayNum-1] = totDayNum - 1
        offDates = self._tradeDates[changedPos]
        return offDates[0] if singleDate else offDates

    def tdayscount(self, headDate, tailDate, selectType='CloseOpen'):
        """
        计算 heat 至 tail 期间天数
        :param head:
        :param tail:
        :param selectType:
        :return:
        """
        tdaysBetween = self.tdaysbetween(headDate, tailDate, selectType)
        return tdaysBetween.shape[0]

    def tdaysbetween(self, headDate, tailDate, selectType='CloseOpen'):
        """
        读取 head  至 tail 期间的 betweendDays
        :param head:
        :param tail:
        :param selectType: 区间分割类型 闭开 闭闭 开闭 开开
        :return:
        """
        headDate = str(headDate)
        tailDate = str(tailDate)
        if headDate > tailDate:
            return pd.DataFrame([], columns=[ALIAS_TABLES.TRDDATES])
        if selectType=='CloseOpen':  # 含头不含尾
            idx = (self._tradeDates >= headDate) & (self._tradeDates < tailDate)
        elif selectType=='CloseClose':  # 含头含尾
            idx = (self._tradeDates >= headDate) & (self._tradeDates <= tailDate)
        elif selectType=='OpenClose':  # 含头含尾
            idx = (self._tradeDates > headDate) & (self._tradeDates <= tailDate)
        else:
            idx = (self._tradeDates > headDate) & (self._tradeDates < tailDate)
        return self._tradeDates[idx]

    def tendsbetween(self, headDate, tailDate, selectType='CloseOpen', frequency='month'):
        """
        提取不同周期的末端 交易日
        :param headDate:
        :param tailDate:
        :param frequency:
        :return:
        """
        headDate = str(headDate)
        tailDate = str(tailDate)
        if frequency=='year':
            years = []




if __name__=='__main__':
    c1 = Calendar()
    print(c1.tdaysbetween(19910101,20180810))
    print(c1.tdayscount(20180801,20180802))
    print(c1.tdaysoffset(1,[20180804,20180805,20180806], currSide='left'))