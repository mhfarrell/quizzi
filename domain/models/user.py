from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Optional display name (for UI)
    display_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text="Optional display name"
    )

    # OAuth provider (e.g., google, discord)
    oauth_provider = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="OAuth provider name"
    )

    # Provider-specific user ID (e.g., Google UID)
    oauth_uid = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Unique user ID from the OAuth provider"
    )

    # Profile metadata
    profile_picture = models.URLField(blank=True, null=True)
    locale = models.CharField(max_length=10, blank=True, null=True)
    email_verified = models.BooleanField(default=False)

    class Meta:
        unique_together = ('oauth_provider', 'oauth_uid')

    def __str__(self):
        return self.display_name or self.username
