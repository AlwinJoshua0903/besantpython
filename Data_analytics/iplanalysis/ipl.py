import pandas as pd
iplball_DF=pd.read_csv(r'C:\Users\ALWIN JOSHUA\PycharmProjects\pythonProject\Data_analytics\iplanalysis\ipl_ball_by_ball_2008_2022.csv')
iplmatches_DF=pd.read_csv(r'C:\Users\ALWIN JOSHUA\PycharmProjects\pythonProject\Data_analytics\iplanalysis\ipl_matches_2008_2022.csv')
'''
print(iplmatches_DF.shape)
print(iplball_DF.shape)
print(iplmatches_DF.columns)
print(iplball_DF.columns)
chennai_matches=iplmatches_DF.loc[iplmatches_DF['city']=='Chennai']
print(chennai_matches)
chennai_matches.to_csv('Chennai_Matchlist.csv',index=True,sep=';')
chennai_winning_matches=iplmatches_DF.loc[(iplmatches_DF['city']=='Chennai')&(iplmatches_DF['winning_team']=='Chennai Super Kings')]
print(chennai_winning_matches)
chennai_winning_matches.to_csv('Chennai_Winning_Matchlist.csv',index=True,sep=';')
mumbai_winning_matches=iplmatches_DF.loc[(iplmatches_DF['city']=='Chennai')&(iplmatches_DF['winning_team']=='Mumbai Indians')]
print(mumbai_winning_matches)
mumbai_winning_matches.to_csv('Mumbai_Winning_Matchlist.csv',index=True,sep=';')

chennai_winning_first=iplmatches_DF.loc[(iplmatches_DF['city']=='Chennai')&(iplmatches_DF['winning_team']=='Chennai Super Kings')&(iplmatches_DF['toss_decision']=='bat')]
print(chennai_winning_first)
chennai_winning_first.to_csv('chennai_Winning_Batfirst.csv',index=True,sep=';')
'''
A=[[1,'A',80],[2,'B',90],[3,'C',10],[4,'D','']]
D=[[10,'IT'],[20,'CSE'],[30,'MECH'],[40,'AUTO'],[50,'ECE']]
o=pd.DataFrame(A,columns=['No','Name','Dep_id'])
p=pd.DataFrame(D,columns=['Dep_id','Dep_name'])
print(o)
print(p)
output=pd.merge(o,p,on='Dep_id',how='inner')
print(output)
output1=pd.merge(o,p,on='Dep_id',how='left')
print(output1)
output2=pd.merge(p,o,on='Dep_id',how='left')
print(output2)