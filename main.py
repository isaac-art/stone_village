from datetime import date, datetime
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

def make_empty_md(when, name):
    if when == "today":
        d = date.today()
    elif when == "yesterday":
        d = date.today() - timedelta(days=1)
    elif when == "tomorrow":
        d = date.today() + timedelta(days=1)
    else:
        d = datetime.strptime(when, "%Y%m%d").date()
    text = f'--\n### {d.strftime("%Y-%m-%d")} \n# {name.lower()}\n'
    with open(f'mds/{d.strftime("%Y_%m_%d")}_{name}.md', 'w') as f:
        f.write(text)
    return
  
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
    parser.add_argument("--md", default="+", help="markdown file to be converted", required=False)
    parser.add_argument("--make", help="create an empty markdown file for the given date", required=False)
    parser.add_argument("--name", help="use this name for the new markdown file made by --make", required=False)
    args = parser.parse_args()
    # if --make is set 
    if args.make:
        if args.name:
            make_empty_md(args.make, args.name)
            exit()
    main(args.md)