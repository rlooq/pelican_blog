Title: Pelican on Netlify
Date: 2021-12-28

Not much to do over Christmas, with Omicron-related restrictions and all, so I managed to put together this simple blog between meals. The domain name was my only Black Friday purchase this year, couldn't make up my mind and ended up with this non-sensical title: **Highnoon Ruffles**, which has a cute story behind. I may tell it one of these days. But for now, suffice it to say I am the Ruffles in that story.

So, anyway, I'm at my parents' place for Christmas, and all I brought with me is a very old (but sturdy) MacBook Pro running Manjaro i3, which has given it a second lease on life. My other laptop is a newer but crankier piece of junk that complaints loudly with the slightest movement. When the fan gets going, it sounds like the dungeons of the Spanish Inquisition. No sane person can ignore it and focus on work. But I digress. Word of wisdom to you, though: never *ever* buy an HP laptop. Back to the point now: the process of making this site was pretty smooth thanks to [Pelican](https://docs.getpelican.com/en/latest/), a Python-based static site generator, and a simple theme adapted from [Hyde](https://github.com/jvanz/pelican-hyde), which is itself based on something else. In the past I had used [Hugo](https://gohugo.io/), which faster and probably more versatile, but this time I wanted to go with something simpler, based of Python and easier for me to understand. 

The whole thing is hosted for free (https certificate included) on Netlify, which compiles it from a repo on Github. [This article](https://frankcorso.dev/deploying-your-pelican-static-site-to-netlify.html) by Frank Corso, does a great job at explaining each step in the deployment: from creating a Github repo to adjusting the environment variables within Netlify. For the domain name bits, Netlify itself has pretty good documentation.

Now, after tweaking the CSS and templates in the theme, and once the Netlify deployment is set, all I have to do is write plain-text files with some markdown, which are then converted into HTML by Pelican. Any changes I make in my laptop, once commited, Netlify gets them from Github and recompiles the site automatically.

Beautiful, great news, Mr. Ruffles. But then what? What are you going to write about? What is it that you have to say?

Not sure how to answer that, Mr. Voice-in-my-head, not yet at least. I'll have to figure it out over the next few posts. The world out there (on- and offline) is very much unpolished, and it doesn't make a whole lot of sense if you ask me, so what's the harm in a little more of that?
