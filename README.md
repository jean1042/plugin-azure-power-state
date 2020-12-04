# plugin-azure-power-state
Plugin for MS Azure Virtual Machine to Check Running status
- Collecting Virtual Machine State


# Data Sample

## Virtual Machine Instance

- cloud_service_type: Compute
- cloud_service_group: VirtualMachine
- provider: azure

~~~
"data": {
        "compute": {
            "instance_state": "RUNNING",
            "instance_id": "/subscriptions/xxxx/resourceGroups/yyyy/providers/Microsoft.Compute/virtualMachines/zzz"
        },
        "power_state": {
            "status": "RUNNING"
        }    
	....
}
~~~
