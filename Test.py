import pandas as pd

df = pd.read_csv("DataPenduduk.csv")

# df.sort_values(["Nama"], axis=0, ascending=[False], inplace=True)

sorted_df = df.sort_values(by=["Nama"], ascending=True)
# sorted_df.to_csv('Penduduk.csv', index=False)

print(sorted_df)


# print("\nBefore sorting:")
# print(csvData)

# csvData.sort_values(["Nama", "Umur", "Alamat"], 
#                     axis=0,
#                     ascending=[True, True, True], 
#                     inplace=True)

# print("\nAfter sorting:")
# print(csvData)