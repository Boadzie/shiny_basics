from htmltools import HTMLDependency, tags
import json 

def tailwind_dependency(plugins = None, config = None, styles = None):
    href = "https://cdn.tailwindcss.com"
    if plugins:
        href += f"?plugins={','.join(plugins)}"

    head = [tags.script(src=href)]

    if config:
        head.append(tags.script(f"tailwind.config = {json.dumps(config)}"))

    if styles:
        head.append(tags.style(styles, type="text/tailwindcss"))

    return HTMLDependency(
        name = "tailwind",
        version = "3.3.1",
        head=head
    )


tailwind = tailwind_dependency(
    plugins=["typography"],
    config=dict(theme = dict(extend = dict(colors = dict(clifford = "#da373d")))),
    styles="""
      @layer utilities {
        .content-auto {
          content-visibility: auto;
        }
      }
    """,
)