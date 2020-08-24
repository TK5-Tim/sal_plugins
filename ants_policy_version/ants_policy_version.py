
from django.db.models import Count

import sal.plugin
import server.utils as utils
from inventory.models import InventoryItem

class ANTS_Policy_version(sal.plugin.Widget):
    
    description = "Show Ants Policy Version"

    def get_context(self, queryset, **kwargs):
        context = self.super_get_context(queryset, **kwargs)
        context['data'] = (
            InventoryItem.objects
            .filter(machine__in=queryset, conditions__condition_name="ants_policy_version")
        )
    

    def filter(self, machines, data):
        machines = machines.filter(
            conditions__condition_name="ants_policy_version", 
            
        )