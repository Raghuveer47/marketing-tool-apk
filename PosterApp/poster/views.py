from django.shortcuts import render, redirect
from .forms import PosterForm
from .models import Poster
from django.shortcuts import get_object_or_404

def create_poster(request):
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            # Save data to the database
            poster = Poster(
                company_name=form.cleaned_data['company_name'],
                price=form.cleaned_data['price'],
                slogan=form.cleaned_data['slogan'],
                property_image=form.cleaned_data['property_image'],
                feature1=form.cleaned_data['feature1'],
                feature1_image=form.cleaned_data['feature1_image'],
                feature2=form.cleaned_data['feature2'],
                feature2_image=form.cleaned_data['feature2_image'],
                feature3=form.cleaned_data['feature3'],
                feature3_image=form.cleaned_data['feature3_image'],
                facilities=','.join(form.cleaned_data['facilities'].split('\n')),  # Save facilities as a comma-separated string
                realtor_name=form.cleaned_data['realtor_name'],
                realtor_role=form.cleaned_data['realtor_role'],
                realtor_image=form.cleaned_data['realtor_image'],
                contact_number=form.cleaned_data['contact_number'],
                contact_email=form.cleaned_data['contact_email'],
                website=form.cleaned_data['website'],
            )
            poster.save()
            return redirect('poster_detail', pk=poster.id)  # Redirect to the detail page
    else:
        form = PosterForm()
    return render(request, 'poster_form.html', {'form': form})

def poster_detail(request, pk):
    poster = get_object_or_404(Poster, pk=pk)
    context = {
        'company_name': poster.company_name,
        'price': poster.price,
        'slogan': poster.slogan,
        'property_image': poster.property_image.url,
        'feature1': poster.feature1,
        'feature1_image': poster.feature1_image.url,
        'feature2': poster.feature2,
        'feature2_image': poster.feature2_image.url,
        'feature3': poster.feature3,
        'feature3_image': poster.feature3_image.url,
        'facilities': poster.facilities.split(','),  # Convert back to a list
        'realtor_name': poster.realtor_name,
        'realtor_role': poster.realtor_role,
        'realtor_image': poster.realtor_image.url,
        'contact_number': poster.contact_number,
        'contact_email': poster.contact_email,
        'website': poster.website,
    }
    return render(request, 'poster_template.html', context)


def poster_list(request):
    posters = Poster.objects.all()
    return render(request, 'poster_list.html', {'posters': posters})

