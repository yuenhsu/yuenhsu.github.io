from pathlib import Path


styles = [
    "a11y",
    "arrow",
    "atom-one",
    "ayu",
    "breeze",
    "breezedark",
    "dracula",
    "espresso",
    "github",
    "gruvbox",
    "haddock",
    "kate",
    "monochrome",
    "monokai",
    "nord",
    "oblivion",
    "printing",
    "pygments",
    "radical",
    "solarized",
    "tango",
    "vim-dark",
    "zenburn",
]

project_dir = Path.cwd().joinpath("drafts/highlight-styles")
for style in styles:
    content = [
        "---",
        f"highlight-style: {style}",
        "---",
        "",
        "::: {#snip}",
        "",
        r"{{< include /drafts/highlight-styles/code-snippets.qmd >}}",
        "",
        ":::",
    ]
    with open(project_dir.joinpath(f"{style}.qmd"), "w") as f:
        f.write("\n".join(content))
    with open(project_dir.joinpath(f"{style}-dark.qmd"), "w") as f:
        f.write("\n".join(content).replace(style, f"{style}-dark"))
    print(f"Created {style}.qmd")
