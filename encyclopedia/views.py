from django.shortcuts import redirect, render
from django.http import HttpResponse
import random
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    entry = util.get_entry(title)
    entry=markdown2.markdown(entry)

    if entry is None:
        return HttpResponse("Entry not found")

    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "title":title
    })
def search(request):
    query = request.GET.get("q", "").strip()
    entries = util.list_entries()
    for title in entries:
      if query.lower() == title.lower():
        return redirect ("encyclopedia:entry", title=query)
    results = [title for title in entries if query.lower() in title.lower()]  
    return render(request, "encyclopedia/search.html",{
       "results":results
    })
    
    
   
def newpage(request):

    return render(request, "encyclopedia/newpage.html")
def created_page(request):
    if request.method == "POST":
        title=request.POST["title"]
        content = request.POST["content"]
        if title in util.list_entries():
          return render(request, "encyclopedia/ newpage.html",{
              "error": "This entry already exist."
          })
        util.save_entry(title, content)
        
        return redirect( "encyclopedia:entry", title=title)
    return render("encyclopedia:newpage")

def editpage(request, title):

    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", title=title)

    content = util.get_entry(title)

    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "content": content
    })
def random_page (request):
    titles=util.list_entries()
    title=random.choice(titles)
    return redirect("encyclopedia:entry", title=title)