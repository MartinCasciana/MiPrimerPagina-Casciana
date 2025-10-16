def unread_messages_count(request):
    if not request.user.is_authenticated:
        return {"unread_count": 0}
    try:
        from .models import Message
        return {
            "unread_count": Message.objects.filter(recipient=request.user, read=False).count()
        }
    except Exception:
        # evita romper si aún no migraste o no existe la tabla
        return {"unread_count": 0}
