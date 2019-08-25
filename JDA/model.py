import pandas as pd
import numpy as np
import math
import time
from sklearn import linear_model

locations = []

df = pd.read_csv("input_data_train.csv")

#------fill missing values of price------
median_price = math.floor(df.price.median())
print(median_price)
print(df)
df.price = df.price.fillna(median_price)
print(df)

#------replace events with binary value------
df.event = df.event.fillna(0)
print(df)
df.loc[df['event'] != 0,'event'] = 1
print("tabla con eventos en booleano")
print(df)

#------replace location with weights------
#print("frecuencia de valores")
#locationcat = df.location.value_counts()
#locationcat = locationcat.index.tolist()
#print(locationcat)
#for id_l in locations:
    #df.loc[df['location'] == id_l,'location'] == locations.index(id_l)
print("Prices mean per category:")
prices_mean_category = df.groupby('location').mean()['price']
print(prices_mean_category)
#category_weight = sales_mean_category.to_dict()
#print(category_weight)
category_weight = prices_mean_category.sort_values().round()
print("Categorías ordenadas por promedio de ventas")
print(category_weight)
category_weight_d = category_weight.to_dict()
print(category_weight_d)
for element_category in category_weight_d:
    df.loc[df['location'] == element_category,'location'] = category_weight_d.get(element_category)
print("location to average of the category:")
print(df)

#------replace date to day of the week------
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.day_name()
days={"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
print("Fecha cambiada a dia de la semana str:")
print(df)
## changes days from string to day of the week by iterating over dictionary
for weekdaystr in days:
    df.loc[df['date'] == weekdaystr,'date'] = days.get(weekdaystr)
print("Fecha cambiada a dia de la semana int:")
print(df)

#data_mean = df.groupby('location').mean()
#print("Promedio datos")
#print(data_mean)



#------ Modify input csv ------
print("INICIANDO PROCESO CON INPUT DATA")
df2 = pd.read_csv("input_data_pred.csv")
df2o = pd.read_csv("input_data_pred.csv")
#------fill missing values of price------
median_price = math.floor(df2.price.median())
print(median_price)
print(df2)
df2.price = df2.price.fillna(median_price)
print(df2)

#------replace events with binary value------
df2.event = df2.event.fillna(0)
print(df2)
df2.loc[df2['event'] != 0,'event'] = 1
print("tabla con eventos en booleano")
print(df2)

#------replace location with weights------
#print("frecuencia de valores")
#locationcat = df.location.value_counts()
#locationcat = locationcat.index.tolist()
#print(locationcat)
#for id_l in locations:
    #df.loc[df['location'] == id_l,'location'] == locations.index(id_l)
print("Prices mean per category:")
prices_mean_category = df2.groupby('location').mean()['price']
print(prices_mean_category)
#category_weight = sales_mean_category.to_dict()
#print(category_weight)
category_weight = prices_mean_category.sort_values().round()
print("Categorías ordenadas por promedio de ventas")
print(category_weight)
category_weight_d = category_weight.to_dict()
print(category_weight_d)
for element_category in category_weight_d:
    df2.loc[df2['location'] == element_category,'location'] = category_weight_d.get(element_category)
print("location to average of the category:")
print(df2)

#------replace date to day of the week------
df2['date'] = pd.to_datetime(df2['date'])
df2['date'] = df2['date'].dt.day_name()
days={"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
print("Fecha cambiada a dia de la semana str:")
print(df2)
## changes days from string to day of the week by iterating over dictionary
for weekdaystr in days:
    df2.loc[df2['date'] == weekdaystr,'date'] = days.get(weekdaystr)
print("Fecha cambiada a dia de la semana int:")
print(df2)

#data_mean = df.groupby('location').mean()
#print("Promedio datos")
#print(data_mean)

#array_data = np.asarray(df2)
array_data = df2.as_matrix()
print(array_data)

#------Regression------
reg = linear_model.LinearRegression()
reg.fit(df[['location','product','date','temp_mean','sunshine_quant','event','price']],df.sa_quantity)

#Model implementation
print("Coeficiente de la regresion")
print(reg.coef_)
print(reg.intercept_)

prediction_values = []

def sendvalues():
    i = 0;
    while i < 184:
        query = np.array([array_data[i][0],array_data[i][1],array_data[i][2],array_data[i][3],array_data[i][6],array_data[i][7],array_data[i][8]])
        query = query.reshape(1,-1)
        #print(reg.predict(query))
        prediction_values.append(reg.predict(query)[0])
        i += 1

sendvalues()    
df2o['sa_quantity'] = pd.Series(prediction_values)
#df2o.insert(3,"sa_quantity",prediction_values,True)
print(df2o)
df2o.to_csv(r'.\Predicted_sales.csv')
print("Done")

#Model output
#print("Prediccion 1:")
#print(reg.predict([[1,10.635,56,1,1.48]]))#5
#print("Prediccion 2:")
#print(reg.predict([[41,12.275,219,1,2.085714286]]))#7
#print("Prediccion 3:")
#print(reg.predict([[63,13.305,603,0,3.247058824]]))#17
#print("Prediccion 4:")
#print(reg.predict([[136,0.83,350,0,2.492307692]]))  #13
