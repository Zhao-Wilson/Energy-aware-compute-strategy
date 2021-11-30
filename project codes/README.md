### Every module meaning

1. mainFunc.py :   
  Draw Figure5,6,7,8 from the report

2. dp.py :   
This module builds up the dynaymic programming table
The procedure consists of sorting Energy cost and building table
In order to test the module function, I provide two methods generating
original data(Bandwidth & Energy arr)
   - randomly generate data table using from generateNodes import generate_table()
   - handwritten data table shown below

3. randomSelect.py :  
This module use random strategy to find relationship between number of nodes and Energy cost
as well as number of nodes and bandwidth

4. roundrobinSelect.py :  
This module use roundrobin strategy to find relationship between number of nodes and Energy cost
as well as number of nodes and bandwidth

5. localFirstSelect.py :    
This module use localfirst strategy to find relationship between number of nodes and Energy cost
as well as number of nodes and bandwidth

6. search_DP.py :    
Search for the optimal strategy given energy limit

7. generateNodes.py :   
This module provides a public function to randomly generate original
Energy array and Bandwidth array

8. load_time.py :   
This module calculates how much time need to spend in order to handle specific 
workload of 50 GBytes based on different strategy with different optimal bandwidth

9. systemCondif.py :   
global system config settings

10. table_cal.py :   
This module compare the four strategies with similar bandwidth 
and energy cost to find how many workers need

### How to run the code
1. In the systemConfig.py, set parameters. In my report, I set the original
cluster is six and in each of them there are 15 nodes.

2. Run mainFun.py to get Figure 5,6,7,8 from report (6.2 Simulation results)

3. Run the timeComplexity to get how much time needed to run the code Figure 9,10(6.3 Time complexity)

4. Run load_time.py to calculate time cost of Figure 11(6.4 Task transmission simulation)

5. Run table_cal.py to get the Table.5