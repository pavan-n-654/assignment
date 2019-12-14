import pandas as pd

df=pd.read_csv('election_data_1.csv')
a=df['Voter ID'].count()
print('election results of data_1 are')
print('total number of votes:',a)

b=df['Candidate'].unique()
print('unique candidates:',b)

dic={'Vestal':df["Voter ID"][df['Candidate']=='Vestal'].count(),
'Torres':df["Voter ID"][df['Candidate']=='Torres'].count(),
'Seth':df["Voter ID"][df['Candidate']=='Seth'].count(),
'Cordin':df["Voter ID"][df['Candidate']=='Cordin'].count()}
print('Vestal got',dic['Vestal'],'votes','\n'
      'Torres got',dic['Torres'],'votes','\n'
      'Seth got',dic['Seth'],'votes','\n'
      'Cordin got',dic['Cordin'],'votes')

print('winner is',max(dic))

#updating details to file
f=open('election_results_1','w')
print('election results of data_1 are',file=f)
print('total number of votes:',a,file=f)
print('unique candidates:',b,file=f)
print('Vestal got',dic['Vestal'],'votes','\n'
      'Torres got',dic['Torres'],'votes','\n'
      'Seth got',dic['Seth'],'votes','\n'
      'Cordin got',dic['Cordin'],'votes',file=f)
print('winner is',max(dic),file=f)
f.close()
