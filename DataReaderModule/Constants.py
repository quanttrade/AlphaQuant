__author__ = 'wangjp'


rootPath = r'D:\AlphaQuant'

class DatabaseNames:
    MysqlDaily = 'testdb' #''stocks_data_daily'

class ALIAS_TABLES:         # 表名标记
    TRDDATES = 'trade_dates'
    STKBASIC = 'stocks_basic_info'
    DAILYCNT = 'daily_stocks_count'
    XFILTER = 'FEATURES_FILTER'
    YFILTER = 'RESPONSE_FILTER'
    RESPONSE = 'RESPONSE'
    TRAEDINFO = 'ASHAREEODPRICES'

class ALIAS_FIELDS:         # 基础数据字段标记
    DATE = 'TRADE_DT'
    STKCD = 'S_INFO_WINDCODE'
    STKCNT = 'DAILY_COUNT'

    OPEN = 'S_DQ_OPEN'
    HIGH = 'S_DQ_HIGH'
    LOW = 'S_DQ_LOW'
    CLOSE = 'S_DQ_CLOSE'
    VOLUME = 'S_DQ_VOLUME'
    AMOUNT = 'S_DQ_AMOUNT'
    PCTCHG = 'S_DQ_PCTCHANGE'
    TRDSTAT = 'S_DQ_TRADESTATUS'
    ADJFCT = 'S_DQ_ADJFACTOR'
    STSTAT = 'TYPE_ST'

class ALIAS_RESPONSE:
    OC1 = 'OCDay1'
    CC1 = 'CCDay1'
    OC10 = 'OCDay10'
    OCG1 = 'OCDay1Gap1'
    CCG1 = 'CCDay1Gap1'
    OCG2 = 'OCDay1Gap2'
    CCG2 = 'CCDay1Gap2'
    OCG3 = 'OCDay1Gap3'
    CCG3 = 'CCDay1Gap3'
    OCG4 = 'OCDay1Gap4'
    CCG4 = 'CCDay1Gap4'

class ALIAS_STATUS:        # 状态字段标记
    NOTRD = 'NOTRADE'
    PNOTRD = 'PRENOTRADE'
    ISST = 'ISST'
    LMUP = 'LIMITUP'
    LMDW = 'LIMITDOWN'
    INSFAMT = 'INSFAMT'
    INSFTRD = 'INSFTRADE'
    INSFLST = 'INSFLIST'
    INSFRSM = 'INSFRESUM'

NO_QUICK = ['ASHAREEODPRICES', 'FEATURES_FILTER', 'RESPONSE_FILTER', 'RESPONSE']

QuickTableFieldsDict = {
    'ASHAREEODPRICES': ['S_DQ_OPEN','S_DQ_HIGH','S_DQ_LOW','S_DQ_CLOSE','S_DQ_VOLUME','S_DQ_AMOUNT','S_DQ_PCTCHANGE','S_DQ_TRADESTATUS'],
    'ASHARECAPITALIZATION': ['TOT_SHR', 'FLOAT_SHR', 'FLOAT_A_SHR', 'S_SHARE_TOTALA'],
    'ASHAREFLOATHOLDER':['TOT_HOLDERS', 'PERS_HOLDERS','INST_HOLDERS','TOT_QUANTITY', 'PERS_QUANTITY','INST_QUANTITY'],
    'ASHAREST':['TYPE_ST'],
    'FEATURES_FILTER': ['NOTRADE', 'PRENOTRADE', 'ISST', 'LIMITUP', 'LIMITDOWN', 'INSFAMT','INSFTRADE','INSFLIST', 'INSFRESUM','FilterX'],
    'RESPONSE_FILTER': ['OCRet', 'CORet', 'CCRet', 'NOTRADE', 'ISST', 'COLIMITUP', 'COLIMITDOWN', 'CCLIMITUP', 'CCLIMITDOWN','FilterY'],
    'RESPONSE':['OCDay1','CCDay1','OCDay10','OCDay1Gap1','CCDay1Gap1','OCDay1Gap2','CCDay1Gap2','OCDay1Gap3','CCDay1Gap3','OCDay1Gap4','CCDay1Gap4'],
}

CacheLevlels = {
    'LEVEL1' : ['ASHAREEODPRICES', 'FEATURES_FILTER', 'RESPONSE_FILTER', 'RESPONSE'],
    'LEVEL2' : ['ASHARECAPITALIZATION', 'ASHAREFLOATHOLDER']
}
