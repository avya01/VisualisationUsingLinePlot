import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Day" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Birth_Rate" : [10, 12, 16, 9, 7]
}

df_July = pd.DataFrame(data)
 
plt.plot(df_July.Day, df_July.Birth_Rate, marker="o", linewidth=1, color="green", linestyle="dashed")
plt.xlabel("Day")
plt.ylabel("Birth Rate")
plt.title("Birth Rate VS Day")
plt.show()

data2 = {
    "Day" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Birth_Rate" : [5, 18, 4, 7, 9]
}

df_August = pd.DataFrame(data2)

plt.plot(df_August.Day, df_August.Birth_Rate, marker="o", linewidth=1, color="blue", linestyle="dashed")
plt.xlabel("Day")
plt.ylabel("Birth Rate")
plt.title("Birth Rate VS Day")
plt.show()

plt.plot(df_July.Day, df_July.Birth_Rate, marker="o", linewidth=1, color="blue", linestyle="dashed")
plt.plot(df_August.Day, df_August.Birth_Rate, marker="o", linewidth=1, color="green", linestyle="dashed")
plt.xlabel("Day")
plt.ylabel("Birth Rate")
plt.title("Birth Rate VS Day")
plt.legend()
plt.show()