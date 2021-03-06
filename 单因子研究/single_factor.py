# 单因子提取器，不包含作图和行业分组
from WindPy import w
import numpy as np
import pandas as pd
import datetime


class SingleFactorReasearch():
    def __init__(self, date, code_list, factor_name):
        # date为查询因子的日期，'yyyy-mm-dd'格式
        # code_list为查询因子的股票代码列表
        self.date = date.split('-')
        self.code_list = code_list
        self.factor_name = factor_name
        self.w = w
        self.w.start()
        self._single_factor_df = self._calculate_factor()
        # print(self._single_factor_df)

    # 具体实现因子计算的部分，返回为DataFrame对象
    def _calculate_factor(self):
        return None

    def get_factor(self):
        return self._single_factor_df


# 净利润增长率
class NetProfitGrowRate(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '净利润增长率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        profit_ttm_now = np.array(w.wss(self.code_list, "fa_profit_ttm", "unit=1;tradeDate=" + ''.join(date_list)).Data[0])
        date_list[0] = str(int(date_list[0])-1)
        profit_ttm_prev = np.array(w.wss(self.code_list, "fa_profit_ttm", "unit=1;tradeDate=" + ''.join(date_list)).Data[0])

        profit_ttm_prev[profit_ttm_prev <= 0.0] = np.nan  # 基期亏损的不考虑此因子，此因子值缺失
        net_profit_grow_rate = (profit_ttm_now - profit_ttm_prev) / profit_ttm_prev
        net_profit_grow_rate = pd.DataFrame(data=net_profit_grow_rate, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 净利润增长率
class NetProfitGrowRateV2(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '净利润增长率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        npgr = np.array(w.wss(self.code_list,  "fa_npgr_ttm", "tradeDate="+"".join(date_list)).Data[0])
        NPGR = pd.DataFrame(data=npgr, index=self.code_list, columns=[self.factor_name])
        return NPGR


# 存货周转率
class InventoryTurnRatio(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '存货周转率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        invturn = np.array(w.wss(self.code_list,  "fa_invturn_ttm", "tradeDate="+"".join(date_list)).Data[0])
        InvTurn = pd.DataFrame(data=invturn, index=self.code_list, columns=[self.factor_name])
        return InvTurn


# 5日移动均线
class MA5(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '5日移动均线'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        MA_data = np.array(w.wss(self.code_list,  "MA", "tradeDate="+"".join(date_list)+";MA_N=5;priceAdj=T;cycle=D").Data[0])
        MA5 = pd.DataFrame(data=MA_data, index=self.code_list, columns=[self.factor_name])
        return MA5


# 10日移动均线
class MA10(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '10日移动均线'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        MA_data = np.array(w.wss(self.code_list,  "MA", "tradeDate="+"".join(date_list)+";MA_N=10;priceAdj=T;cycle=D").Data[0])
        MA10 = pd.DataFrame(data=MA_data, index=self.code_list, columns=[self.factor_name])
        return MA10


# 20日移动均线
class MA20(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '20日移动均线'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        MA_data = np.array(w.wss(self.code_list,  "MA", "tradeDate="+"".join(date_list)+";MA_N=20;priceAdj=T;cycle=D").Data[0])
        MA20 = pd.DataFrame(data=MA_data, index=self.code_list, columns=[self.factor_name])
        return MA20


# 60日移动均线
class MA60(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '60日移动均线'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        MA_data = np.array(w.wss(self.code_list,  "MA", "tradeDate="+"".join(date_list)+";MA_N=60;priceAdj=T;cycle=D").Data[0])
        MA60 = pd.DataFrame(data=MA_data, index=self.code_list, columns=[self.factor_name])
        return MA60


# 120日移动均线
class MA120(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '120日移动均线'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        MA_data = np.array(w.wss(self.code_list,  "MA", "tradeDate="+"".join(date_list)+";MA_N=120;priceAdj=T;cycle=D").Data[0])
        MA120 = pd.DataFrame(data=MA_data, index=self.code_list, columns=[self.factor_name])
        return MA120


# N日移动均线
class MA_N(SingleFactorReasearch):
    def __init__(self, date, code_list, N):
        self.N = N  # N日均线的长度
        factor_name = str(N) + '日移动均线'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        MA_data = np.array(w.wss(self.code_list,  "MA", "tradeDate="+"".join(date_list)+";MA_N="+str(self.N)+";priceAdj=T;cycle=D").Data[0])
        MA_N = pd.DataFrame(data=MA_data, index=self.code_list, columns=[self.factor_name])
        return MA_N


# N日移动均线相对价格比例
class MA_N_rel(SingleFactorReasearch):
    def __init__(self, date, code_list, N):
        self.N = N  # N日均线的长度
        factor_name = str(N) + '日移动均线相对价格比例'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        MA_data = np.array(w.wss(self.code_list,  "MA", "tradeDate="+"".join(date_list)+";MA_N="+str(self.N)+";priceAdj=T;cycle=D").Data[0])
        close_data = np.array(w.wss(self.code_list,  "close", "tradeDate="+"".join(date_list)+";priceAdj=T;cycle=D").Data[0])
        MA_data = MA_data / close_data
        MA_N_rel = pd.DataFrame(data=MA_data, index=self.code_list, columns=[self.factor_name])
        return MA_N_rel


# 5日平均换手率
class VOL5(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '5日平均换手率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-5, "".join(date_list), "").Data[0][0])  # 区间数据
        vol_data = np.array(w.wss(self.code_list, "avg_turn_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        vol_data = vol_data / 100.0
        VOL5 = pd.DataFrame(data=vol_data, index=self.code_list, columns=[self.factor_name])
        return VOL5


# 10日平均换手率
class VOL10(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '10日平均换手率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-10, "".join(date_list), "").Data[0][0])  # 区间数据
        vol_data = np.array(w.wss(self.code_list, "avg_turn_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        vol_data = vol_data / 100.0
        VOL10 = pd.DataFrame(data=vol_data, index=self.code_list, columns=[self.factor_name])
        return VOL10


# 20日平均换手率
class VOL20(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '20日平均换手率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-20, "".join(date_list), "").Data[0][0])  # 区间数据
        vol_data = np.array(w.wss(self.code_list, "avg_turn_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        vol_data = vol_data / 100.0
        VOL20 = pd.DataFrame(data=vol_data, index=self.code_list, columns=[self.factor_name])
        return VOL20


# 60日平均换手率
class VOL60(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '60日平均换手率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-60, "".join(date_list), "").Data[0][0])  # 区间数据
        vol_data = np.array(w.wss(self.code_list, "avg_turn_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        vol_data = vol_data / 100.0
        VOL60 = pd.DataFrame(data=vol_data, index=self.code_list, columns=[self.factor_name])
        return VOL60


# 120日平均换手率
class VOL120(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '120日平均换手率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-120, "".join(date_list), "").Data[0][0])  # 区间数据
        vol_data = np.array(w.wss(self.code_list, "avg_turn_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        vol_data = vol_data / 100.0
        VOL120 = pd.DataFrame(data=vol_data, index=self.code_list, columns=[self.factor_name])
        return VOL120


# 240日平均换手率
class VOL240(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '240日平均换手率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-240, "".join(date_list), "").Data[0][0])  # 区间数据
        vol_data = np.array(w.wss(self.code_list, "avg_turn_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        vol_data = vol_data / 100.0
        VOL240 = pd.DataFrame(data=vol_data, index=self.code_list, columns=[self.factor_name])
        return


# Aroon指标
class AROON(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = 'Aroon指标'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        Aroon_data = np.array(w.wss(self.code_list, "tech_aroon", "tradeDate=" + "".join(date_list)).Data[0])
        Aroon = pd.DataFrame(data=Aroon_data, index=self.code_list, columns=[self.factor_name])
        return Aroon


# MTM动量指标
class MTM(SingleFactorReasearch):
    def __init__(self, date, code_list, MTM_interDay=6, MTM_N=6):
        factor_name = 'MTM指标'
        # MTM_interDay为间隔周期数，MTM_N为均值计算周期数，6为Wind默认参数
        self.MTM_interDay = MTM_interDay
        self.MTM_N = MTM_N
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        MTM_data = np.array(w.wss(self.code_list, "MTM", "tradeDate=" + "".join(date_list) + ";MTM_interDay="+str(self.MTM_interDay)+";MTM_N="+str(self.MTM_N)+";MTM_IO=1;priceAdj=T;cycle=D").Data[0])
        MTM = pd.DataFrame(data=MTM_data, index=self.code_list, columns=[self.factor_name])
        return MTM


# BETA
class BETA_V1(SingleFactorReasearch):
    def __init__(self, date, code_list, refer_index='000001.SH', length=22):
        factor_name = 'BETA'
        self.refer_index = refer_index  # 计算Beta值时用的参考指数
        self.length = 22  # 计算Beta的历史数据长度
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-self.length, "".join(date_list), "").Data[0][0])  # 每个月22个交易日
        beta_data = np.array(w.wss(self.code_list, "beta", "startDate="+startDate+";endDate="+"".join(date_list)+";period=2;returnType=1;index="+self.refer_index).Data[0])
        BETA = pd.DataFrame(data=beta_data, index=self.code_list, columns=[self.factor_name])
        return BETA


# 残差收益波动率，万德因子名称：252日残差收益波动率
# 算法：Ri=a+b*Rb+e,Rb为参考指数沪深300，a为截距项，b即为beta，e为残差项，252日残差收益波动率为252日e的标准差
class HSIGMA_252(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = 'HSIGMA'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        hsigma_252_value = np.array(w.wss(self.code_list, "risk_residvol252", "tradeDate=" + "".join(date_list)).Data[0])*100.0
        HSIGMA_252 = pd.DataFrame(data=hsigma_252_value, index=self.code_list, columns=[self.factor_name])
        return HSIGMA_252


# SKEWNESS，过去20日股价的偏度
class SKEWNESS_20(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '股价偏度'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        skewness_data = np.array(w.wss(self.code_list, "tech_skewness", "tradeDate=" + "".join(date_list)).Data[0])
        SKWNESS_20 = pd.DataFrame(data=skewness_data, index=self.code_list, columns=[self.factor_name])
        return SKWNESS_20


# TURN_VOLATILITY，过去20日换手率相对波动率
class TURN_VOLATILITY_20(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '换手率相对波动率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        volatility_data = np.array(w.wss(self.code_list, "tech_turnoverratevolatility20", "tradeDate=" + "".join(date_list)).Data[0])
        TURN_VOLATILITY_20 = pd.DataFrame(data=volatility_data, index=self.code_list, columns=[self.factor_name])
        return TURN_VOLATILITY_20


# RelativePriceN，当前价格处于过去N个交易日股价的位置 算法：(close - low)/(high - low)
class RelativePriceN(SingleFactorReasearch):
    def __init__(self, date, code_list, N=252):
        factor_name = 'FiftyTwoWeekHigh'
        self.N = N  # 计算窗口期
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(--self.N, "".join(date_list), "").Data[0][0])
        high_price = np.array(w.wss(self.code_list, "high_per", "startDate="+"".join(startDate)+";endDate="+"".join(date_list)+";priceAdj=T").Data[0])
        low_price = np.array(w.wss(self.code_list, "low_per", "startDate="+"".join(startDate)+";endDate="+"".join(date_list)+";priceAdj=T").Data[0])
        close_price = np.array(w.wss(self.code_list, "close_per", "startDate="+"".join(startDate)+";endDate="+"".join(date_list)+";priceAdj=T").Data[0])
        relative_position = (close_price - low_price)/(high_price - low_price)
        RelativePriceN = pd.DataFrame(data=relative_position, index=self.code_list, columns=[self.factor_name])
        return RelativePriceN


# N日平均换手率
class VOL_N(SingleFactorReasearch):
    def __init__(self, date, code_list, N):
        self.N = N
        factor_name = str(N) + '日平均换手率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-self.N, "".join(date_list), "").Data[0][0])  # 区间数据
        vol_data = np.array(w.wss(self.code_list, "avg_turn_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        vol_data = vol_data / 100.0
        VOL240 = pd.DataFrame(data=vol_data, index=self.code_list, columns=[self.factor_name])
        return VOL240


# 对数市值  # 算法：np.log(个股当日股价*当日总股本)
class LCap(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '对数市值'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        log_Cap = np.log(w.wss(self.code_list, "val_lnmv", "tradeDate=" + "".join(date_list)).Data[0])
        LCap = pd.DataFrame(data=log_Cap, index=self.code_list, columns=[self.factor_name])
        return LCap


# 对数流通市值
class LFloatCap(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '对数市值'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        log_Circulation_Cap = np.log(w.wss(self.code_list, "val_lnfloatmv", "tradeDate=" + "".join(date_list)).Data[0])
        LFloatCap = pd.DataFrame(data=log_Circulation_Cap, index=self.code_list, columns=[self.factor_name])
        return LFloatCap


# RSI指标
class RSI(SingleFactorReasearch):
    def __init__(self, date, code_list, N=6):
        factor_name = '相对强度指标RSI'
        self.N = N
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        rsi_index = w.wss(self.code_list, "RSI", "industryType=1;tradeDate="+''.join(date_list)+";RSI_N="+str(self.N)+";priceAdj=T;cycle=D").Data[0]
        net_profit_grow_rate = pd.DataFrame(data=rsi_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 成交量比率  # VolumeRatio = N日内上升日成交额总和/N日内下降日成交额总和, 万得默认N=26
class VR(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '成交量比率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        vr_data = np.array(w.wss(self.code_list, "tech_vr", "tradeDate=" + "".join(date_list)).Data[0])
        VR = pd.DataFrame(data=vr_data, index=self.code_list, columns=[self.factor_name])
        return VR


# 20日资金流量  # 用20日的收盘价、最高价及最低价的均值乘以20日成交量即可得到该交易日的资金流量
class MoneyFlow20(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '20日资金流量'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-20, "".join(date_list), "").Data[0][0])  # 区间数据
        price_data = np.array(w.wss(self.code_list, "high_per,low_per,close_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list) + ";priceAdj=T").Data)
        avg_price = np.sum(price_data, axis=0) / 3.0
        volume = np.array(w.wss(self.code_list, "vol_per", "unit=1;startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        result = avg_price * volume
        MoneyFlow20 = pd.DataFrame(data=result, index=self.code_list, columns=[self.factor_name])
        return MoneyFlow20


# N日资金流量  # 用N日的收盘价、最高价及最低价的均值乘以20日成交量即可得到该交易日的资金流量
class MoneyFlow_N(SingleFactorReasearch):
    def __init__(self, date, code_list, N):
        self.N = N
        factor_name = str(N) + '日资金流量'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        startDate = str(w.tdaysoffset(-self.N, "".join(date_list), "").Data[0][0])  # 区间数据
        price_data = np.array(w.wss(self.code_list, "high_per,low_per,close_per", "startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list) + ";priceAdj=T").Data)
        avg_price = np.sum(price_data, axis=0) / 3.0
        volume = np.array(w.wss(self.code_list, "vol_per", "unit=1;startDate=" + "".join(startDate) + ";endDate=" + "".join(date_list)).Data[0])
        result = avg_price * volume
        MoneyFlow20 = pd.DataFrame(data=result, index=self.code_list, columns=[self.factor_name])
        return MoneyFlow20


# ROE指标
class ROE(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '权益回报率ROE'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        roe_ttm = np.array(w.wss(self.code_list, "fa_roe_ttm", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=roe_ttm, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 基本每股收益EPS
class BasicEPS(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '基本每股收益EPS'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        eps_index = np.array(w.wss(self.code_list, "fa_eps_basic", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=eps_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 稀释每股收益EPS
class DilutedEPS(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '稀释每股收益'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        eps_data = np.array(w.wss(self.code_list, "fa_eps_diluted", "tradeDate=" + "".join(date_list)).Data[0])
        DilutedEPS = pd.DataFrame(data=eps_data, index=self.code_list, columns=[self.factor_name])
        return DilutedEPS


# ROA
class ROA(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = 'ROA'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        roa_data = np.array(w.wss(self.code_list, "fa_roa_ttm", "tradeDate=" + "".join(date_list)).Data[0])/100.0
        ROA = pd.DataFrame(data=roa_data, index=self.code_list, columns=[self.factor_name])
        return ROA


# EquityToAsset
class EquityToAsset(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = 'EquityToAsset'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        total_equity = np.array(w.wss(self.code_list, "fa_equity", "tradeDate"+"".join(self.date)).Data[0])
        total_asset = np.array(w.wss(self.code_list, "fa_totassets", "tradeDate"+"".join(self.date)).Data[0])
        data = total_equity/total_asset
        EquityToAsset = pd.DataFrame(data=data, index=self.code_list, columns=[self.factor_name])
        return EquityToAsset


# FixAssetRatio
class FixAssetRatio(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '固定资产比率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        fixed_asset = np.array(w.wss(self.code_list, "fa_fixassets", "tradeDate="+"".join(date_list)).Data[0])
        total_asset = np.array(w.wss(self.code_list, "fa_totassets", "tradeDate="+"".join(date_list)).Data[0])
        data = fixed_asset/total_asset
        FixAssetRatio = pd.DataFrame(data=data, index=self.code_list, columns=[self.factor_name])
        return FixAssetRatio


# 账面杠杆
class BLEV(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '账面杠杆'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        blev_data = np.array(w.wss(self.code_list, "fa_blev", "tradeDate=" + "".join(date_list)).Data[0])
        BLEV = pd.DataFrame(data=blev_data, index=self.code_list, columns=[self.factor_name])
        return BLEV


# ORPS指标
class ORPS(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '每股营业收入ORPS'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        orps_index = np.array(w.wss(self.code_list, "orps_ttm", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=orps_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 销售毛利率
class GrossIncomeRatio(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '销售毛利率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        grossprofit_data = np.array(w.wss(self.code_list, "fa_grossprofitmargin_ttm", "tradeDate=" + "".join(date_list)).Data[0])/100.0
        GrossIncomeRatio = pd.DataFrame(data=grossprofit_data, index=self.code_list, columns=[self.factor_name])
        return GrossIncomeRatio


# 资产负债率
class DebetToAsset(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '资产负债率'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        debet_to_asset = np.array(w.wss(self.code_list, "fa_debttoasset", "tradeDate=" + "".join(date_list)).Data[0])/100.0
        DebetToAsset = pd.DataFrame(data=debet_to_asset, index=self.code_list, columns=[self.factor_name])
        return DebetToAsset


# 经营活动现金流与企业价值比
class CFO2EV(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '经营现金流比企业价值'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        OpCash = np.array(w.wss(self.code_list, "fa_operactcashflow_ttm", "tradeDate="+"".join(date_list)).Data[0])
        Rev_Ev = np.array(w.wss(self.code_list, "val_ortoev_ttm", "tradeDate="+"".join(date_list)).Data[0])
        Rev = np.array(w.wss(self.code_list, "fa_or_ttm", "tradeDate="+"".join(date_list)).Data[0])
        CFO2EV_data = OpCash/(Rev/Rev_Ev)
        GrossIncomeRatio = pd.DataFrame(data=CFO2EV_data, index=self.code_list, columns=[self.factor_name])
        return GrossIncomeRatio


# 未来预期盈利增长
# 建议不使用此因子 数据不全+没有参考价值
class ForecastEarningGrowth_FY1_3M(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '三个月个月盈利变化率（一年）预测'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        Forecast_data = np.array(w.wss(self.code_list, "west_netprofit_fy1_3m","tradeDate=" + "".join(date_list)).Data[0])/100.0
        ForecastEarningGrowth = pd.DataFrame(data=Forecast_data, index=self.code_list, columns=[self.factor_name])
        return ForecastEarningGrowth


# CFPS指标，每股现金流量
class CFPS(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '每股现金流CFPS'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        cfps_index = np.array(w.wss(self.code_list, "fa_cfps_ttm", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=cfps_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# OCFPS指标，经营活动每股现金流量
class OCFPS(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '经营活动每股现金流OCFPS'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        ocfps_index = np.array(w.wss(self.code_list, "fa_ocfps_ttm", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=ocfps_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 市值/企业自由现金流
class MarketValueToFreeCashFlow(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '市值/企业自由现金流'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        val_mvtofcff = np.array(w.wss(self.code_list, "val_mvtofcff", "tradeDate=" + ''.join(date_list)).Data[0])
        MarketValueToFreeCashFlow = pd.DataFrame(data=val_mvtofcff, index=self.code_list, columns=[self.factor_name])
        return MarketValueToFreeCashFlow


# LogEV(含货币资金)指标
class LogEVWithCash(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '对数企业价值（含货币资金）LogEV'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        ev1_index = np.array(w.wss(self.code_list, "ev1", "tradeDate=" + ''.join(date_list)).Data[0])
        ev1_index = np.log(ev1_index)
        net_profit_grow_rate = pd.DataFrame(data=ev1_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# PE指标
class PE(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '市盈率PE'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        pe_index = np.array(w.wss(self.code_list, "pe_ttm", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=pe_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# PB指标
class PB(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = 'PB市净率指标'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        pb_index = np.array(w.wss(self.code_list, "pb_lf", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=pb_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 股息率指标
class DividendYield(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '股息率指标'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        dividendyield_index = np.array(w.wss(self.code_list, "dividendyield2", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=dividendyield_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 每股企业自由现金流指标
class FreeCashFlowPerShare(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '每股企业自由现金流指标'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        fa_fcffps_index = np.array(w.wss(self.code_list, "fa_fcffps", "tradeDate=" + ''.join(date_list)).Data[0])
        net_profit_grow_rate = pd.DataFrame(data=fa_fcffps_index, index=self.code_list, columns=[self.factor_name])
        return net_profit_grow_rate


# 股价/每股企业自由现金流
class PriceFreeCashFlowPerShare(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '股价_每股企业自由现金流'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        fa_fcffps_index = np.array(w.wss(self.code_list, "fa_fcffps", "tradeDate=" + ''.join(date_list)).Data[0])
        price = np.array(w.wss(self.code_list, "close", "tradeDate=" + ''.join(date_list) + ';priceAdj=U;cycle=D').Data[0])
        price_fa_fcffps = pd.DataFrame(data=fa_fcffps_index/price, index=self.code_list, columns=[self.factor_name])
        return price_fa_fcffps


# 带息债务/全部投入资本
class InterestBearingDebtInvestmentCapital(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '带息债务_全部投入资本指标'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        fa_interestdebttocapital_index = np.array(w.wss(self.code_list, "fa_interestdebttocapital", "tradeDate=" + ''.join(date_list)).Data[0])
        fa_interestdebttocapital_index = pd.DataFrame(data=fa_interestdebttocapital_index, index=self.code_list, columns=[self.factor_name])
        return fa_interestdebttocapital_index


# 长期负债/营运资金
class LongTermLiabilityToWorkCapital(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '长期负债/营运资金'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list = self.date
        fa_uncurdebttoworkcap = np.array(w.wss(self.code_list, "fa_uncurdebttoworkcap", "tradeDate=" + ''.join(date_list)).Data[0])
        fa_uncurdebttoworkcap = pd.DataFrame(data=fa_uncurdebttoworkcap, index=self.code_list, columns=[self.factor_name])
        return fa_uncurdebttoworkcap


# 股权质押比例（三年统计）
class StockPledgeRatio(SingleFactorReasearch):
    def __init__(self, date, code_list):
        factor_name = '股权质押比例（三年统计）'
        super().__init__(date, code_list, factor_name)

    def _calculate_factor(self):
        date_list_end = self.date
        date_list_start = date_list_end.copy()
        date_list_start[0] = str(int(date_list_start[0])-3)
        date_list_end = '-'.join(date_list_end)
        date_list_start = '-'.join(date_list_start)
        data_temp = w.wset("sharepledge", "startdate="+date_list_start+";enddate="+date_list_end+";sectorid=a001010100000000;field=wind_code,pledged_shares,pledge_end_date,pledge_termination_date").Data
        # 将None数据用一个遥远的时间代替
        data_temp[2] = self._replace_list(data_temp[2])
        data_temp[3] = self._replace_list(data_temp[3])

        df = pd.DataFrame(data=np.array([data_temp[1], data_temp[2], data_temp[3]]).transpose(), index=data_temp[0])
        df[0] = df[0] * 10000.0  # 把质押的份数换为股数
        # 取出所有未到期的股权质押信息
        df = df[(df[1]>datetime.datetime.strptime(date_list_end, '%Y-%m-%d')) & (df[2]>datetime.datetime.strptime(date_list_end, '%Y-%m-%d'))]
        ds = df[0]  # 全A个股处于股权质押状态的股票数量
        ds = ds.sum(level=0)
        all_shares = w.wss(self.code_list, "total_shares", "unit=1;tradeDate=" + ''.join(self.date)).Data[0]  # 获取总股本列表
        for i in range(len(self.code_list)):  # 计算个股的抵押比例
            code_temp = self.code_list[i]
            try:
                pledge_shares = ds[code_temp]
            except:
                pledge_shares = 0
            all_shares[i] = pledge_shares / all_shares[i]
        df_ratio = pd.DataFrame(data=all_shares, index=self.code_list, columns=[self.factor_name])  # 对应个股的总股本
        return df_ratio

    def _replace_list(self, list):
        for i in range(len(list)):
            if list[i] == None:
               list[i] = datetime.datetime.strptime('2200-12-31', '%Y-%m-%d')
        return list


if __name__ == '__main__':
    date = '2017-05-09'
    w.start()
    # code_list = w.wset("sectorconstituent", "date=" + date + ";windcode=000300.SH").Data[1]  # 沪深300动态股票池
    code_list = ['000001.SZ', '000002.SZ']
    factor_model = PB(date, code_list)
    df = factor_model.get_factor()
    # df.to_csv('temp1.csv')
    print(df)