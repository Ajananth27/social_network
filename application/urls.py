from django.urls import path
from .views import SignupView, LoginView, SearchUserView, SendFriendRequestView, AcceptFriendRequestView, RejectFriendRequestView, ListFriendsView, ListPendingFriendRequestsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', SearchUserView.as_view(), name='search_users'),
    path('send-friend-request/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('accept-friend-request/<int:request_id>/', AcceptFriendRequestView.as_view(), name='accept_friend_request'),
    path('reject-friend-request/<int:request_id>/', RejectFriendRequestView.as_view(), name='reject_friend_request'),
    path('friends/', ListFriendsView.as_view(), name='list_friends'),
    path('pending-requests/', ListPendingFriendRequestsView.as_view(), name='list_pending_requests'),
]
