from django.views.generic import TemplateView, CreateView, UpdateView
from django.http import JsonResponse
from summarize import summarizer


class HomeView(TemplateView):
    title = 'Text summarization app'
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PostTextView(CreateView):
    def post(self, request, *args, **kwargs):
        text = request.POST.get('story')
        print("Processing started...", flush=True)
        summary = summarizer.summarize(text)
        print(summary, flush=True)
        data = {'success': True, 'summary': summary}
        return JsonResponse(data)
