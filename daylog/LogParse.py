#coding=utf-8
__author__ = 'paul'
from pyspark import SparkContext
from parse_utils import *
from operator import add
import os


pf1 = os.path.dirname(__file__)+"/parse_utils.py"
sc = SparkContext("spark://dev1:7077", "daylog", pyFiles=[pf1])
rdd1=sc.textFile("/Users/paul/dw/106/2013/12/dm2011_hangzhou-access_log.2013.12.17.19.59.log.gz")
rdd2=sc.textFile("/Users/paul/dw/116/2013/12/dm2011_hangzhou-access_log.2013.12.17.19.59.log.gz")
rdd = rdd1.union(rdd2)
pv=rdd.count()

urlRdd=rdd.map(lambda line: (get_req_url(line),get_refer_url(line)))

threadRdd = urlRdd.filter(lambda (req,ref): getUrlType(req)=="thread")
wapRdd = urlRdd.filter(lambda (req,ref): getUrlType(req)=="wap")

#帖子也页面PV
threadPv = threadRdd.count()
wapPv =  wapRdd.count()

tfRefTypeResult = threadRdd.map(lambda (req,ref): (getUrlType(ref),1)).reduceByKey(add).collect()

for type,count in tfRefTypeResult:
    print type ,": ",count

print "thread pv:", threadPv
print "total pv: ", pv
