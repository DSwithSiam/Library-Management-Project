from django.urls import reverse
from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from author.models import BorrowingDataModel, UserAccount
from author.views import ConfarmationEmail
from .forms import *
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

    
class DetailsPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam 
        comments = post.comment.all()
        comment_form = CommentForm()
        borrow = BorrowingDataModel.objects.filter(user = self.request.user, post=post)
        print(borrow)
        print(post)
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['rev'] = borrow
        return context
    
def BorrowPost(request, id):
    try:
        acc = UserAccount.objects.get(user=request.user)
        post = Post.objects.get(id=id)

        if acc.balance >= post.price:
            acc.balance -= post.price
            acc.save()

            add_data = BorrowingDataModel.objects.create(
                book_name=post.title,
                book_price=post.price,
                balance=acc.balance,
                user=request.user,
                post=post
            )
            add_data.save()

            messages.success(
                request,
                'Borrowing successfully'
            )

            mail_subject = 'Borrowing successfully'
            to_email = request.user.email
            ConfarmationEmail(request.user, to_email, "Borrowing", mail_subject, 0, 'borrow_email.html')
            
        else:
            messages.error(
                request,
                "Your account doesn't have enough money."
            )

    except (UserAccount.DoesNotExist, Post.DoesNotExist):
        messages.error(
            request,
            "Your account doesn't have enough money."
        )
    redirect_url = reverse('detail_post', args=[id])
    return redirect(redirect_url)


def ReturnBook(request, id):
    acc = UserAccount.objects.get(user = request.user)
    borrow = BorrowingDataModel.objects.get(id = id)
    print(borrow.book_price)
    acc.balance += borrow.book_price
    acc.save()
    borrow.delete()
    return redirect('profile')
    
    