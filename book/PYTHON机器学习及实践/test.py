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
print("==============")
day = 17
while day <= 29:
    result = "alter table mod_gprs_day_out add partition(datetime='202002%s');"%day;
    print(result)
    day = day +1

print("==============")
day = 17
while day <= 29:
    # result = "hadoop fs -cp /NS2/DATA/small_unit/gprs/day_out/202002%s/SS301PD51202002%s.0001 /NS3/user/hive/warehouse/unicom_all_common.db/mod_gprs_day_out/datetime=202002%s;"%(day,day,day)
    # result = "hadoop fs -ls  /NS3/user/hive/warehouse/unicom_all_common.db/mod_gprs_day_out/datetime=202002%s;"%(day)
    # 删除目录与目录下所有文件
    result = "hadoop fs -rm -r /NS3/user/hive/warehouse/unicom_all_common.db/mod_gprs_mon_out/datetime=2020%s;" %(day)
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


result = (22.26*10**4-204755.8)/204755.8
print(result)

print(24/31)