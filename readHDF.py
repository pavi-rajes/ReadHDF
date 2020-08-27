# Import function
import h5py

# Use this function to load HDF data with the keys 
def load_HDF(filename,print_keys= True):
    """
    Input: 
    filename: name of the file to be loaded with full path 
    
    Output:
    Data from HDF file
    """
    with h5py.File(filename,"r") as f:
        if print_keys:
            print("Keys: %s" %f.keys())
        data = {}

        for key_id in range(len(f.keys())):
            var_suffix = list(f.keys())[key_id]
            data[var_suffix] = list(f[var_suffix])
    return data
    
 # Use case
f_neural = '...../jeev072312_080412/catNeuralDat_jeev072312_080412_trE5_B100.mat'
data_neural = load_HDF(f_neural,True)
#print(data_neural.keys())
