from __future__ import annotations

from socialapi.resources.accounts import Accounts, AsyncAccounts
from socialapi.resources.brands import AsyncBrands, Brands
from socialapi.resources.comments import AsyncComments, Comments
from socialapi.resources.conversations import AsyncConversations, Conversations
from socialapi.resources.events import AsyncEvents, Events
from socialapi.resources.feedback import AsyncFeedback, Feedback
from socialapi.resources.invites import AsyncInvites, Invites
from socialapi.resources.keys import AsyncKeys, Keys
from socialapi.resources.media import AsyncMedia, Media
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
    "AsyncBrands",
    "AsyncComments",
    "AsyncConversations",
    "AsyncEvents",
    "AsyncFeedback",
    "AsyncInvites",
    "AsyncKeys",
    "AsyncMedia",
    "AsyncMentions",
    "AsyncPosts",
    "AsyncPublishing",
    "AsyncReviews",
    "AsyncUsage",
    "AsyncUsers",
    "AsyncWebhooks",
    "Brands",
    "Comments",
    "Conversations",
    "Events",
    "Feedback",
    "Invites",
    "Keys",
    "Media",
    "Mentions",
    "Posts",
    "Publishing",
    "Reviews",
    "Usage",
    "Users",
    "Webhooks",
]
