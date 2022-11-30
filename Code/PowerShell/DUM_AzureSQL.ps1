Connect-AzAccount -UseDeviceAuthentication -TenantId xxxx-xxxx-xxxx-xxxx-xxxx -SubscriptionId xxxx-xxxx-xxxx-xxxx

$server = Get-AzSqlServer -ResourceGroupName "RESOURCEGROUPNAME" -ServerName "SERVERNAME"

#Initiate the call to the REST API to set externalPolicyBasedAuthorization to true
Invoke-AzRestMethod -Method PUT -Path "$($server.ResourceId)/externalPolicyBasedAuthorizations/MicrosoftPurview?api-version=2021-11-01-preview" -Payload '{"properties":{"externalPolicyBasedAuthorization":true}}'

# Now, verify that the property "externalPolicyBasedAuthorization" has been set to true
Invoke-AzRestMethod -Method GET -Path "$($server.ResourceId)/externalPolicyBasedAuthorizations/MicrosoftPurview?api-version=2021-11-01-preview"