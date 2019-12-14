import pandas as pd

df=pd.read_csv('election_data_2.csv')
a=df['Voter ID'].count()
print('election results of data_2 are')
print('total number of votes:',a)

b=df['Candidate'].unique()
print('unique candidates:',b)

dic1={"Khan":df["Voter ID"][df['Candidate']=='Khan'].count(),
"Correy":df["Voter ID"][df['Candidate']=='Correy'].count(),
"O'Tooley":df["Voter ID"][df['Candidate']=="O'Tooley"].count(),
"Li":df["Voter ID"][df['Candidate']=='Li'].count()}
print('Khan got',dic1["Khan"],'votes','\n'
      'Correy got',dic1["Correy"],'votes','\n'
      "O'Tooley got",dic1["O'Tooley"],'votes','\n'
      "Li got",dic1["Li"],'votes')
a=''
b=0
for i in dic1:
    if dic1[i]>=b:
        a=i
        b=dic1[i]
        
print('winner is',a)    


#uploading details to file
f=open('election_results_2','w')
print('election results of data_2 are',file=f)
print('total number of votes:',a,file=f)
print('unique candidates:',b,file=f)

print('Khan got',dic1['Khan'],'votes','\n'
      'Correy got',dic1['Correy'],'votes','\n'
      "O'Tooley got",dic1["O'Tooley"],'votes','\n'
      'Li got',dic1['Li'],'votes',file=f)
print('winner is',a,file=f)

f.close()
