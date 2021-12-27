s = '0981234567; 0917654321;10:18:25;75'
dt1,dt2,s,t = [i.strip() for i in s.split(';')]
cuoc_thue_bao = int(t)/60 * 2500
print(cuoc_thue_bao)