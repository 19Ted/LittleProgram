import numpy as np
import pandas as pd

cosa={"country" : ["Italia","Francia","Germania","Spagna"],
       "capitale" : ["Roma","Parigi","Berlino","Madrid"],
       "popolazione" : ["60mil","100mil","130mil","150mil"]
       }
mattone=pd.DataFrame(cosa)
mattone.index=["IT","FR","GR","SP"]

print(mattone.loc[["FR","IT","SP"]])