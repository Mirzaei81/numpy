import pandas as pd 
df = pd.read_html("https://en.wikipedia.org/wiki/Transistor_count#Microprocessors")
df[3]["Transistor count"]=df[3]["Transistor count"].apply(lambda x:x.split('[')[0].replace(',',""))
df[3]["Year"]=df[3]["Year"].apply(lambda x:x.split('[')[0].replace(',',""))
df[3]['Transistor count'] = pd.to_numeric(df[3]['Transistor count'], errors='coerce')
df[3] = df[3].dropna()
df[3] = df[3].filter(items=["Year","Transistor count"])
print(df[3])
df[3].to_csv("output.csv")

