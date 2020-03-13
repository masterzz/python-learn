from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib
import pandas as pd


# 搜集iq出账实收数据，201902-202001
def acct_collect():
    content = r"select a.user_id, b.OTH_FEE2 , b.RENT_FEE2, b.INCRE_FEE2 , b.SMS_FEE2 , b.VO_FEE2, b.CUR_INCOME2, c.MON_CATEGORY_FEE001, c.MON_CATEGORY_FEE031, d.CUR_INCOME , f.PRODUCT_RENT P1, g.PRODUCT_RENT P2, h.MON_CATEGORY_FEE031 MON_CATEGORY_FEE0311 , b.OVER_PRODUCT_FEE_01, b.OVER_PRODUCT_FEE_02, b.OVER_PRODUCT_FEE , d.MEALOUT_QT_FEE , d.MEALOUT_CALL_FEE , d.MEALOUT_SMS_FEE, d.DATA_PLANOUT_INCOME, d.PROM_FEE PROM_FEE1, j.EPARCHY_CODE , g.AGE, j.JOIN_MONTH , t.LEV_2, substr(g.PSPT_ID,1,6) PSPT_CITY, k.ADD_DURATION , k.ADD_CALL_TIMES , l.ADD_STREAM into zhubr_tmp_202002 from dc_cust_data.DWU_AI_USER_INFO_01_20200224 a inner join dc_cust_data.DWU_AI_USER_INFO_01_20200224 j on (j.brand_code like '1%' or j.brand_code like 'D%') and j.on_tag = '1' and a.user_id = j.user_id left join DC_CEN.SRV_DIM_CONVERT_CHANNEL_BNESS t on t.LEV_ID = j.DEVELOP_DEPART_ID left join dc_cust_data.DWU_AI_ACCT_20200224 b on a.user_id = b.user_id left join dc_cust_data.DWD_AI_FEECY_WIDE_20200224 c on a.user_id = c.user_id left join dc_cust_data.DWU_DIM_1_ACCT_202001 d on a.user_id = d.user_id left join dc_cust_data.DWU_AI_USER_INFO_02_202001 f on a.user_id = f.user_id left join dc_cust_data.DWU_AI_USER_INFO_02_20200224 g on a.user_id = g.user_id left join dc_cust_data.DWD_AI_FEECY_WIDE_20200124 h on a.user_id = h.user_id left join dc_cust_data.DWU_CALL_20200224 k on a.user_id = k.user_id left join dc_cust_data.DWU_GS_20200224 l on a.user_id = l.user_id;"
    # test = '201902'
    content = content.replace("202001", "201912").replace("202002", "202001")
    print(content)
    content = content.replace("201912", "201911").replace("202001", "201912")
    print(content)
    content = content.replace("201911", "201910").replace("201912", "201911")
    print(content)


# 作图表示1个月中每一天的流量走势
def plotGprs():
    x = range(20200301, 20200311, 1)
    y = [4341.758803, 4329.315044, 4106.401714, 4035.227659, 4056.395007, 4073.575122, 4068.307837, 4033.35269,
         3816.297639, 4296.004657]
    plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(x, y)
    _xtick_labels = [i for i in range(20200301, 20200311)]
    # plt.xticks(range(20200301, 20200311, 1))
    plt.xticks(_xtick_labels)
    plt.yticks(range(0, 5000, 500))
    plt.show()


# 输出19年2月到20年2月每个月iq的出账收入
def plotAcctMon():
    beginDate = '2019-02-01'
    endDate = '2020-03-11'

    date_index = pd.date_range(beginDate, endDate)
    days = [pd.Timestamp(x).strftime("%Y-%m-%d") for x in date_index.values]

    tmp = []
    for index, v in enumerate(days):
        if index == len(days) - 1:
            tmp.append(days[index])
        if index == 0:
            # tmp.append(days[0])
            continue
        else:
            _ = v.split('-')[2]
            if _ == '01':
                # 取一个月的最后一天
                tmp.append(days[index - 1])
                # 取一个月的第一天
                # tmp.append(days[index])

    # print(tmp)
    # result是日表最后一天的累计值
    result = ''
    # result1是月表的出账收入值
    result1 = ''
    # 获取统计语句
    for x in tmp:
        end_date = x.replace('-', '')
        result = result + '(select %s,sum(CUR_INCOME2) from dc_cust_data.DWU_AI_ACCT_%s)' % (
            end_date[0:6], end_date) + "union"
        result1 = result1 + '(select %s,sum(CUR_INCOME)  from dc_cust_data.DWU_DIM_1_ACCT_%s)' % (
            end_date[0:6], end_date[0:6]) + "union"

    # print(result1)
    # 读取月统计数据
    day_end = pd.read_table("F:/信息化/大数据中心/模型组/需求/漫游结算预测/研发设计/数据处理/出账数据/201902-202002_iq_day_sum.txt", header=None)
    mon_end = pd.read_table("F:/信息化/大数据中心/模型组/需求/漫游结算预测/研发设计/数据处理/出账数据/201902-202002_iq_mon_sum.txt", header=None)

    day_end.columns = ['month', 'acct']
    mon_end.columns = ['month', 'acct']
    matplotlib.rc("font", family='MicroSoft YaHei', weight="bold")
    plt.figure(figsize=(20, 8), dpi=80)
    # 按月份排序
    day_end.sort_values("month", inplace=True)
    mon_end.sort_values("month", inplace=True)
    day_end['acct'] = day_end['acct'] / 10 ** 10
    mon_end['acct'] = mon_end['acct'] / 10 ** 10

    # 处理月份数据
    plt.xticks(list(range(0, len(day_end['month']))), day_end['month'], rotation=45)
    # plt.yticks([x/3 for x in range(1,75)])
    plt.plot(list(range(0, len(day_end['month']))), day_end['acct'], label="IQ-日指标")
    plt.plot(list(range(0, len(mon_end['month']))), mon_end['acct'], label="IQ-月指标")
    plt.legend(loc="upper left")

    plt.xlabel("月份")
    plt.ylabel("出账应收（亿元）")
    plt.title("2019年2月到2020年2月各月出账应收")
    plt.show()


# 获取iq建模数据
def getIqModelData():
    beginDate = '2019-02-01'
    endDate = '2020-03-11'

    date_index = pd.date_range(beginDate, endDate)
    days = [pd.Timestamp(x).strftime("%Y-%m-%d") for x in date_index.values]

    tmp = []
    for index, v in enumerate(days):
        if index == len(days) - 1:
            tmp.append(days[index])
        if index == 0:
            # tmp.append(days[0])
            continue
        else:
            _ = v.split('-')[2]
            if _ == '01':
                # 取一个月的最后一天
                tmp.append(days[index - 1])
                # 取一个月的第一天
                # tmp.append(days[index])
    mon_len = len(tmp)
    result = ''
    i = 0
    while i < mon_len - 1:
        mon_1 = tmp[i].replace('-', '')
        mon_2 = tmp[i + 1].replace('-', '')
        result = "select a.user_id, b.OTH_FEE2 , b.RENT_FEE2, b.INCRE_FEE2 , b.SMS_FEE2 , b.VO_FEE2, b.CUR_INCOME2, c.MON_CATEGORY_FEE001, c.MON_CATEGORY_FEE031, d.CUR_INCOME , f.PRODUCT_RENT P1, g.PRODUCT_RENT P2, h.MON_CATEGORY_FEE031 MON_CATEGORY_FEE0311 , b.OVER_PRODUCT_FEE_01, b.OVER_PRODUCT_FEE_02, b.OVER_PRODUCT_FEE , d.MEALOUT_QT_FEE , d.MEALOUT_CALL_FEE , d.MEALOUT_SMS_FEE, d.DATA_PLANOUT_INCOME, d.PROM_FEE PROM_FEE1, j.EPARCHY_CODE , g.AGE, j.JOIN_MONTH , t.LEV_2, substr(g.PSPT_ID,1,6) PSPT_CITY, k.ADD_DURATION , k.ADD_CALL_TIMES , l.ADD_STREAM into zhubr_tmp_$2$ from dc_cust_data.DWU_AI_USER_INFO_01_$2$24 a inner join dc_cust_data.DWU_AI_USER_INFO_01_$2$24 j on (j.brand_code like '1%' or j.brand_code like 'D%') and j.on_tag = '1' and a.user_id = j.user_id left join DC_CEN.SRV_DIM_CONVERT_CHANNEL_BNESS t on t.LEV_ID = j.DEVELOP_DEPART_ID left join dc_cust_data.DWU_AI_ACCT_$2$24 b on a.user_id = b.user_id left join dc_cust_data.DWD_AI_FEECY_WIDE_$2$24 c on a.user_id = c.user_id left join dc_cust_data.DWU_DIM_1_ACCT_$1$ d on a.user_id = d.user_id left join dc_cust_data.DWU_AI_USER_INFO_02_$1$ f on a.user_id = f.user_id left join dc_cust_data.DWU_AI_USER_INFO_02_$2$24 g on a.user_id = g.user_id left join dc_cust_data.DWD_AI_FEECY_WIDE_$1$24 h on a.user_id = h.user_id left join dc_cust_data.DWU_CALL_$2$24 k on a.user_id = k.user_id left join dc_cust_data.DWU_GS_$2$24 l on a.user_id = l.user_id;" \
            .replace("$2$", mon_2[0:6]).replace("$1$", mon_1[0:6])
        print(result)
        i = i + 1


if __name__ == '__main__':
    # plotAcctMon()
    getIqModelData()
