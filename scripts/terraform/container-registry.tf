#
# Creates a container registry on Azure so that you can publish your Docker images.
#
resource "azurerm_container_registry" "container_registry" {
  name                = var.app_name
  resource_group_name = var.group_name
  location            = var.location
  admin_enabled       = true
  sku                 = "Basic"
}

output "registry_username" {
  value = azurerm_container_registry.container_registry.admin_username
}

output "registry_password" {
  value = azurerm_container_registry.container_registry.admin_password
}

output "container_registry_url" {
  value = azurerm_container_registry.container_registry.login_server
}

output "resource_group_name" {
  value = azurerm_resource_group.container_registry.resource_group_name
}