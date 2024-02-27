from django.contrib import admin

from .models import Dream, Person, Group, Membership, Place, RestaurantInPerson, Waiter


class GroupInline(admin.TabularInline):
    model = Group


class MembershipInline(admin.TabularInline):
    model = Membership


class PersonInline(admin.TabularInline):
    model = Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass


@admin.register(Dream)
class DreamAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(RestaurantInPerson)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    pass
