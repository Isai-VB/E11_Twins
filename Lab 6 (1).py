#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside = pd.read_csv('outsidedata.csv',skiprows=0)
inside = pd.read_csv('insidedata.csv',skiprows=0)

display(outside)
display(inside)


# # Other Teams Data - Step 2 Onwards

# In[14]:


def plot_time_series(df, title):
    df = df.iloc[30:] 
    plt.figure(figsize=(10, 5))
    
    for col in df.columns:
        if col.lower() != 'time':
            plt.plot(range(len(df)), df[col], label=col) 

    plt.xlabel('Data Entry Number')
    plt.ylabel('Sensor Value')
    plt.yscale('log')
    plt.title(title)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.tight_layout()
    plt.show()

plot_time_series(outside, 'Outside Data')
plot_time_series(inside, 'Inside Data')


# In[3]:


import matplotlib.pyplot as plt
import pandas as pd

inside = inside.iloc[30:]
outside = outside.iloc[30:]

sensor_columns = [col for col in inside.columns if col != inside.columns[0]]

start_index = 30

for sensor in sensor_columns:
    plt.figure(figsize=(10, 5))
    
    plt.plot(range(start_index, len(inside) + start_index), inside[sensor], label=f'Inside {sensor}')
    plt.plot(range(start_index, len(outside) + start_index), outside[sensor], label=f'Outside {sensor}')
    
    plt.xlabel('Data Entry Number')
    plt.ylabel(sensor)
    plt.title(f'{sensor} vs Time (Inside vs Outside)')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()


# In[4]:


import matplotlib.pyplot as plt
import pandas as pd

inside = inside.iloc[30:]
outside = outside.iloc[30:]

sensor_columns = [col for col in inside.columns if col != inside.columns[0]]

for sensor in sensor_columns:
    inside_data = inside[sensor].dropna()
    outside_data = outside[sensor].dropna()

    plt.figure(figsize=(10, 5))
    plt.hist(inside_data, bins=50, label=f'Inside {sensor}')
    plt.hist(outside_data, bins=70, label=f'Outside {sensor}')
    plt.xlabel(sensor)
    plt.ylabel('Frequency')
    plt.title(f'{sensor} Distribution: Inside vs Outside')
    plt.legend()
    plt.tight_layout()
    plt.show()


# In[5]:


inside = inside.iloc[30:]
outside = outside.iloc[30:]

sensor_columns = [col for col in inside.columns if col != inside.columns[0]]  # Exclude the first column

for sensor in sensor_columns:
    inside_data = inside[sensor].dropna()
    outside_data = outside[sensor].dropna()

    mu_in = np.mean(inside_data)
    mu_out = np.mean(outside_data)
    
    sigma_in = np.std(inside_data, ddof=1)
    sigma_out = np.std(outside_data, ddof=1)
    
    n_in = len(inside_data)
    n_out = len(outside_data)
    
    SEM_in = sigma_in / np.sqrt(n_in)
    SEM_out = sigma_out / np.sqrt(n_out)
    
    SE_delta = np.sqrt(SEM_in**2 + SEM_out**2)
    
    delta = abs(mu_in - mu_out)
    
    num_standard_devs = delta / SE_delta
    
    print(f"Sensor: {sensor}")
    print(f"Inside Mean: {mu_in:.2f}, Inside Std Dev: {sigma_in:.2f}, SEM: {SEM_in:.2f}")
    print(f"Outside Mean: {mu_out:.2f}, Outside Std Dev: {sigma_out:.2f}, SEM: {SEM_out:.2f}")
    print(f"Difference in Means: {delta:.2f}, Combined Standard Error: {SE_delta:.2f}")
    print(f"Number of Standard Deviations between Means: {num_standard_devs:.2f}")
    
    if num_standard_devs > 3:
        print(f"For sensor {sensor}, the means are separated by more than 3σ; statistically significant difference.")
    else:
        print(f"For sensor {sensor}, the means are not separated by more than 3σ; no significant difference.")
    print("\n")


# Almost all the distribution graphs look to be well described as a gaussian distribution, except fot the gas distribiutions on the inside and the humidity distribution on the outside. 

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside1 = pd.read_csv('outsidedata.csv', skiprows=0)
outside2 = pd.read_csv('SensorsOutside.csv', skiprows=1)

time_outside1 = np.arange(30, len(outside1))  
data_outside1 = outside1.iloc[30:, 4] 

time_outside2 = np.arange(30, len(outside2)) 
data_outside2 = outside2.iloc[30:, 1]  

inside1 = pd.read_csv('insidedata.csv', skiprows=0)

inside2 = pd.read_csv('SensorsInside.csv', skiprows=1)

time_inside1 = np.arange(30, len(inside1))
data_inside1 = inside1.iloc[30:, 4]  

time_inside2 = np.arange(30, len(inside2))
data_inside2 = inside2.iloc[30:, 1] 
inside = pd.read_csv('SensorsInside.csv', skiprows=1)
time_inside = np.arange(30, len(inside))  
data_inside = inside.iloc[30:, 1] 
min_length = min(len(data_outside1), len(data_outside2), len(data_inside1), len(data_inside2), len(data_inside))

time_outside1 = time_outside1[:min_length]
time_outside2 = time_outside2[:min_length]
time_inside1 = time_inside1[:min_length]
time_inside2 = time_inside2[:min_length]
time_inside = time_inside[:min_length]

data_outside1 = data_outside1[:min_length]
data_outside2 = data_outside2[:min_length]
data_inside1 = data_inside1[:min_length]
data_inside2 = data_inside2[:min_length]
data_inside = data_inside[:min_length]

plt.figure(figsize=(10, 6))

plt.plot(time_outside1, data_outside1, label='Other Outside (outside1)', color='blue')
plt.plot(time_outside2, data_outside2, label='Self Outside (outside2)', color='red')

plt.plot(time_inside1, data_inside1, label='Other Inside (inside1)', color='green')
plt.plot(time_inside2, data_inside2, label='Self Inside (inside2)', color='orange')

plt.xlabel('Time (Seconds)')
plt.ylabel('Temperature')
plt.title('Temperature Comparison')

plt.legend()
plt.grid(True)

plt.show()


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside1 = pd.read_csv('outsidedata.csv', skiprows=0)

outside2 = pd.read_csv('SensorsOutside.csv', skiprows=1)

time_outside1 = np.arange(30, len(outside1))
data_outside1 = outside1.iloc[30:, 5]  
time_outside2 = np.arange(30, len(outside2))  
data_outside2 = outside2.iloc[30:, 2] 
inside1 = pd.read_csv('insidedata.csv', skiprows=0)

inside2 = pd.read_csv('SensorsInside.csv', skiprows=1)

time_inside1 = np.arange(30, len(inside1))
data_inside1 = inside1.iloc[30:, 5]  

time_inside2 = np.arange(30, len(inside2))  
data_inside2 = inside2.iloc[30:, 2]  
inside = pd.read_csv('SensorsInside.csv', skiprows=1)
time_inside = np.arange(30, len(inside)) 
data_inside = inside.iloc[30:, 1]  

min_length = min(len(data_outside1), len(data_outside2), len(data_inside1), len(data_inside2), len(data_inside))

time_outside1 = time_outside1[:min_length]
time_outside2 = time_outside2[:min_length]
time_inside1 = time_inside1[:min_length]
time_inside2 = time_inside2[:min_length]
time_inside = time_inside[:min_length]

data_outside1 = data_outside1[:min_length]
data_outside2 = data_outside2[:min_length]
data_inside1 = data_inside1[:min_length]
data_inside2 = data_inside2[:min_length]
data_inside = data_inside[:min_length]

plt.figure(figsize=(10, 6))

plt.plot(time_outside1, data_outside1, label='Other Outside (outside1)', color='blue')
plt.plot(time_outside2, data_outside2, label='Self Outside (outside2)', color='red')

plt.plot(time_inside1, data_inside1, label='Other Inside (inside1)', color='green')
plt.plot(time_inside2, data_inside2, label='Self Inside (inside2)', color='orange')

plt.xlabel('Time (Seconds)')
plt.ylabel('Gas (Ohms)')
plt.title('Gas Comparison')

plt.legend()
plt.grid(True)

plt.show()


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside1 = pd.read_csv('outsidedata.csv', skiprows=0)

outside2 = pd.read_csv('SensorsOutside.csv', skiprows=1)

time_outside1 = np.arange(30, len(outside1)) 
data_outside1 = outside1.iloc[30:, 6] 
time_outside2 = np.arange(30, len(outside2))
data_outside2 = outside2.iloc[30:, 3]

inside1 = pd.read_csv('insidedata.csv', skiprows=0)

inside2 = pd.read_csv('SensorsInside.csv', skiprows=1)

time_inside1 = np.arange(30, len(inside1))  
data_inside1 = inside1.iloc[30:, 6] 
time_inside2 = np.arange(30, len(inside2)) 
data_inside2 = inside2.iloc[30:, 3]

inside = pd.read_csv('SensorsInside.csv', skiprows=1)
time_inside = np.arange(30, len(inside))  
data_inside = inside.iloc[30:, 1] 

min_length = min(len(data_outside1), len(data_outside2), len(data_inside1), len(data_inside2), len(data_inside))

time_outside1 = time_outside1[:min_length]
time_outside2 = time_outside2[:min_length]
time_inside1 = time_inside1[:min_length]
time_inside2 = time_inside2[:min_length]
time_inside = time_inside[:min_length]

data_outside1 = data_outside1[:min_length]
data_outside2 = data_outside2[:min_length]
data_inside1 = data_inside1[:min_length]
data_inside2 = data_inside2[:min_length]
data_inside = data_inside[:min_length]

plt.figure(figsize=(10, 6))

plt.plot(time_outside1, data_outside1, label='Other Outside (outside1)', color='blue')
plt.plot(time_outside2, data_outside2, label='Self Outside (outside2)', color='red')

plt.plot(time_inside1, data_inside1, label='Other Inside (inside1)', color='green')
plt.plot(time_inside2, data_inside2, label='Self Inside (inside2)', color='orange')

plt.xlabel('Time (Seconds)')
plt.ylabel('Humidity %')
plt.title('Humidity Comparison')

plt.legend()
plt.grid(True)

plt.show()


# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside1 = pd.read_csv('outsidedata.csv', skiprows=0)

outside2 = pd.read_csv('SensorsOutside.csv', skiprows=1)

time_outside1 = np.arange(30, len(outside1)) 
data_outside1 = outside1.iloc[30:, 7] 

time_outside2 = np.arange(30, len(outside2)) 
data_outside2 = outside2.iloc[30:, 4]  

inside1 = pd.read_csv('insidedata.csv', skiprows=0)

inside2 = pd.read_csv('SensorsInside.csv', skiprows=1)

time_inside1 = np.arange(30, len(inside1))  
data_inside1 = inside1.iloc[30:, 7] 

time_inside2 = np.arange(30, len(inside2))  
data_inside2 = inside2.iloc[30:, 4]  

inside = pd.read_csv('SensorsInside.csv', skiprows=1)
time_inside = np.arange(30, len(inside)) 
data_inside = inside.iloc[30:, 1]

min_length = min(len(data_outside1), len(data_outside2), len(data_inside1), len(data_inside2), len(data_inside))

time_outside1 = time_outside1[:min_length]
time_outside2 = time_outside2[:min_length]
time_inside1 = time_inside1[:min_length]
time_inside2 = time_inside2[:min_length]
time_inside = time_inside[:min_length]

data_outside1 = data_outside1[:min_length]
data_outside2 = data_outside2[:min_length]
data_inside1 = data_inside1[:min_length]
data_inside2 = data_inside2[:min_length]
data_inside = data_inside[:min_length]

plt.figure(figsize=(10, 6))

plt.plot(time_outside1, data_outside1, label='Other Outside (outside1)', color='blue')
plt.plot(time_outside2, data_outside2, label='Self Outside (outside2)', color='red')

plt.plot(time_inside1, data_inside1, label='Other Inside (inside1)', color='green')
plt.plot(time_inside2, data_inside2, label='Self Inside (inside2)', color='orange')

plt.xlabel('Time (Seconds)')
plt.ylabel('Pressure (hPa)')
plt.title('Pressure Comparison')

plt.legend()
plt.grid(True)

plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside1 = pd.read_csv('outsidedata.csv', skiprows=0)

outside2 = pd.read_csv('SensorsOutside.csv', skiprows=1)

time_outside1 = np.arange(30, len(outside1)) 
data_outside1 = outside1.iloc[30:, 8]

time_outside2 = np.arange(30, len(outside2))
data_outside2 = outside2.iloc[30:, 5]  
inside1 = pd.read_csv('insidedata.csv', skiprows=0)

inside2 = pd.read_csv('SensorsInside.csv', skiprows=1)


time_inside1 = np.arange(30, len(inside1))  
data_inside1 = inside1.iloc[30:, 8]  
time_inside2 = np.arange(30, len(inside2))  
data_inside2 = inside2.iloc[30:, 5] 

inside = pd.read_csv('SensorsInside.csv', skiprows=1)
time_inside = np.arange(30, len(inside)) 
data_inside = inside.iloc[30:, 1] 
min_length = min(len(data_outside1), len(data_outside2), len(data_inside1), len(data_inside2), len(data_inside))

time_outside1 = time_outside1[:min_length]
time_outside2 = time_outside2[:min_length]
time_inside1 = time_inside1[:min_length]
time_inside2 = time_inside2[:min_length]
time_inside = time_inside[:min_length]

data_outside1 = data_outside1[:min_length]
data_outside2 = data_outside2[:min_length]
data_inside1 = data_inside1[:min_length]
data_inside2 = data_inside2[:min_length]
data_inside = data_inside[:min_length]

plt.figure(figsize=(10, 6))

plt.plot(time_outside1, data_outside1, label='Other Outside (outside1)', color='blue')
plt.plot(time_outside2, data_outside2, label='Self Outside (outside2)', color='red')

plt.plot(time_inside1, data_inside1, label='Other Inside (inside1)', color='green')
plt.plot(time_inside2, data_inside2, label='Self Inside (inside2)', color='orange')

plt.xlabel('Time (Seconds)')
plt.ylabel('Altitude (m)')
plt.title('Altitude Comparison')

plt.legend()
plt.grid(True)

plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside1 = pd.read_csv('outsidedata.csv', skiprows=0)

outside2 = pd.read_csv('SensorsOutside.csv', skiprows=1)

time_outside1 = np.arange(30, len(outside1)) 
data_outside1 = outside1.iloc[30:, 1]  

time_outside2 = np.arange(30, len(outside2)) 
data_outside2 = outside2.iloc[30:, 6]
inside1 = pd.read_csv('insidedata.csv', skiprows=0)

inside2 = pd.read_csv('SensorsInside.csv', skiprows=1)

time_inside1 = np.arange(30, len(inside1))  
data_inside1 = inside1.iloc[30:, 1]
time_inside2 = np.arange(30, len(inside2)) 
data_inside2 = inside2.iloc[30:, 6]  

inside = pd.read_csv('SensorsInside.csv', skiprows=1)
time_inside = np.arange(30, len(inside))  
data_inside = inside.iloc[30:, 1]  
min_length = min(len(data_outside1), len(data_outside2), len(data_inside1), len(data_inside2), len(data_inside))

time_outside1 = time_outside1[:min_length]
time_outside2 = time_outside2[:min_length]
time_inside1 = time_inside1[:min_length]
time_inside2 = time_inside2[:min_length]
time_inside = time_inside[:min_length]

data_outside1 = data_outside1[:min_length]
data_outside2 = data_outside2[:min_length]
data_inside1 = data_inside1[:min_length]
data_inside2 = data_inside2[:min_length]
data_inside = data_inside[:min_length]

plt.figure(figsize=(10, 6))

plt.plot(time_outside1, data_outside1, label='Other Outside (outside1)', color='blue')
plt.plot(time_outside2, data_outside2, label='Self Outside (outside2)', color='red')

plt.plot(time_inside1, data_inside1, label='Other Inside (inside1)', color='green')
plt.plot(time_inside2, data_inside2, label='Self Inside (inside2)', color='orange')

plt.xlabel('Time (Seconds)')
plt.ylabel('Standard')
plt.title('PM1.0 Comparison')

plt.legend()
plt.grid(True)

plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside1 = pd.read_csv('outsidedata.csv', skiprows=0)

outside2 = pd.read_csv('SensorsOutside.csv', skiprows=1)

time_outside1 = np.arange(30, len(outside1))
data_outside1 = outside1.iloc[30:, 2] 

time_outside2 = np.arange(30, len(outside2)) 
data_outside2 = outside2.iloc[30:, 7]  

inside1 = pd.read_csv('insidedata.csv', skiprows=0)

inside2 = pd.read_csv('SensorsInside.csv', skiprows=1)


time_inside1 = np.arange(30, len(inside1))  
data_inside1 = inside1.iloc[30:, 2] 

time_inside2 = np.arange(30, len(inside2)) 
data_inside2 = inside2.iloc[30:, 7] 
inside = pd.read_csv('SensorsInside.csv', skiprows=1)
time_inside = np.arange(30, len(inside))  
data_inside = inside.iloc[30:, 1]
min_length = min(len(data_outside1), len(data_outside2), len(data_inside1), len(data_inside2), len(data_inside))

time_outside1 = time_outside1[:min_length]
time_outside2 = time_outside2[:min_length]
time_inside1 = time_inside1[:min_length]
time_inside2 = time_inside2[:min_length]
time_inside = time_inside[:min_length]

data_outside1 = data_outside1[:min_length]
data_outside2 = data_outside2[:min_length]
data_inside1 = data_inside1[:min_length]
data_inside2 = data_inside2[:min_length]
data_inside = data_inside[:min_length]

plt.figure(figsize=(10, 6))

plt.plot(time_outside1, data_outside1, label='Other Outside (outside1)', color='blue')
plt.plot(time_outside2, data_outside2, label='Self Outside (outside2)', color='red')

plt.plot(time_inside1, data_inside1, label='Other Inside (inside1)', color='green')
plt.plot(time_inside2, data_inside2, label='Self Inside (inside2)', color='orange')

plt.xlabel('Time (Seconds)')
plt.ylabel('Standard')
plt.title('PM2.5 Comparison')

plt.legend()
plt.grid(True)

plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outside1 = pd.read_csv('outsidedata.csv', skiprows=0)

outside2 = pd.read_csv('SensorsOutside.csv', skiprows=1)

time_outside1 = np.arange(30, len(outside1))  
data_outside1 = outside1.iloc[30:, 3]  
time_outside2 = np.arange(30, len(outside2))  
data_outside2 = outside2.iloc[30:, 8]  
inside1 = pd.read_csv('insidedata.csv', skiprows=0)

inside2 = pd.read_csv('SensorsInside.csv', skiprows=1)

time_inside1 = np.arange(30, len(inside1))  
data_inside1 = inside1.iloc[30:, 3]  
time_inside2 = np.arange(30, len(inside2))  
data_inside2 = inside2.iloc[30:, 8]  

inside = pd.read_csv('SensorsInside.csv', skiprows=1)
time_inside = np.arange(30, len(inside))  
data_inside = inside.iloc[30:, 1]  

min_length = min(len(data_outside1), len(data_outside2), len(data_inside1), len(data_inside2), len(data_inside))

time_outside1 = time_outside1[:min_length]
time_outside2 = time_outside2[:min_length]
time_inside1 = time_inside1[:min_length]
time_inside2 = time_inside2[:min_length]
time_inside = time_inside[:min_length]

data_outside1 = data_outside1[:min_length]
data_outside2 = data_outside2[:min_length]
data_inside1 = data_inside1[:min_length]
data_inside2 = data_inside2[:min_length]
data_inside = data_inside[:min_length]

plt.figure(figsize=(10, 6))

plt.plot(time_outside1, data_outside1, label='Other Outside (outside1)', color='blue')
plt.plot(time_outside2, data_outside2, label='Self Outside (outside2)', color='red')

plt.plot(time_inside1, data_inside1, label='Other Inside (inside1)', color='green')
plt.plot(time_inside2, data_inside2, label='Self Inside (inside2)', color='orange')

plt.xlabel('Time (Seconds)')
plt.ylabel('Standard')
plt.title('PM10 Comparison')

plt.legend()
plt.grid(True)

plt.show()


# Examining all the graphs, it seems that our sensors are similar in their data readinds, but our own outside measurements seems to be off. This could be due to the time it took to get upstairs and outside. We removed the first 30 seconds of all the data to see if we could eliminate some of that human error but it seems like it wasn't enough.  
