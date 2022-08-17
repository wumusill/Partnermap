from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator
from intro.models import PartnerBusiness, PartnerHumanity


def likes_humanity(request, partner_id):
    like_p = get_object_or_404(PartnerHumanity, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('humanity')


def likes_business(request, partner_id):
    like_p = get_object_or_404(PartnerBusiness, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('business')