default_az_parameters = {
    "azure_cluster" : { 
        "subscription": "Bing DLTS",
        "infra_node_num": 1, 
        "worker_node_num": 2,
        "mysqlserver_node_num": 0,
        "nfs_node_num": 1,
        "azure_location": "westus2",
        "infra_vm_size" : "Standard_D1_v2",
        "worker_vm_size": "Standard_NC6",
        "mysqlserver_vm_size": "Standard_D1_v2",
        "nfs_vm_size": "Standard_D1_v2",
        "vm_image" : "Canonical:UbuntuServer:18.04-LTS:18.04.201907221",
        "os_storage_sku": "Premium_LRS",
        "os_storage_sz": 50,
        "vm_local_storage_sku" : "Premium_LRS",
        "infra_local_storage_sz" : 1023,
        "worker_local_storage_sz" : 1023,
        "mysqlserver_local_storage_sz": 2048,
        "nfs_data_disk_sku" : "Premium_LRS",
        "nfs_data_disk_sz" : 1023,
        "nfs_data_disk_num": 1,
        "nfs_data_disk_path": '/data',
        "nfs_vm": [],
        "eviction_policy": "Deallocate",
        "single_placement_group": "false",
        "default_low_priority_domain": "redmond.corp.microsoft.com",
    },
}
