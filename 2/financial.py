from random import random
from time import sleep
from tqdm import tqdm
from typing import Callable
from pylab import mpl
from matplotlib import pyplot as plt
import akshare as ak
import os
import os.path as path
import pandas as pd
import pathlib as pl


# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["Songti SC"]
mpl.rcParams["axes.unicode_minus"] = False


class DataLoader:
    """
    Load data from akshare and save it to local file.
    """
    stock_zcfz_em_df: pd.DataFrame
    stock_lrb_em_df: pd.DataFrame
    stock_xjll_em_df: pd.DataFrame
    stock_yjbb_em_df: pd.DataFrame

    def __init__(self, date: str):
        self.load_data(date)

    @staticmethod
    def load_df_em(p: pl.Path, getter: Callable[[], pd.DataFrame]) -> pd.DataFrame:
        '''
        Load DataFrame from local file, if the file does not exist, call getter to get the data.
        '''
        # 使用 pickle 格式保存数据以保证类型的准确和减少加载时间
        if not path.exists(p):
            df = getter()
            df.set_index("股票代码", inplace=True)
            df.to_pickle(p)
        return pd.read_pickle(p)

    @staticmethod
    def load_df_sina(p: pl.Path, getter: Callable[[], pd.DataFrame]) -> tuple[pd.DataFrame, bool]:
        '''
        Load DataFrame from local file, if the file does not exist, call getter to get the data.
        '''
        # 使用 pickle 格式保存数据以保证类型的准确和减少加载时间
        cached = True
        if not path.exists(p):
            df = getter()
            df.to_pickle(p)
            cached = False
        return pd.read_pickle(p), cached

    def load_data(self, date: str):
        DIR = pl.Path("data")
        os.makedirs(DIR, exist_ok=True)
        self.stock_zcfz_em_df = self.load_df_em(
            DIR / f"stock_zcfz_em-{date}.pkl",
            lambda: ak.stock_zcfz_em(date=date)
        )
        self.stock_lrb_em_df = self.load_df_em(
            DIR / f"stock_lrb_em-{date}.pkl",
            lambda: ak.stock_lrb_em(date=date)
        )
        self.stock_xjll_em_df = self.load_df_em(
            DIR / f"stock_xjll_em-{date}.pkl",
            lambda: ak.stock_xjll_em(date=date)
        )
        self.stock_yjbb_em_df = self.load_df_em(
            DIR / f"stock_yjbb_em-{date}.pkl",
            lambda: ak.stock_yjbb_em(date=date)
        )


DATES = ["20201231", "20211231", "20221231", "20231231"]
data = {date: DataLoader(date) for date in DATES}

codes: set = set(data[DATES[0]].stock_zcfz_em_df.index.array)
for date in DATES[1:]:
    codes = codes.intersection(set(data[date].stock_zcfz_em_df.index.array))
list_codes: list = [*codes]
list_codes.sort()
print(len(list_codes))


class FinancialLoader:
    stock_financial_analysis_indicator_df: dict[str, pd.DataFrame]

    def __init__(self, codes: list[str], names: dict[str, str]):
        DIR = pl.Path("data")
        self.stock_financial_analysis_indicator_df = dict()
        for code in tqdm(codes):
            os.makedirs(DIR / "stocks" / code, exist_ok=True)
            self.stock_financial_analysis_indicator_df[code], cached = DataLoader.load_df_sina(
                DIR / "stocks" / code / f"stock_financial_analysis_indicator.pkl",
                lambda: ak.stock_financial_analysis_indicator(
                    symbol=code)
            )
            if not cached:
                sleep(28+4*random())


financial = FinancialLoader(list_codes, {
                            code: data[DATES[0]].stock_zcfz_em_df.loc[code, "股票简称"] for code in list_codes})
