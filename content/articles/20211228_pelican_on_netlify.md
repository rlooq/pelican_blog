Title: Pelican on Netlify
Date: 2021-12-28
Description: How I started this blog during a Christmas break using Pelican, Netlify, and a very old MacBook Pro running Manjaro i3.

Not much to do over Christmas, with Omicron-related restrictions and all, so I managed to put together this simple blog between meals. This odd domain name was my only Black Friday purchase this year. I couldn't make up my mind and ended up with the non-sensical **Highnoon Ruffles**, which has a cute story behind. More on that some other time.

So, anyway, I'm at my parents' place for Christmas, and all I brought with me is a very old (but sturdy) MacBook Pro running Manjaro i3, which has given it a second lease on life. My other laptop is a newer but crankier piece of junk that complains loudly with the slightest movement. When the fan gets going, it sounds like the dungeons of the Spanish Inquisition. No sane person can ignore it and focus on work. But I digress. Word of wisdom to you, though: never *ever* buy an HP laptop. 

Back to the point now: the process of making this site was pretty smooth thanks to [Pelican](https://docs.getpelican.com/en/latest/), a Python-based static site generator, and a simple theme adapted from [Hyde](https://github.com/jvanz/pelican-hyde), which is itself based on something else. In the past I had used [Hugo](https://gohugo.io/), which is faster and probably more versatile, but this time I wanted to go with something simpler, Python-based and, hence, easier for me to understand. 

The whole thing is hosted for free (https certificate included) on Netlify, which compiles it from a repo on Github. [This article](https://frankcorso.dev/deploying-your-pelican-static-site-to-netlify.html) by Frank Corso, does a great job at explaining each step in the deployment: from creating a Github repo to adjusting the environment variables within Netlify. For the domain name bits, Netlify itself has pretty good [documentation](https://docs.netlify.com/domains-https/custom-domains/).

Now, after tweaking the CSS and templates to my taste, and once the Netlify deployment is set, all I have to do is write plain-text files with some [markdown](https://en.wikipedia.org/wiki/Markdown), which are converted into HTML by Pelican. If I make any changes to my text files, I commit and push them with [`git`](https://git-scm.com/), which triggers Netlify to fetch them from [Github](https://github.com) and recompile the whole site automatically. It sounds complicated, but it's really quick and easy in practice.

To make it look less empty, I have populated the site with a bric-a-brac of old stuff I had written in the past, going as far back as 2011. But *this* is the initial post, *this* is the beginning.

Beautiful, great news, Mr. Ruffles. But then what? What are you going to write about? What is it that you have to say?

Not sure how to answer that, Mr. Voice-in-my-head, not yet at least. I'll have to figure it out over the next few posts. The world out there (on- and offline) is very much unpolished, and it doesn't make a whole lot of sense if you ask me, so what's the harm in a little more of that?

Find a niche, you say? Niches are for marble statues. And please, stop talking to me while I write.
