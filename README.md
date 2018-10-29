# Jekyll to Hugo migration script

If you're looking for an easy way to migrate files from your Jekyll site to your new Hugo site, you can use this script. 

This script iterates over all the files in a directory in Jekyll and copies them to a destination script in Hugo.

## Usage

1. Clone this repo
1. Copy the absolute path of your Jekyll files (use `pwd`) to the clipboard or somewhere accessible
1. Copy the absolute path of where your Hugo files should go (use `pwd`) to the clipboard or somewhere accessible
1. Run the script

Example:

```
python jekyll-to-hugo.py -dest "/Users/YOUR_USERNAME/HUGO_SITE/content/posts" -source "/Users/YOUR_USERNAME/PATH/JEKYLL_SITE/_posts"
```
