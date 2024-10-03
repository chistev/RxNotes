from django import template
import re

register = template.Library()


@register.filter
def highlight(text, search_term):
    """Highlight all occurrences of the search term in the text."""
    if search_term:
        # Use regex to wrap the search term in a span with a highlight class
        pattern = re.compile(re.escape(search_term), re.IGNORECASE)
        return pattern.sub(f'<span class="highlight">{search_term}</span>', text)
    return text
