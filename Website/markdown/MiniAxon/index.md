---
pagename: MiniAxon/index
last-modified-date: 2008-09-20
page-template: default
page-type: text/markdown
page-status: current|legacy|needsupdate|deprecated|recommended
---
[Mini-Axon]{style="font-size:24pt;font-weight:600"}

[Build your own Kamaelia Core]{style="font-size:16pt"}

**[Introduction](/MiniAxon/index?template=veryplain)**

**[Standing](/MiniAxon/index?template=veryplain&tab=2)**

**[Walking](/MiniAxon/index?template=veryplain&tab=3)**

**[Interlude](/MiniAxon/index?template=veryplain&tab=4)**

**[Talking](/MiniAxon/index?template=veryplain&tab=5)**

**[Conversing](/MiniAxon/index?template=veryplain&tab=6)**

**[Interlude](/MiniAxon/index?template=veryplain&tab=7)**

**[Summary](/MiniAxon/index?template=veryplain&tab=8)**

[Introduction]{style="font-size: 14pt; font-weight: 600;"}

When using any system, library, or framework, you\'re likely to have a
better understanding of the system and how to better use it if you
really understand how it works. That is you\'ve written the system
rather than someone else. Our preferred approach to date so far for
teaching a novice how to use to Kamaelia has been to get them to write a
version of the core concurrency system. This is framed as a series of
exercises. After having built it, they realise that the system is really
just a simple skein over simple programs.

Furthermore, this set of exercises has normally been done within less
than 2 weeks of the novice learning python. If you\'re a new programmer,
and you\'ve learnt a certain core of python, you should be able to do
and follow these exercises. It might look daunting, but it should be
fine. If you get stuck, please feel free to come chat on IRC or on the
mailing lists!

[Python pre-requisitives:]{style="font-weight: 600;"}

-   classes, methods, functions, if/elif/else, while, try..except,
    for..in.., generators (yield), lists, dictionaries, tuples.

[What\'s in this tutorial?]{style="font-weight: 600;"}

1.  Write a basic [microprocess]{style="font-weight: 600;"}
2.  Build a simple [scheduler ]{style="font-weight: 600;"}to run the
    microprocesses
3.  Interlude, discussing progress so far and what you can do with
    microprocesses and schedulers, putting the next two exercises in
    context
4.  Turn a microprocess into a simple
    [component]{style="font-weight: 600;"}
5.  Create a [postman ]{style="font-weight: 600;"}to deliver data
    between microprocesses
6.  A second interlude where you see how to use your framework to build
    a simple multicast server that can serve a file over multicast. The
    resulting components can be used with the main Axon system as they
    can with your mini-axon system.
7.  Summary

**[Introduction](/MiniAxon/index?template=veryplain)**

**[Standing](/MiniAxon/index?template=veryplain&tab=2)**

**[Walking](/MiniAxon/index?template=veryplain&tab=3)**

**[Interlude](/MiniAxon/index?template=veryplain&tab=4)**

**[Talking](/MiniAxon/index?template=veryplain&tab=5)**

**[Conversing](/MiniAxon/index?template=veryplain&tab=6)**

**[Interlude](/MiniAxon/index?template=veryplain&tab=7)**

**[Summary](/MiniAxon/index?template=veryplain&tab=8)**

[Feedback, Questions ?]{style="font-size:16pt;font-weight:600"}

[Please leave feedback
here](http://kamaelia.sourceforge.net/cgi-bin/blog/blog.cgi?rm=addpostcomment&postid=1131572608)!
Hope you found this tutorial interesting, useful and doable!