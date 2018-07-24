from django.shortcuts import render, get_object_or_404

from hitcount.views import HitCountDetailView

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from django.views.generic import DetailView, ListView
from .models import gPost

import json



class gPostListView(ListView):
	model = gPost
	template_name = 'goodtoknow/post_list.html'


class gPostCountHitDetailView(HitCountDetailView):
    model = gPost        # your model goes here
    count_hit = True    # set to True if you want it to try and count the hit



# class gPostDetailView(DetailView):
# 	model = gPost
# 	template_name = 'goodtoknow/gpost_detail.html'


@login_required
@require_POST	# POST method만 받음
def gpost_like(request):
	pk = request.POST.get('pk', None)
	gpost = get_object_or_404(gPost, pk=pk)

	gpost_like, gpost_like_created = gpost.likegpost_set.get_or_create(user=request.user)

	if not gpost_like_created:
		gpost_like.delete()
		message = "좋아요 취소"
	else:
		message = "좋아요"

	context = {
				'like_count': gpost.like_count,
				'message': message,
				'username': request.user.username
	}

	return HttpResponse(json.dumps(context))
