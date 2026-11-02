import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Example data
data = {
    0: {-0.0: 10.0, 10.0: -10.0},
    25.0: {5.0: 0},
    9: {1.0: 8.0, 9.0: -8.0},
    -11: {-1.0: 12.0, 11.0: -12.0}
}

# Extracting dates and speeds from the dictionary
dates = []
speeds = []
for key, value in data.items():
    for date, speed in value.items():
        dates.append(date)
        speeds.append(speed)

# Sorting dates and speeds according to the dates
sorted_data = sorted(zip(dates, speeds))
dates, speeds = zip(*sorted_data)

# Convert dates to datetime objects (assuming they are relative to a start date)
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=float(d)) for d in dates]

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(min(dates), max(dates))
ax.set_ylim(min(speeds) - 5, max(speeds) + 5)
ax.set_xlabel('Date')
ax.set_ylabel('Speed')

line, = ax.plot([], [], lw=2)

# Formatting the dates on x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator())

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Update function for the animation
def update(frame):
    x = dates[:frame]
    y = speeds[:frame]
    line.set_data(x, y)
    return line,

# Creating the animation
ani = FuncAnimation(fig, update, frames=len(dates) + 1, init_func=init, blit=True, repeat=False)

# Show the animation
plt.show()
