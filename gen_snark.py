import pandas as pd
import random


random.seed("Snark")

def roll_dX(X):
 return random.choice(list(range(X)))+1

def roll_NdX(N,X):
 op=0
 for i in range(N):
  op+=roll_dX(X)
 return op



def timeify(mins):
 smins = mins%60
 if smins<10:
  smins = "0"+str(smins)
 else:
  smins = str(smins)
 return str(int(mins/60))+":"+smins+"pm"

def choiceify(d):
 op = []
 for c in d:
  op = op+[c]*d[c]
 return op

def ynify(b):
 if b:
  return "Yes"
 else:
  return "No"

snarks = {

"Vorpal":{
"prevalence":19,
"polytaste":{"Hollow":81,"Haunting":6,"Crumbling":4,"Artless":7,"Meagre":2},
"monotaste":{"Crisp":85,"Blunt":5,"Clear":2,"Bright":4,"Neat":4},
"wakestats":[147,[20, 40, 60]],
"fondness":{"Mild":3,"Moderate":8,"Extreme":89},
"liness":{"Mild":12,"Moderate":80,"Extreme":8},
"phobia":{"Mild":24,"Moderate":71,"Extreme":5},
"boojum":False
},

"Frumious":{
"prevalence":7,
"polytaste":{"Hollow":4,"Haunting":3,"Crumbling":80,"Artless":1,"Meagre":12},
"monotaste":{"Crisp":1,"Blunt":92,"Clear":3,"Bright":3,"Neat":1},
"wakestats":[120,[24, 36, 60]],
"fondness":{"Mild":40,"Moderate":51,"Extreme":9},
"liness":{"Mild":3,"Moderate":95,"Extreme":2},
"phobia":{"Mild":1,"Moderate":3,"Extreme":96},
"boojum":False
},

"Slythy":{
"prevalence":14,
"polytaste":{"Hollow":44,"Haunting":14,"Crumbling":2,"Artless":30,"Meagre":10},
"monotaste":{"Crisp":60,"Blunt":2,"Clear":0,"Bright":1,"Neat":37},
"wakestats":[260,[100, 100, 200]],
"fondness":{"Mild":70,"Moderate":20,"Extreme":10},
"liness":{"Mild":77,"Moderate":22,"Extreme":1},
"phobia":{"Mild":72,"Moderate":18,"Extreme":10},
"boojum":False
},

"Mimsy":{
"prevalence":4,
"polytaste":{"Hollow":8,"Haunting":0,"Crumbling":2,"Artless":42,"Meagre":48},
"monotaste":{"Crisp":9,"Blunt":1,"Clear":12,"Bright":58,"Neat":20},
"wakestats":[250,[100, 20, 120]],
"fondness":{"Mild":1,"Moderate":91,"Extreme":8},
"liness":{"Mild":4,"Moderate":92,"Extreme":4},
"phobia":{"Mild":7,"Moderate":89,"Extreme":4},
"boojum":False
},

"Manxome":{
"prevalence":4,
"polytaste":{"Hollow":50,"Haunting":44,"Crumbling":2,"Artless":1,"Meagre":3},
"monotaste":{"Crisp":9,"Blunt":80,"Clear":8,"Bright":1,"Neat":1},
"wakestats":[171,[4, 6, 10]],
"fondness":{"Mild":98,"Moderate":1,"Extreme":1},
"liness":{"Mild":20,"Moderate":70,"Extreme":10},
"phobia":{"Mild":2,"Moderate":40,"Extreme":58},
"boojum":False
},

"Whiffling":{
"prevalence":6,
"polytaste":{"Hollow":92,"Haunting":3,"Crumbling":3,"Artless":1,"Meagre":1},
"monotaste":{"Crisp":3,"Blunt":1,"Clear":8,"Bright":87,"Neat":1},
"wakestats":[99,[8, 12, 20]],
"fondness":{"Mild":8,"Moderate":18,"Extreme":74},
"liness":{"Mild":98,"Moderate":2,"Extreme":0},
"phobia":{"Mild":2,"Moderate":88,"Extreme":10},
"boojum":False
},

"Burbling":{
"prevalence":8,
"polytaste":{"Hollow":14,"Haunting":5,"Crumbling":1,"Artless":74,"Meagre":6},
"monotaste":{"Crisp":50,"Blunt":0,"Clear":45,"Bright":3,"Neat":2},
"wakestats":[273,[80, 20, 100]],
"fondness":{"Mild":1,"Moderate":19,"Extreme":80},
"liness":{"Mild":32,"Moderate":33,"Extreme":35},
"phobia":{"Mild":8,"Moderate":80,"Extreme":12},
"boojum":False
},

"Uffish":{
"prevalence":7,
"polytaste":{"Hollow":68,"Haunting":10,"Crumbling":11,"Artless":0,"Meagre":11},
"monotaste":{"Crisp":2,"Blunt":10,"Clear":12,"Bright":70,"Neat":6},
"wakestats":[293,[20, 20, 40]],
"fondness":{"Mild":92,"Moderate":7,"Extreme":1},
"liness":{"Mild":44,"Moderate":33,"Extreme":23},
"phobia":{"Mild":40,"Moderate":40,"Extreme":20},
"boojum":False
},

"Gyring":{
"prevalence":10,
"polytaste":{"Hollow":2,"Haunting":13,"Crumbling":1,"Artless":1,"Meagre":83},
"monotaste":{"Crisp":11,"Blunt":0,"Clear":1,"Bright":11,"Neat":77},
"wakestats":[202,[80, 40, 120]],
"fondness":{"Mild":22,"Moderate":80,"Extreme":2},
"liness":{"Mild":19,"Moderate":62,"Extreme":19},
"phobia":{"Mild":12,"Moderate":12,"Extreme":76},
"boojum":False
},

"Gimbling":{
"prevalence":11,
"polytaste":{"Hollow":1,"Haunting":1,"Crumbling":10,"Artless":41,"Meagre":47},
"monotaste":{"Crisp":21,"Blunt":19,"Clear":17,"Bright":21,"Neat":22},
"wakestats":[203,[60, 60, 120]],
"fondness":{"Mild":2,"Moderate":6,"Extreme":92},
"liness":{"Mild":9,"Moderate":82,"Extreme":9},
"phobia":{"Mild":84,"Moderate":14,"Extreme":2},
"boojum":False
},

"Cromulent":{
"prevalence":5,
"polytaste":{"Hollow":44,"Haunting":2,"Crumbling":34,"Artless":8,"Meagre":12},
"monotaste":{"Crisp":3,"Blunt":90,"Clear":1,"Bright":3,"Neat":3},
"wakestats":[241,[80, 80, 160]],
"fondness":{"Mild":21,"Moderate":18,"Extreme":61},
"liness":{"Mild":85,"Moderate":13,"Extreme":2},
"phobia":{"Mild":38,"Moderate":1,"Extreme":61},
"boojum":True
},

"Snippid":{
"prevalence":2,
"polytaste":{"Hollow":18,"Haunting":32,"Crumbling":0,"Artless":0,"Meagre":50},
"monotaste":{"Crisp":6,"Blunt":0,"Clear":77,"Bright":6,"Neat":10},
"wakestats":[164,[60, 40, 100]],
"fondness":{"Mild":12,"Moderate":78,"Extreme":10},
"liness":{"Mild":44,"Moderate":36,"Extreme":20},
"phobia":{"Mild":2,"Moderate":67,"Extreme":31},
"boojum":True
},

"Scrumbling":{
"prevalence":3,
"polytaste":{"Hollow":18,"Haunting":0,"Crumbling":60,"Artless":12,"Meagre":10},
"monotaste":{"Crisp":4,"Blunt":84,"Clear":4,"Bright":4,"Neat":4},
"wakestats":[262,[60, 4, 64]],
"fondness":{"Mild":88,"Moderate":10,"Extreme":2},
"liness":{"Mild":40,"Moderate":53,"Extreme":7},
"phobia":{"Mild":28,"Moderate":70,"Extreme":2},
"boojum":True
}

}

def gen_snark():
 clist = []
 for name in snarks:
  clist = clist + [name]*snarks[name]["prevalence"]
 name = random.choice(clist)
 ptaste, mtaste, taste, wakemins, wake, fond, lin, phob, booj = gen_specific_snark(name)
 return ptaste, mtaste, taste, wakemins, wake, fond, lin, phob, booj, name

def gen_specific_snark(name):
 snark = snarks[name]
 
 ptaste = random.choice(choiceify(snark["polytaste"]))
 mtaste = random.choice(choiceify(snark["monotaste"]))
 taste = ptaste + ", yet " + mtaste
 
 wakemins = snark["wakestats"][0] + roll_dX(snark["wakestats"][1][0]) + roll_dX(snark["wakestats"][1][1]) - roll_dX(snark["wakestats"][1][2])
 wake = timeify(wakemins)
 
 fond = random.choice(choiceify(snark["fondness"]))
 lin = random.choice(choiceify(snark["liness"]))
 phob = random.choice(choiceify(snark["phobia"]))
 
 booj = snark["boojum"]
 
 return ptaste, mtaste, taste, wakemins, wake, fond, lin, phob, booj

#####

ptastes = []
mtastes = []
tastes = []
wakeminses = []
wakes = []
fonds = []
lins = []
phobs = []
hunts = []
boojs = []
names = []

for i in range(141300):
 ptaste, mtaste, taste, wakemins, wake, fond, lin, phob, booj, name = gen_snark()
 ptastes.append(ptaste)
 mtastes.append(mtaste)
 tastes.append(taste)
 wakeminses.append(wakemins)
 wakes.append(wake)
 fonds.append(fond)
 lins.append(lin)
 phobs.append(phob)
 
 #boojs.append(booj)
 
 if random.choice([True]*3+[False]*97) or ((ptaste=="Crumbling") or (mtaste=="Blunt") and random.choice([True]*6+[False])):
  hunts.append("No")
  boojs.append("Unknown")
 else:
  hunts.append("Yes")
  boojs.append(ynify(booj))
 
 names.append(name)

df = pd.DataFrame({"p":ptastes,"m":mtastes, "Taste":tastes,"w":wakeminses,"Waking-Time":wakes,"Fondness for Washing-Machines":fonds, "Cleanliness":lins, "Financial Phobia":phobs, "Hunted?":hunts, "Boojum?":boojs,"n":names})

print(df)
print(df[:141275])
print(df[141275:])


#df.to_csv("data.csv")
df[:141275].to_csv("data.csv")
df[141275:].to_csv("targets.csv")



print(len(df[df["Boojum?"]=="Yes"])/len(df[df["Hunted?"]=="Yes"]))

#####

def p_roll_dX(X):
 op = {}
 for i in range(X):
  op[i+1] = 1.0/X
 return op

def app(dyct,key,val):
 if key in dyct:
  dyct[key]+=val
 else:
  dyct[key]=val
 return dyct

def p_add(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey+bkey, a[akey]*b[bkey])
 return op

def p_subtract(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey-bkey, a[akey]*b[bkey])
 return op
 
def eval_species_probs(ptaste, mtaste, wakemins, fond, lin, phob):
 probs = {}
 for name in snarks:
  wakeyprobs = {snarks[name]["wakestats"][0]:1.0}
  wakeyprobs = p_add(wakeyprobs, p_roll_dX(snarks[name]["wakestats"][1][0]))
  wakeyprobs = p_add(wakeyprobs, p_roll_dX(snarks[name]["wakestats"][1][1]))
  wakeyprobs = p_subtract(wakeyprobs, p_roll_dX(snarks[name]["wakestats"][1][2]))
  
  if wakemins in wakeyprobs:
   wakefactor = wakeyprobs[wakemins]
  else:
   wakefactor = 0
  
  probs[name] = snarks[name]["prevalence"] * snarks[name]["polytaste"][ptaste] * snarks[name]["monotaste"][mtaste] * wakefactor * snarks[name]["fondness"][fond] * snarks[name]["liness"][lin] * snarks[name]["phobia"][phob]
 return probs

def eval_snark_probs(ptaste, mtaste, wakemins, fond, lin, phob):
 sprobs = eval_species_probs(ptaste, mtaste, wakemins, fond, lin, phob)
 Ybooj = sum([sprobs[name] for name in sprobs if snarks[name]["boojum"]==True])
 Nbooj = sum([sprobs[name] for name in sprobs if snarks[name]["boojum"]==False])
 return Ybooj/(Ybooj+Nbooj)
 
 
for c in range(141275, 141300):
 p = df["p"][c]
 m = df["m"][c]
 w = df["w"][c]
 f = df["Fondness for Washing-Machines"][c]
 l = df["Cleanliness"][c]
 ph = df["Financial Phobia"][c]
 
 #print(c)
 #print(df[c:(c+1)])
 #print(eval_species_probs(p,m,w,f,l,ph))
 print(eval_snark_probs(p,m,w,f,l,ph))
 print("-")
