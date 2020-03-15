print("==============")
result = 9.22*10**6*1.227*10**4/1000/1000
money2 = 9.22*10**6*1.227*10**4 * 0.002 / 10 ** 8
realflow2 =  115837985649529384 / 10**12
print("%s"  %result)
print("money2: %s" %money2)
print("real realflow2: %s " %realflow2)

result1 = 7.8463 * 10


money = 13805067553.36 /100/ 10**4
print(money)
print("======mod_gprs_mon_out drop========")
day = 17
while day <= 29:
    # result = "alter table mod_gprs_day_out add partition(datetime='202002%s');"%day;
    result = "alter table mod_gprs_mon_out drop partition(datetime='2020%s');" % day;
    print(result)
    day = day +1

print("==============")
day = 17
while day <= 29:
    # result = "hadoop fs -cp /NS2/DATA/small_unit/gprs/day_out/202002%s/SS301PD51202002%s.0001 /NS3/user/hive/warehouse/unicom_all_common.db/mod_gprs_day_out/datetime=202002%s;"%(day,day,day)
    # result = "hadoop fs -ls  /NS3/user/hive/warehouse/unicom_all_common.db/mod_gprs_day_out/datetime=202002%s;"%(day)
    # 删除目录与目录下所有文件
    result = "hadoop fs -rm -r /NS3/user/hive/warehouse/unicom_all_common.db/mod_gprs_mon_out/datetime=2020%s;" % (day)
    print(result + '\n')
    day = day +1

print("=================")
iqflow = 134619000733.66481 / 10 ** 6
print(iqflow)
iq29flow = 3649578696.84085 / 10 ** 6
print(iq29flow)

print("====================")

day = 1
while day <= 29 :
    if day < 10:
        day = "0%s"%day
    result = "select sum(ROAM_STREAM_02) ROAM_STREAM%s from dc_cust_data.DWU_GS_202002%s;"%(day,day)
    print(result + '\n')
    day = int(day) + 1

print("================")
float_sum = 160920338586499328 / 1024**4
print(float_sum)

myflow = 9.229381e+06 * 1.487139e+04 / 1024 ** 2
print("flow num: %s" %myflow)
num = (3.3444745747983892E18 / 10 **4)
print(num)

print("===============")
aa=3.956909e+07 * 5.440585e+03 / 10 ** 6
print(aa)

aa1=3.956909e+07*5.174640e+03/10 ** 6
print(aa1)



patio = 92502986/10**4
print(patio)

avg =208713325649/32791342/100
predict = 5.174640e+03/100
ratio  = (avg -predict) /predict
total = predict * 3.956909e+07
print("avg:%s,predict:%s"%(avg,predict))
print(ratio)
print("total: %s"%total)

ratio = 229173438034

print(ratio)

money = 231450856418/1e+6
print(money)

# 1月23.28
22.26 + 23.28

print("=============")

# 1月y的情况
result = 1.651345e+07 * 8.353507e+09 / 1024 ** 4
print("1月y的情况:%s"%result)
result1 = 16513447*7130492963.585551 / 1024 ** 4
print("1月y的预测情况:%s"%result1)
# 1月x的情况
result2 = 1.651345e+07 * 5.897760e+09 / 1024**4
print("1月x的情况:%s" %result2)
ratio = (result - result1) / result1
print("1月预测误差百分比：%s"%ratio)


# 2月y的情况
result = 1.408627e+07 * 1.142392e+10 / 1024 ** 4
print("2月y的情况:%s"%result)
result1 = 14086268*11785850198.835596 / 1024 ** 4
print("2月y的预测情况:%s"%result1)
# 2月x的情况
result2 = 1.408627e+07 * 9.748290e+09 / 1024**4
print("2月x的情况:%s" %result2)

ratio =  (150993.07757614178-146356.2708326208) /146356.2708326208
print("2月预测误差百分比：%s"%ratio)

mse = 2.5142609345304486e+19/1.2346813442026936e+19
print(mse)

ratio = (219034289066 - 219009506916) / 219009506916
print("2月iq出账实收月指标和日志表差额：%s"%ratio)

ratio = (231450856418-229173438034) / 229173438034
print("1月iq出账实收月指标和日志表差额：%s"%ratio)

ratio = (227318441232-217442299168)/217442299168
print("12月iq出账实收月指标和日志表差额：%s"%ratio)

ratio = (229146288983 - 219757786548) / 219757786548
print("11月iq出账实收月指标和日志表差额：%s"%ratio)

print(10408015*13009776263.98988/1024**4)
a = 1.651345e+07*8.353507e+09/1024**4
b= 1.651345e+07*5.897760e+09/1024**4
print((b-a)/b)
print(149790408687/10**10)
