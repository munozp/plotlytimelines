# PlotlyTimelines
A simple python script to create timelines visualizations with plotly

Requirements:
- python 3.x
- plotly
- web browser

Usage:
python plotlytimelines.py timelineA,action1,start,duration,color;timelineB,action2,start,duration,color... outfile

Colors use hexadecimal format (e.g. A9C308, no '#' symbol)
Example:
Output filename is also used as chart title

python plotlytimelines.py UGV,Go-Vt[100-600],0,180.2776,8FEC71;UGV,Wait,180.2776,4,9E9FE8;UGV,Go-Vl[204-600],184.2776,104.7919,8FEC71;UGV,Wait,289.0695,42.0785,9E9FE8;UGV,Go-Vt[248-600],331.148,43.609,8FEC71;UGV,Wait,374.757,5,9E9FE8;UGV,Go-Vl[300-600],379.757,51.599,8FEC71;UGV,Wait,431.3561,96.6229,9E9FE8;UGV,Go-Vi[200-450],527.9789,180.2776,8FEC71;UAV-1,Idle,0,708.2565,DEF4FB;UAV-2,Idle,0,180.2776,DEF4FB;UAV-2,Take-Off,180.2776,4,00D0A3;UAV-2,FlyTo-[150-640],184.2776,64.0312,2ECDEA;UAV-2,Delivery,248.3088,5,E4DB28;UAV-2,Fly-[204-600],253.3088,67.8392,2ECDEA;UAV-2,Land-Vl-[204-600],321.148,10,E9B11B;UAV-2,Charging,331.148,43.609,A81500;UAV-2,Take-Off,374.757,4,00D0A3;UAV-2,FlyTo-[260-660],378.757,61.1109,2ECDEA;UAV-2,Delivery,439.8679,5,E4DB28;UAV-2,Fly-[300-600],444.8679,72.111,2ECDEA;UAV-2,Land-Vl-[300-600],516.9789,11,E9B11B,;UAV-2,Charging,527.9789,152.2219,A81500;UAV-2,Idle,680.2008,28.0557,DEF4FB plotlytimelinesTest
