""" from faker import Faker as fk
import os

temp = fk("ko-KR")
print (temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")
with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," +
                temp.address() + "," +
                temp.postcode() + "," +
                temp.company() + "," +
                temp.job() + "," +
                temp.phone_number() + "," +
                temp.email() + "," +
                temp.user_name() + "," +
                temp.ipv4_private() + "," +
                temp.ipv4_public() + "," +
                temp.catch_phrase() + "," +
                temp.color_name() + "\n") """



""" import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)

df["aver"] = df.postcode.rank(method="average")
print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(method="dense")
print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method="min")
print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(method="max")
print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first", "dense", "aver"]])

print(df.transpose())

print(df["postcode"].expanding())
print(df["postcode"].expanding().sum())

print(df.postcode.idxmax(axis=0))
print(df.postcode.idxmin(axis=0))

print(df.empty)

print(df.isin([48742]))
print(df.isin(["장상호"]))
print(df.isin([48742, 12834]))
print(df.isin([48742, 12834,"장상호"]))

# period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
# dt = {"col1":[1,2,3,4,5,6],"col2":period}
# idx = ["row1","row2","row3","row4","row5","row6"]
# pf = pd.DataFrame(data=dt, index=idx)
# print(pf)

# i = pd.date_range("2023-11-10", periods=10, freq="1H")
# df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
# print(df)

# print(df.at_time("09:00"))
# print(df.at_time("03:00"))

# print(df.between_time(start_time="12:00", end_time="00:00"))
# print(df.between_time(start_time="03:00", end_time="09:00"))

# i = pd.date_range("2023-11-10", periods=10, freq="3D")
# i = pd.date_range("2023-11-10", periods=10, freq="5D")
# df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
# print(df)

# print(df.first("3D"))
# print(df.first("7D"))
# print(df.last("7D")) """



""" import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2023")
print(ksp)

print(ksp["High"].max())
print(ksp["High"].idxmax())

print(ksp["Low"].min())
print(ksp["Low"].idxmin())

print(ksp["Volume"].nlargest(n=5))
print(ksp["Close"].nlargest(n=5))

print(ksp["Volume"].nsmallest(n=5))
print(ksp["Close"].nsmallest(n=5))

cond = ksp["Close"] >= 2000
res = ksp[cond].index[0]
print(res)

ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
print(ksp)

ksp["grp"] = ksp["up"] != ksp["up"].shift().cumsum()
print(ksp)

ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp)

print(ksp["up_cnt"].max()) """



""" import pandas as pd

target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")

df.to_csv("./data/apttt.csv", encoding="utf8")

print(df.head()) """



""" import pandas as pd

df= pd.read_csv("./data/apttt.csv", index_col=0)

print(df.head())

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)

# arr = df.to_numpy()
# print(arr)
# print(arr[2])
# print(len(arr))

# print(df.describe())

# print(df.transpose())
# print(df.T.head()) """