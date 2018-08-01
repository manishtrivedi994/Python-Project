def scored(self,list1):
        #Calculates the score of a player irrespective of his designation as batsmen or bowler
        Scored=list1[0]
        Faced=list1[1]
        Fours=list1[2]
        Sixes=list1[3]
        Bowled=list1[4]
        Maiden=list1[5]
        Given=list1[6]
        Wickets=list1[7]
        Catches=list1[8]
        Stumping=list1[9]
        RunOut=list1[10]
        points=(Scored/2)
        if(Scored >= 0 and Scored <50):
                points+=5
        elif(Scored>=50 and Scored<100):
                 points+=5
        else:
                points+=10
        if(Faced==0):
                points+=0
        else:
                if(float(Scored/Faced)*100 >= 0 and float(Scored/Faced)*100 < 80):
                        points+=0
                elif(float(Scored/Faced)*100 >= 80 and float(Scored/Faced)*100 <= 100):
                        points+=2
                else:
                        points+=4
        points+=(Fours*1)
        points+=(Sixes*2)
        points+=(Wickets*10)
        if(Wickets>=0 and Wickets< 3):
                points+=0
        elif(Wickets>=3 and Wickets < 5):
                points+=5
        else:
                points+=10
        if(Bowled==0):
                points+=0
        else:
                if(float(Given/Bowled)>=0 and float(Given/Bowled)<2):
                        points+=10
                elif(float(Given/Bowled)>=2 and float(Given/Bowled)<3.5):
                        points+=7
                else:
                        points+=4
        points+=(Stumping*10)
        points+=(Catches*10)
        points+=(RunOut*10)
        
        
        return points
