from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import Asset, Comment, Assignment

# Create your views here.
from django.db.models import Q
from .models import Asset

def search_asset(request):

    query = request.GET.get('q')

    results = None

    if query:

        results = Asset.objects.filter(

            Q(serial_number__icontains=query) |
            Q(company__icontains=query) |
            Q(computer_type__icontains=query) |
            Q(brand__icontains=query) |
            Q(model__icontains=query) |
            Q(year__icontains=query) |
            Q(opco_asset_tag__icontains=query) |
            Q(invoice_number__icontains=query) |
            Q(state__icontains=query) |
            Q(comments__icontains=query) |
            Q(column1__icontains=query) |
            Q(column2__icontains=query)

        )

    return render(request, 'search.html', {'results': results})




def asset_detail(request, id):

    asset = get_object_or_404(Asset, id=id)

    comments = Comment.objects.filter(asset=asset).order_by('created_at')

    users = User.objects.all()

    if request.method == "POST":

        message = request.POST.get("message")

        assign_to = request.POST.get("assign_to")

        # Save comment
        if message:
            Comment.objects.create(
                asset=asset,
                user=request.user,
                message=message
            )
            
        status = request.POST.get("status")

        if status and request.user.is_staff:
            asset.status = status
            asset.save()

        # Save assignment (admin only)
        if assign_to and request.user.is_staff:

            Assignment.objects.create(
                asset=asset,
                assigned_to=assign_to,
                assigned_by=request.user,
                comments=message
            )

            asset.status = "progress"
            asset.save()

        return redirect(f"/asset/{id}/")

    return render(request, "asset_detail.html", {
        "asset": asset,
        "comments": comments,
        "users": users
    })
