# CS-117 Lab 11
# Storage Estimator

print("================================")
print("       STORAGE ESTIMATOR")
print("================================")

# Ask the user to enter storage size in gigabytes
storage_gb = float(input("Enter storage size in GB: "))

# Convert gigabytes to megabytes and terabytes
storage_mb = storage_gb * 1024
storage_tb = storage_gb / 1024

# Display the results
print("\nStorage Conversion Results")
print("--------------------------")
print("Storage in GB:", storage_gb)
print("Storage in MB:", storage_mb, "MB")
print("Storage in TB:", round(storage_tb, 4), "TB")

print("\nProgram completed successfully!")