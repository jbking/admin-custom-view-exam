from django.contrib import admin
from django.utils.html import format_html
from myapp.models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('data', 'enable', 'send_to_token')

    def send_to_token(self, obj):
        # Step 1 show button navigate to send text view
        return format_html(
            '<form method="post" target=""><input type="submit"/></form>'
        )

    send_to_token.allow_tags = True

    
admin.site.register(Token, TokenAdmin)
