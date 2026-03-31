```html
      <a class="navbar-brand navbar-brand-custom" href="{% url 'nucleo:feed_principal' %}">
                <i class="fa-solid fa-diagram-project me-2"></i>ContentTypes Demo
            </a>
            <div class="d-flex gap-3">
                <a href="{% url 'nucleo:feed_principal' %}" class="nav-link-custom">
                    <i class="fa-solid fa-house-chimney me-1"></i>Feed
                </a>
                <a href="/admin/" class="nav-link-custom">
                    <i class="fa-solid fa-gear me-1"></i>Admin
                </a>
```

python manage.py loaddata nucleo/fixture/demo_data.json