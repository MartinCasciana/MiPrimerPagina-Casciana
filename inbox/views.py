from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm

@login_required
def inbox_list(request):
    messages_qs = Message.objects.filter(recipient=request.user)
    return render(request, "inbox/inbox_list.html", {"messages_list": messages_qs})

@login_required
def sent_list(request):
    messages_qs = Message.objects.filter(sender=request.user)
    return render(request, "inbox/sent_list.html", {"messages_list": messages_qs})

@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    # Permiso: solo remitente o destinatario
    if msg.sender != request.user and msg.recipient != request.user:
        messages.error(request, "No tenés permiso para ver este mensaje.")
        return redirect("inbox_home")
    # Marcar leído si soy el destinatario
    if msg.recipient == request.user and not msg.read:
        msg.read = True
        msg.save(update_fields=["read"])
    return render(request, "inbox/message_detail.html", {"msg": msg})

@login_required
def compose(request, username=None):
    initial = {}
    if username:
        try:
            initial_user = User.objects.get(username=username)
            initial["recipient"] = initial_user.id
        except User.DoesNotExist:
            pass
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            new_msg = form.save(commit=False)
            new_msg.sender = request.user
            new_msg.save()
            messages.success(request, "Mensaje enviado.")
            return redirect("inbox_home")
    else:
        form = MessageForm(initial=initial)
    return render(request, "inbox/message_form.html", {"form": form})

@login_required
def delete_message(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if msg.sender != request.user and msg.recipient != request.user:
        messages.error(request, "No tenés permiso para borrar este mensaje.")
        return redirect("inbox_home")
    if request.method == "POST":
        msg.delete()
        messages.success(request, "Mensaje eliminado.")
        return redirect("inbox_home")
    return render(request, "inbox/message_confirm_delete.html", {"msg": msg})
