from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TiposExames, PedidoExame, SolicitacaoExame
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants

@login_required
def solicitar_exames(request): 
    tipos_exames = TiposExames.objects.all()
    if request.method == "GET" :
        return render(request, "solicitar_exames.html", {"tipos_exames": tipos_exames})
    elif request.method == "POST":
        exames_id = request.POST.getlist("exames")
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
        
        preco_total = 0
        for i in solicitacao_exames:
            if i.disponivel:
                preco_total += i.preco

        feedback = request.POST.get('feedback', '')

        return render(request, "solicitar_exames.html", {"tipos_exames": tipos_exames,
                                                         "solicitacao_exames": solicitacao_exames,
                                                         "preco_total": preco_total,
                                                         "feedback": feedback})

        
def fechar_pedido(request):
    exames_id = request.POST.getlist('exames')
    solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
    
    pedido_exames = PedidoExame(
        usuario = request.user,
        data =  datetime.now()
    )
    pedido_exames.save()
    
    for exame in solicitacao_exames:
        solicitacao_exames_temp =  SolicitacaoExame(
            usuario=request.user,
            exame=exame,
            status="E",
            feedback=request.POST.get('feedback', '')  # Adicione esta linha
        )
        solicitacao_exames_temp.save()
        pedido_exames.exames.add(solicitacao_exames_temp)
    pedido_exames.save()
    messages.add_message(request, constants.SUCCESS, 'Pedido de exame realizado com sucesso')
    return redirect('/exames/gerenciar_pedidos')   

 
 
def cancelar_pedido(request, id_pedido):
    pedido = PedidoExame.objects.get(id_pedido)
    if not pedido.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Pedido não encontrado')
        return redirect('exames/gerenciar_pedidos')
    return HttpResponse(id_pedido)

@login_required
def gerenciar_pedidos(request):
    pedidos_exames = PedidoExame.objects.filter(usuario=request.user).prefetch_related('exames__exame')
    return render(request, 'gerenciar_pedidos.html', {'pedidos_exames': pedidos_exames})



@login_required
def enviar_feedback(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback', '')
        avaliacao = request.POST.get('avaliacao', None)  # Obtenha a avaliação da solicitação POST
        # Obtenha a última SolicitacaoExame criada pelo usuário
        ultima_solicitacao = SolicitacaoExame.objects.filter(usuario=request.user).order_by('-id').first()
        if ultima_solicitacao is not None:
            # Atualize o feedback e a avaliação da última SolicitacaoExame
            ultima_solicitacao.feedback = feedback
            ultima_solicitacao.avaliacao = int(avaliacao) if avaliacao is not None else None
            ultima_solicitacao.save()
            messages.add_message(request, constants.SUCCESS, 'Feedback enviado com sucesso')
        else:
            messages.add_message(request, constants.ERROR, 'Nenhum exame encontrado para fornecer feedback')
    return redirect('/exames/solicitar_exames')



@login_required
def ver_feedback(request):
    solicitacoes = SolicitacaoExame.objects.filter(usuario=request.user)
    return render(request, 'ver_feedback.html', {'solicitacoes': solicitacoes})

