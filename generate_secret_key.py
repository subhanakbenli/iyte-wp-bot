#!/usr/bin/env python
"""
Django SECRET_KEY generator
Run this script to generate a new SECRET_KEY for your Django project
"""

from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    print("🔐 Yeni Django SECRET_KEY:")
    print(get_random_secret_key())
    print("\n⚠️  Bu anahtarı .env dosyanıza kopyalayın ve eski anahtarı silin!")
