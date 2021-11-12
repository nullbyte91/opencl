# Import the Python OpenCL API
import pyopencl as cl

# Create a list of all the platform IDs
platforms = cl.get_platforms()

print("Number of OpenCL platforms:{} \n".format(len(platforms)))

# Investigate each platform
for p in platforms:
    # Print out some information about the platforms
    print("Platform:{} ".format(p.name))
    print("Vendor:{}".format(p.vendor))
    print("Version:{}".format(p.version))

    # Discover all devices
    devices = p.get_devices()
    print("Number of devices:{}".format(len(devices)))

    # Investigate each device
    for d in devices:
        print("\t-------------------------")
        # Print out some information about the devices
        print("\t\tName: {}".format(d.name))
        print("\t\tVersion: {}".format(d.opencl_c_version))
        print("\t\tMax. Compute Units:{}".format(d.max_compute_units))
        print("\t\tLocal Memory Size:{} KB".format(d.local_mem_size/1024))
        print("\t\tGlobal Memory Size:{} MB".format(d.global_mem_size/(1024*1024)))
        print("\t\tMax Alloc Size:{} MB".format(d.max_mem_alloc_size/(1024*1024)))
        print("\t\tMax Work-group Total Size:{}".format(d.max_work_group_size))
