# CS-117 Lab 11
# Storage Estimator

print("================================")
print("       STORAGE ESTIMATOR")
print("================================")

# Ask the user to enter storage size in gigabytes
storage_gb = float(input("Enter storage size in GB: "))

# Convert gigabytes to megabytes
storage_mb = storage_gb * 1024

# Display the result
print("\nStorage Conversion Result")
print("-------------------------")
print("Storage in GB:", storage_gb)
print("Storage in MB:", storage_mb, "MB")

print("\nProgram completed successfully!")