from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.utils.html import format_html
from myapp.models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ("data", "enable", "send_to_token")

    # sending messsage view configuration.

    def send_to_token(self, obj):
        # Step 2 show button navigate to the view.
        return format_html(
            f"""<a href="custom/{obj.id}/my_view">send message</a>"""
        )

    send_to_token.allow_tags = True

    def get_urls(self):
        # Step 1 register the view url.
        urls = super().get_urls()
        my_urls = [
            path("custom/<int:token_id>/my_view", self.admin_site.admin_view(self.my_view)),
        ]
        return my_urls + urls

    def my_view(self, request, token_id):
        # Step 3 handle at the view.
        token = Token.objects.get(id=token_id)
        context = dict(
            self.admin_site.each_context(request),
            token=token
        )
        if request.method == "POST":
            # Step 4 send message.
            print(f"""send message: {request.POST["message"]}""")
            context["sent"] = True
        return render(request, "myapp/sometemplate.html", context)


    
admin.site.register(Token, TokenAdmin)
