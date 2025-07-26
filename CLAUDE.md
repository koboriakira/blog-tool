# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **blog-tool**, a Python CLI utility for managing Markdown blog posts with a focus on tag management and link formatting. The tool operates on blog files in `~/git/blog/content/` and provides automated tag detection, linking, and frontmatter management.

## Development Commands

### Installation and Setup
```bash
# Build and install from source
python setup.py sdist
pip install dist/blog-tool-1.0.tar.gz

# Development installation
pip install -e .

# Install with Docker
docker build -t blog-tool .
```

### Testing
```bash
# Run tests
python -m pytest tests/
# or
python -m unittest discover tests/
```

### Core CLI Commands
```bash
# Auto-detect and add tags to today's post
blog-tool add_tags

# Process specific file
blog-tool add_tags --file content/2023/08/05.md

# Process all markdown files
blog-tool add_tags --all

# Add specific tag to all relevant files
blog-tool add_tag --tag "タグ名"

# Remove tag from all files
blog-tool remove_tag --tag "タグ名"

# Convert [[double brackets]] to markdown links
blog-tool bracket --file content/2023/08/05.md
```

## Architecture

### Core Components
- **CLI Entry Point**: `blog_tool/cli.py` - Main command dispatcher
- **Tags Management**: `blog_tool/tags.py` - Core Tags class for tag collections
- **Command Modules**: Each CLI command has its own module (`add_tags.py`, `add_tag.py`, `remove_tag.py`, `format_double_brackets.py`)
- **File Discovery**: `blog_tool/get_all_files.py` - Recursively finds markdown files

### Key Design Patterns
- **Hardcoded Blog Path**: All operations target `~/git/blog/content/`
- **Frontmatter Management**: Updates YAML `tags:` field in markdown headers
- **Link Generation**: Creates `/tags/tag-name` style links with URL encoding for spaces
- **Atomic File Operations**: Read entire file → process → write back

### Tag Processing Flow
1. **Detection**: Scan markdown content for tag text patterns
2. **Linking**: Convert text to `[tag](/tags/tag-name)` format
3. **Frontmatter Update**: Add/remove tags from YAML header
4. **Deduplication**: Remove duplicate tags automatically

## File Structure
- Target files: `~/git/blog/content/**/*.md`
- Default file pattern: `{year}/{month:02}/{day:02}.md`
- Entry point: `blog_tool.cli:execute`

## Important Notes
- Tool is designed for Japanese blog content
- Handles spaces in tags via URL encoding (`%20`)
- Uses current date for default file paths when no file specified
- All commands operate on markdown files with YAML frontmatter