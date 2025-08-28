from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession.builder \
    .appName("sparkapp") \
    .getOrCreate()
data=[(1,'kiran',5000,'IT'),(2,'rahul',6000,'Dev'),(3,'rajendra',7000,'devops')]
schema=['id','name','salary','dept']
df=spark.createDataFrame(data,schema)
df.show()