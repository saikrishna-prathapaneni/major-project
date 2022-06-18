
import numpy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error



#df.drop(df.loc[df['line_race']==0].index, inplace=True)


#print(data['Median Time at Port'].head())

class Resource:
    def __init__(self,data,port,year):
        self.data = data
        self.port = port
        self.year = year

        self.data.drop(self.data.loc[self.data['Median Waiting time off port limits'] == 'LOW'].index,inplace=True)
        self.data.drop(self.data.loc[self.data['Median Waiting time off port limits'] == 'HIGH'].index,inplace=True)
        self.data.drop(self.data.loc[self.data['Median Waiting time off port limits'] == 'MEDIUM'].index,inplace=True)

        self.data.drop(self.data.loc[self.data['Median Time at Port'] == 'LOW'].index,inplace=True)
        self.data.drop(self.data.loc[self.data['Median Time at Port'] == 'HIGH'].index,inplace=True)
        self.data.drop(self.data.loc[self.data['Median Time at Port'] == 'MEDIUM'].index,inplace=True)
        self.data['Year']=self.data['Year'].astype(int)
        self.data['week']=self.data['week'].astype(int)
        self.data['Median Time at Port']=self.data['Median Time at Port'].astype(str).apply(lambda x:x[:3])
        self.data['Median Waiting time off port limits']=self.data['Median Waiting time off port limits'].astype(str).apply(lambda x:x[:3])

        self.model=self.fit_model()
    def get_scale(self,datase):
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        return self.scaler.fit_transform(datase[['Median Time at Port']])

    def get_plot(self):
        f_data=self.data[['Median Time at Port','Median Waiting time off port limits','Port','Year','week']].where(self.data['Port']==self.port).dropna()
        f_data=f_data.where(self.data['Year']==self.year).dropna().sort_values(by=['week','Median Time at Port'])
        f_data=self.data[['Median Time at Port','Median Waiting time off port limits','Port','Year','week']].where(self.data['Port']==self.port).dropna()
        f_data=f_data.where(self.data['Year']==self.year).dropna().sort_values(by=['week','Median Time at Port'])
        plt.bar(f_data['week'],f_data['Median Time at Port'].astype(float))
        plt.plot(f_data['week'],f_data['Median Time at Port'].astype(float),color="red")
        plt.xlabel('week')
        plt.ylabel('Median time')
        plt.title(self.place+str(int(self.year)))
        
    def fit_model(self):
        # split into train and test sets
        dataset=self.get_scale(self.data)
        train_size = int(len(dataset) * 0.67)
        test_size = len(dataset) - train_size
        train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
        print(len(train), len(test))
        look_back = 1
        trainX, trainY = self.create_dataset(train, look_back)
        testX, testY = self.create_dataset(test, look_back)
        
        trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
        testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
        

        model = Sequential()
        model.add(LSTM(4, input_shape=(1, look_back)))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        with tf.device('/cpu:0'):
    
             model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
        # make predictions
        with tf.device('/cpu:0'): 
            trainPredict = model.predict(trainX)
            testPredict = model.predict(testX)
        # invert predictions
        trainPredict = self.scaler.inverse_transform(trainPredict)
        trainY = self.scaler.inverse_transform([trainY])
        testPredict = self.scaler.inverse_transform(testPredict)
        testY = self.scaler.inverse_transform([testY])
        # calculate root mean squared error
        trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
        print('Train Score: %.2f RMSE' % (trainScore))
        testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
        print('Test Score: %.2f RMSE' % (testScore))
        return model
    def predict(self,input):
        return self.model.predict(np.array([[[input]]]))
             
    def create_dataset(self,dataset, look_back=1):
        dataX=[]
        dataY=[]
    
        for i in range(len(dataset)-look_back-1):
            
            a = dataset[i:(i+look_back), 0]
            dataX.append(a)
            dataY.append(dataset[i + look_back, 0])
        return numpy.array(dataX), numpy.array(dataY)