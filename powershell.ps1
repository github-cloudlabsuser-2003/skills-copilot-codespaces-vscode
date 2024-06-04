# Define parameters
$resourceGroupName = "myResourceGroup"
$location = "West US"
$storageAccountName = "mystorageaccount"

# Create a resource group
New-AzResourceGroup -Name $resourceGroupName -Location $location

# Create a storage account
New-AzStorageAccount -ResourceGroupName $resourceGroupName -Name $storageAccountName -Location $location -SkuName Standard_LRS
