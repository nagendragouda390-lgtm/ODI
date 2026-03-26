# modules 

import matplotlib.pyplot as plt

import random 

# chances for a ball

ch = [0,1,2,3,4,6,'w']

# variables like runs wickets over and stats

team1_run = 0
team1_wicket = 0
wicket_run1 = []
wicket_ball1 = []
run_graph1 = [0]
ball_graph1 = [0]
team2_run = 0
team2_wicket = 0
wicket_run2 = []
wicket_ball2 = []
run_graph2 = [0]
ball_graph2 = [0]
target_run = [0] 
target_over = [0]

# ball by ball simulation of England batting 

for i in range(1,301):
    if i > 270:
        prob = [40,20,10,5,20,20,10]
    elif i <61:
        prob = [80,30,1,0.5,20,15,5]
    else:
        prob=[70,80,10,3,5,2,5]
    if team1_wicket > 7:
        prob = [0.6,0.6,0.1,0.01,0.02,0.01,0.7]
    run1 = random.choices(ch,prob)[0]
    
    if run1 =='w':
        wicket_run1.append(team1_run)
        wicket_ball1.append(i/6)
        team1_wicket += 1
        run_graph1.append(team1_run)
        ball_graph1.append(i/6)
    else:
        team1_run += run1
        run_graph1.append(team1_run)
        ball_graph1.append(i/6)
    if team1_wicket == 10:
        break 
    
# ball by ball simulation of New Zealand batting 

for k in range(1,301):
   
    if k > 270:
        prob = [40,20,10,5,20,20,10]
    elif k <61:
        prob = [80,30,1,0.5,20,15,5]
    else:
        prob=[70,80,10,3,5,2,5]
    if team2_wicket > 7:
        prob = [0.6,0.6,0.1,0.01,0.02,0.01,0.7]
    run2 = random.choices(ch,prob)[0]
        
    if run2 =='w':
        wicket_run2.append(team2_run)
        wicket_ball2.append(k/6)
        team2_wicket += 1
    else:
        team2_run += run2
        run_graph2.append(team2_run)
        ball_graph2.append(k/6)
    if k == 150:
         wicket = team2_wicket
    if team2_wicket == 10 or team2_run > team1_run:
        break
    
# Target graph or line
       
for j in range(0,51):
    rr = (team1_run+1) *j / 50
    target_run.append(rr)
    target_over.append(j)

# To show in graph (England)

plt.plot(ball_graph1,run_graph1,color = 'red',label = f' ENGLAND       : {team1_run}-{team1_wicket}({i//6}.{i%6})')

# To show New Zealand batting graph 

plt.plot(ball_graph2,run_graph2,color = 'black',label = f' NEW ZEALAND : {team2_run}-{team2_wicket}({k//6}.{k%6})')

# New Zealand runs after halfway stage 

if k > 150:
    plt.text(25,run_graph2[150],f'                      NZ after 25 :  {run_graph2[150]}-{wicket}')

# Target line in graph 

plt.plot(target_over,target_run, linestyle = '--',color = 'green')

# Wickets of England 

plt.scatter(wicket_ball1,wicket_run1,marker ='o',color = 'blue')

# Wickets of New Zealand 

plt.scatter(wicket_ball2,wicket_run2,marker ='o',color = 'grey')

# Result 

if team1_run > team2_run:
    plt.text(20,0,f'Result:', color='brown')
    plt.text(25,-5,f' ENGLAND  won the match by {team1_run - team2_run} runs')
elif team2_run > team1_run:
    plt.text(2,0,f'Result:', color='brown')
    plt.text(5,-5,f' NEW ZEALAND won the match by {10-team2_wicket} wickets {300-k} balls remaining ')
else:
    plt.text(20,0,f'Result:', color='brown')
    plt.text(25,-5,f' Match tied ')

# scale of graph 

plt.xticks([0,5,10,15,20,25,30,35,40,45,50])
plt.yticks([0,30,60,90,120,150,180,210,240,270,300,330,360,390])


plt.legend() 
plt.grid()    
plt.show()  

