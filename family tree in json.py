import json
from functools import reduce
import numpy as np
a={
    "lineage": {
        "FamilyTree": "Some Family Tree",
        "Members": [
            {
                "Name": "First-",
                "BirthYear": "1221",
                "DeathYear": "1264",
                "Members": [
                    {
                        "Name": "Second-",
                        "BirthYear": "1245",
                        "DeathYear": "1300",
                        "Members": [
                            {
                                "Name": "Third-",
                                "BirthYear": "1270",
                                "DeathYear": "1333"
                            },
                            {
                                "Name": "Third--",
                                "BirthYear": "1272",
                                "DeathYear": "1300"
                            },
                            {
                                "Name": "Third--",
                                "BirthYear": "1272",
                                "DeathYear": "1340"
                            },
                            {
                                "Name": "Third---",
                                "BirthYear": "1274",
                                "DeathYear": "1343"
                            }
                        ]
                    },
                    {
                        "Name": "Second--",
                        "BirthYear": "1248",
                        "DeathYear": "1310",
                        "Members": [
                            {
                                "Name": "Third-/",
                                "BirthYear": "1274",
                                "DeathYear": "1330"
                            },
                            {
                                "Name": "Third-//",
                                "BirthYear": "1276",
                                "DeathYear": "1312"
                            },
                            {
                                "Name": "Third-///",
                                "BirthYear": "1276",
                                "DeathYear": "1344"
                            },
                            {
                                "Name": "Third-////",
                                "BirthYear": "1278",
                                "DeathYear": "1352"
                            },
                            {
                                "Name": "Third-/////",
                                "BirthYear": "1278",
                                "DeathYear": "1268"
                            }
                        ]
                    }
                ]
            },
            {
                "Name": "First--",
                "BirthYear": "1212",
                "DeathYear": "1260",
                "Members": [
                    {
                        "Name": "Second+",
                        "BirthYear": "1243",
                        "DeathYear": "1312"
                    },
                    {
                        "Name": "Second++",
                        "BirthYear": "1245",
                        "DeathYear": "1274",
                        "Members": [
                            {
                                "Name": "Third+/",
                                "BirthYear": "1274",
                                "DeathYear": "1330"
                            },
                            {
                                "Name": "Third+//",
                                "BirthYear": "1276",
                                "DeathYear": "1312"
                            },
                            {
                                "Name": "Third+///",
                                "BirthYear": "1250",
                                "DeathYear": "1344"
                            },
                            {
                                "Name": "Third+////",
                                "BirthYear": "1278",
                                "DeathYear": "1352"
                            }
                        ]
                    },
                    {
                        "Name": "Second++",
                        "BirthYear": "1243",
                        "DeathYear": "1260"
                    }
                ]
            }
        ]
    }
}
s1 = json.dumps(a)
y = json.loads(s1)
strs=''
all_ages=[]
maname=''
minm_name=''
maxm_age=0
minm_age=1000000
family_lines=[]
mins_name=[]
maxs_name=[]
mins_count=float('inf')
maxs_count=0

#Invalid Nodes and its reasons
def invalid_nodes(year,members):
        strs=set()
        global end_age
        global maxm_age
        global maname
        global minm_age
        global minm_name
        global all_ages
        
        end_age=0
        for idx,each in enumerate(members):
            if each['BirthYear'] < year:
                    print('-------------------------INVALID NODES AND ITS REASON----------------------')
                    print(each['Name'] +' is invalid as ' +each['BirthYear']+' is less than '+year+'\n')
                    del members[idx]
                    del each
            try:
                strs.add(each['Name']+', ')
                if int(each['DeathYear'])>int(each['BirthYear']):
                        all_ages.append([each['Name'],str(int(each['DeathYear'])-int(each['BirthYear']))] )
                if int(each['DeathYear'])> end_age:
                    end_age=int(each['DeathYear'])
                
                if 'Members' in each:
                    if int(int(each['DeathYear'])-int(each['BirthYear'])) > maxm_age:
                        maname=str(each['Name'])
                        maxm_age=int(int(each['DeathYear'])-int(each['BirthYear']))
                    if (int(each['DeathYear'])-int(each['BirthYear'])) < minm_age:
                        minm_name=str(each['Name'])
                        minm_age=int(int(each['DeathYear'])-int(each['BirthYear']))  
                    invalid_nodes(each['BirthYear'],each['Members'])
            except:
                pass
           
        if strs!='':
                family_lines.append(["".join(strs)])

invalid_nodes(y['lineage']['Members'][0]['BirthYear'],y['lineage']['Members'])
print('---------------------FAMILY LINE---------------')
for each in family_lines:
        fam=''
        if len(each)>maxs_count:
                maxs_count=len(each)
                maxs_name=each
        if len(each)<mins_count:
                mins_count=len(each)
                mins_name=each        
        for i in each:
                fam+=i+','
        print("Each family name in individual family lines :"+fam)
        
print('-------SHORTEST FAMILY LINE BASED ON LEAST NUMBER OF MEMBERS IN FAMILY LINE-------')
print("The Shortest Family line based on number of Member in Family Line :"+str(mins_name)+'\n')

print('----------LONGEST FAMILY LINE BASED ON HIGHEST NUMBER OF MEMBERS IN FAMILY LINE----')
print("The Longest Family line based on highest number of Member in Family Line :"+str(maxs_name)+'\n')

print('-----------------------ALL FAMILY MEMBERS WITH CORRESPONDING AGE------------------')
all_ages.sort(key = lambda x: x[1])
print(all_ages)
            
start_age=int(y['lineage']['Members'][0]['BirthYear'])              
    
print('------------------RANGE OF LINEGAE------------')
print(str(end_age - start_age)+'\n')
age_num=[int(each[1]) for each in all_ages]

print('------------------MEAN AGE FOR THIS LINEAGE-----------')

print(np.mean(age_num))
print('-----------------MEDIAN AGE FOR LINEGAE ---------')
print(np.median(age_num))
print('-----------------IQR----------------------')
v1 = np.percentile(age_num, 50, interpolation='midpoint')
v2 = np.percentile(age_num, 50, interpolation='midpoint')
print(v2 - v1)
print('-----------------LONGEST AND YOUNGES --------------')
print('The name '+maname+' and maxm age is : '+str(maxm_age))
print('The name '+minm_name+' and minm age is : '+str(minm_age))


