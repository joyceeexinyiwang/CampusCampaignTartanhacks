from django.contrib import admin

from .models import Campaign, PhysicalGoal, VirtualGoal, Suggestion


admin.site.register(Campaign)
admin.site.register(PhysicalGoal)
admin.site.register(VirtualGoal)
admin.site.register(Suggestion)

