from datetime import date
import markdown
import argparse
from os import listdir, remove

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def empty_posts_dir():
    for f in listdir('posts'):
        if not f.startswith('.'):
            print(f'Removing {f}')
            remove(f'posts/{f}')

def update_index(md):
    posts = [f'<a href="posts/{x}">{x[:-5]}</a>' for x in listdir_nohidden('posts')]
    last_updated = date.today()
    print(posts)
    print(last_updated)
    # open templates/index.html and replace {{POSTS}} with posts
    with open('templates/index_template.html', 'r') as f:
        html = f.read()
    
    updated = html.replace('{POSTS}', '<br>'.join(posts)).replace('{LAST_UPDATED}', str(last_updated))
    
    with open('index.html', 'w') as f:
        print("writing..")
        f.write(updated)


def write_post(md):
    with open(f'mds/{md}.md', 'r') as f:
        html = markdown.markdown(f.read())
        
    with open('templates/post_template.html', 'r') as f:
        template = f.read()
    updated = template.replace('{POST_TITLE}', md).replace('{POST}', html)
    with open(f'posts/{md}.html', 'w') as f:
        f.write(updated) 
    # add link to post to index.html
    update_index(md)
    
def main(md):
    if md == '+':
        for md in listdir_nohidden('mds'):
            if md == 'index.html':
                pass
            else:
                write_post(md[:-3])
    elif md == '-':
        empty_posts_dir()
    else:
        write_post(md)
    
    
if __name__ == "__main__":
    # take argument of markdown file
    parser = argparse.ArgumentParser()
    parser.add_argument("md", help="markdown file to be converted")
    args = parser.parse_args()
    main(args.md)