from rest_framework import permissions


class AuthenticatedDevIsManagerOrReadOnly(permissions.BasePermission):
    """
    Permission for projects: Senior PMs and managers of a project can edit or delete a project.
    As always superusers can do anything and everything.
    If the user doesn't have the above permissions, they need to be a dev to see projects (no write permission).
    """

    def has_object_permission(self, request, view, project):
        # user needs to be authenticated
        if request.user.is_authenticated:
            # Read permissions are allowed to authenticated requests by dev users
            if request.method in permissions.SAFE_METHODS  \
                    and (request.user.has_perm('tracker.view_project') or request.user.has_perms('tracker.all_project')):
                return True
            # Write permissions for managers and superusers
            if request.user.is_superuser or request.user.has_perm(
                    'tracker.all_project') or project.manager == request.user:
                return True

        return False

    def has_permission(self, request, view):
        # user needs to be authenticated
        if request.user.is_authenticated:
            # Read permissions are allowed to authenticated requests by dev users
            if request.method in permissions.SAFE_METHODS \
                    and (request.user.has_perm('tracker.view_project') or request.user.has_perms('tracker.all_project')):
                return True
            # Write permissions for managers and superusers
            if request.user.is_superuser or request.user.has_perm('tracker.all_project'):
                return True

        return False


class AuthenticatedDevIsAssignedOrManagerOrReadOnly(permissions.BasePermission):
    """
    Permission for stories: Senior PMs, managers of the story's project, contributors to the project and the person
    assigned to a project can edit it.
    If the user doesn't have the above permissions, they need to be a dev to see stories (no write permission).
    """

    def has_object_permission(self, request, view, story):
        # user needs to be authenticated
        if request.user.is_authenticated:
            # Read permissions are allowed to authenticated requests by dev users
            if request.method in permissions.SAFE_METHODS \
                    and (request.user.has_perm('tracker.view_story') or request.user.has_perms('tracker.all_story')):
                return True
            # Write permissions for managers and superusers
            if request.user.is_superuser or request.user.has_perm('tracker.all_story') \
                    or story.project.manager == request.user or story.project.contributors.filter(pk=request.user.pk) \
                    or story.assigned_to == request.user:
                return True

        return False

    def has_permission(self, request, view):
        # user needs to be authenticated
        if request.user.is_authenticated:
            # Read permissions are allowed to authenticated requests by dev users
            if request.method in permissions.SAFE_METHODS \
                    and (request.user.has_perm('tracker.view_story') or request.user.has_perms('tracker.all_story')):
                return True
            # Write permissions for managers and superusers
            if request.user.is_superuser or request.user.has_perms('tracker.all_story') \
                    or request.user.has_perm('tracker.add_story'):
                return True

        return False