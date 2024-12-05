# tester
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm  # Imports the ft_tqdm function from Loading.py

# Test with ft_tqdm
print("Using ft_tqdm:")
for elem in ft_tqdm(range(333)):
    sleep(0.005)  # Simulates work time
print()  # New line at the end

# Test with tqdm
print("Using tqdm:")
for elem in tqdm(range(333)):
    sleep(0.005)  # Simulates work time
print()  # New line at the end
