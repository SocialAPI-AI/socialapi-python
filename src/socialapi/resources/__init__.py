"""API resource namespaces."""

from socialapi.resources.accounts import Accounts, AsyncAccounts
from socialapi.resources.comments import AsyncComments, Comments
from socialapi.resources.dms import AsyncDMs, DMs
from socialapi.resources.feedback import AsyncFeedback, Feedback
from socialapi.resources.interactions import AsyncInteractions, Interactions
from socialapi.resources.keys import AsyncKeys, Keys
from socialapi.resources.media import AsyncMedia, Media
from socialapi.resources.mentions import AsyncMentions, Mentions
from socialapi.resources.oauth import AsyncOAuth, OAuth
from socialapi.resources.posts import AsyncPosts, Posts
from socialapi.resources.reviews import AsyncReviews, Reviews
from socialapi.resources.usage import AsyncUsage, Usage
from socialapi.resources.users import AsyncUsers, Users
from socialapi.resources.webhooks import AsyncWebhooks, Webhooks

__all__ = [
    "Accounts",
    "AsyncAccounts",
    "AsyncComments",
    "AsyncDMs",
    "AsyncFeedback",
    "AsyncInteractions",
    "AsyncKeys",
    "AsyncMedia",
    "AsyncMentions",
    "AsyncOAuth",
    "AsyncPosts",
    "AsyncReviews",
    "AsyncUsage",
    "AsyncUsers",
    "AsyncWebhooks",
    "Comments",
    "DMs",
    "Feedback",
    "Interactions",
    "Keys",
    "Media",
    "Mentions",
    "OAuth",
    "Posts",
    "Reviews",
    "Usage",
    "Users",
    "Webhooks",
]
