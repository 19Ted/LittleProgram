import numpy as np
import pandas as pd
import supporto1
import supporto2
kera=supporto1.Cani()
kera.nome="Kera"
kera.età=11
kera.razza="bastarda"

print(kera.descrive())

cosa={"country" : ["Italia","Francia","Germania","Spagna"],
       "capitale" : ["Roma","Parigi","Berlino","Madrid"],
       "popolazione" : ["60mil","100mil","130mil","150mil"]
       }   
mattone=pd.DataFrame(cosa)
mattone.index=["IT","FR","GR","SP"]

print(mattone.loc[["FR","IT","SP"]])

