# ML-SPES: Machine Learning Based SDN Traffic Management

## Description
This project uses a Machine Learning model (Random Forest) to detect malicious network traffic. If the traffic is classified as normal, an energy-aware scheduling algorithm selects the most suitable network node based on energy, load, and priority.

## Technologies Used
- Python
- Machine Learning (Random Forest)
- Software Defined Networking (SDN)

## Project Structure
- main.py → Main execution file  
- ml_detection.py → Detects normal/attack traffic  
- scheduler.py → Selects best node  
- network_dataset.csv → Training dataset  

## How to Run
1. Install required libraries (numpy, pandas, scikit-learn)
2. Run:
   python main.py

## Sample Output
Traffic Type: Normal  
Running SPES Scheduler...  
Selected Node: Node3
