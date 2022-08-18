from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator
from intro.models import *


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


def likes_society(request, partner_id):
    like_p = get_object_or_404(PartnerSociety, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('society')


def likes_science(request, partner_id):
    like_p = get_object_or_404(PartnerScience, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('science')


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


def likes_engine(request, partner_id):
    like_p = get_object_or_404(PartnerEngine, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('engine')


def likes_elec(request, partner_id):
    like_p = get_object_or_404(PartnerElec, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('elec')


def likes_farm(request, partner_id):
    like_p = get_object_or_404(PartnerFarm, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('farm')


def likes_teacher(request, partner_id):
    like_p = get_object_or_404(PartnerTeacher, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('teacher')


def likes_life(request, partner_id):
    like_p = get_object_or_404(PartnerLife, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('life')


def likes_vet(request, partner_id):
    like_p = get_object_or_404(PartnerVet, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('vet')


def likes_medicine(request, partner_id):
    like_p = get_object_or_404(PartnerMedicine, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('medicine')


def likes_doctor(request, partner_id):
    like_p = get_object_or_404(PartnerDoctor, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('doctor')


def likes_mixed(request, partner_id):
    like_p = get_object_or_404(PartnerMixed, id=partner_id)
    if request.user in like_p.like.all():
        like_p.like.remove(request.user)
        like_p.like_count -= 1
        like_p.save()
    else:
        like_p.like.add(request.user)
        like_p.like_count += 1
        like_p.save()
    return redirect('mixed')