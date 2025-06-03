import sys
sys.path.append(r"D:\Imp Projects\NIDS_Project")
from src.config import Config
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

df = pd.read_csv(os.path.join(Config.DATA_PATH, Config.TRAIN_DATA))

print(df.shape)
print(df.head())
print(df.isna().sum())

print(df.isin([np.inf, -np.inf]).sum())

df.replace([np.inf, -np.inf], np.nan, inplace=True)

print(df.isna().sum())


#df['Label'].value_counts(), df['Attack'].value_counts()


list_dropped = ['Label', 'Attack','IPV4_SRC_ADDR','IPV4_DST_ADDR','OUT_PKTS','SRC_TO_DST_SECOND_BYTES','NUM_PKTS_UP_TO_128_BYTES',
 'FLOW_START_MILLISECONDS','FLOW_END_MILLISECONDS','PROTOCOL','IN_PKTS','OUT_BYTES','TCP_FLAGS','CLIENT_TCP_FLAGS','SERVER_TCP_FLAGS',
 'FLOW_DURATION_MILLISECONDS','DURATION_IN','SHORTEST_FLOW_PKT','MIN_IP_PKT_LEN','DST_TO_SRC_SECOND_BYTES','RETRANSMITTED_IN_BYTES',
 'RETRANSMITTED_IN_PKTS','RETRANSMITTED_OUT_BYTES','RETRANSMITTED_OUT_PKTS','DST_TO_SRC_AVG_THROUGHPUT','NUM_PKTS_128_TO_256_BYTES',
 'NUM_PKTS_256_TO_512_BYTES','NUM_PKTS_512_TO_1024_BYTES','NUM_PKTS_1024_TO_1514_BYTES','TCP_WIN_MAX_IN','TCP_WIN_MAX_OUT',
 'ICMP_TYPE','DNS_QUERY_ID','DNS_TTL_ANSWER','FTP_COMMAND_RET_CODE','SRC_TO_DST_IAT_MIN','SRC_TO_DST_IAT_MAX','SRC_TO_DST_IAT_AVG',
 'SRC_TO_DST_IAT_STDDEV','DST_TO_SRC_IAT_MIN','DST_TO_SRC_IAT_MAX','DST_TO_SRC_IAT_AVG','DST_TO_SRC_IAT_STDDEV', 'MAX_IP_PKT_LEN']

X = df.drop(columns=list_dropped, axis=1)
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.1, shuffle=True, random_state=Config.RANDOM_STATE)
#print(X_train.columns)

fff = pd.concat([X_test, y_test], axis=1)
print(fff[fff['Label'] == 1].iloc[0])
print(fff[fff['Label'] == 1].iloc[10])
print(fff[fff['Label'] == 0].iloc[0])