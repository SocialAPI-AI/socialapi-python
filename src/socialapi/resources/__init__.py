from __future__ import annotations

from socialapi.resources.accounts import Accounts, AsyncAccounts
from socialapi.resources.comments import AsyncComments, Comments
from socialapi.resources.conversations import AsyncConversations, Conversations
from socialapi.resources.feedback import AsyncFeedback, Feedback
from socialapi.resources.keys import AsyncKeys, Keys
from socialapi.resources.mentions import AsyncMentions, Mentions
from socialapi.resources.posts import AsyncPosts, Posts
from socialapi.resources.publishing import AsyncPublishing, Publishing
from socialapi.resources.reviews import AsyncReviews, Reviews
from socialapi.resources.usage import AsyncUsage, Usage
from socialapi.resources.users import AsyncUsers, Users
from socialapi.resources.webhooks import AsyncWebhooks, Webhooks

__all__: list[str] = [
    "Accounts",
    "AsyncAccounts",
    "AsyncComments",
    "AsyncConversations",
    "AsyncFeedback",
    "AsyncKeys",
    "AsyncMentions",
    "AsyncPosts",
    "AsyncPublishing",
    "AsyncReviews",
    "AsyncUsage",
    "AsyncUsers",
    "AsyncWebhooks",
    "Comments",
    "Conversations",
    "Feedback",
    "Keys",
    "Mentions",
    "Posts",
    "Publishing",
    "Reviews",
    "Usage",
    "Users",
    "Webhooks",
]
