import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
def data_miner(**data):
    url = fr'https://www.siam.in/statistics.aspx?mpgid=8&pgidtrail='
    for geo,val in data.items():
        table = pd.read_html(url+val)
        df = table[0]
        df.set_index('Category', inplace=True)
        df = df.transpose()
        print(df)
        df.drop('Grand Total', axis=1, inplace=True)
        df.plot.bar(stacked=True, title=f'{geo} Sales', xlabel='Years', ylabel='Number of Vehicles')
    plt.show()
    return None
data_miner(Domestic='14',Export='15')