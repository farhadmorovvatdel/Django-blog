from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from django.views import View


from .models import Blog,Comment
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView

from .forms import CommentForm,CreatePostForm,UpdateCommentForm

class All_Blogs(ListView):
    context_object_name = 'blog'
    template_name = 'blog/allblogs.html'
    paginate_by = 3

    def get_queryset(self):
        blog=Blog.objects.filter(publish=True)
        return  blog


class DetailPost(DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    model = Blog
    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)
        context['commentform']=CommentForm
        return context

class CreatePost(LoginRequiredMixin,CreateView):
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog:Blogs')
    form_class = CreatePostForm

    def form_valid(self,form):
        print(self.request.path)
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(CreatePost, self).form_valid(form)



class UserPost(View):
    def get(self,request):
        posts=Blog.objects.filter(user=self.request.user)
        return render(request,'blog/userblogs.html',{'posts':posts})

class DeletePost(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:user_post')
    template_name ='blog/confirm_delete.html'



def AddComment(request,id):
    post=get_object_or_404(Blog,id=id)
    user=request.user
    commentform=CommentForm(request.POST or None)
    if commentform.is_valid():
        body=commentform.cleaned_data['body']
        newcomment=commentform.save(commit=False)
        newcomment.user=user
        newcomment.post=post
        newcomment.body=body
        newcomment.save()
        return redirect('blog:detail',post.id)
    return render(request,'blog/detail.html')

def DeleteComment(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('blog:detail',comment.post.id)

def UpdateComment(request,comment_id):
    commentt=get_object_or_404(Comment,id=comment_id)
    updatecomment = UpdateCommentForm(request.POST or None,instance=commentt)
    if updatecomment.is_valid():
       body = updatecomment.cleaned_data['body']
       comment = Comment.objects.filter(id=comment_id).update(body=body)

       return redirect('blog:detail',commentt.post.id)
    return render(request,'blog/updatecomment.html',{'updatecomment':updatecomment,'comment_id':comment_id})



