<h1>WIKI TITLES SINGABLE TO (X)</h1>

<p>Basically allows you to do the exact same thing as <a href="https://twitter.com/wiki_tmnt">this account</a>, except
you can fork this repo and easily fill in the blank with whatever meme you'd like. The <i>this_is_america</i> branch already exists for you.</p>

<h2>USAGE</h2>

<ol>
    <li> Duplicate <i>auth_template.py</i> and call the copy <i>auth.py</i></li>
    <li> Create your Twitter app and link it to this app by filling in the various public/private key combination fields
            in your new <i>auth.py</i> file.
    </li>
    <li> Add images you'd like to appear in your tweets to img/ directory. </li>
    <li> Update line 13 in main.py with the number of syllables you'd like. The default is 5. (5 felt like
            a good number.)
    </li>
    <li>Update <i>forbidden_phrases.txt</i> with any phrases you'd like to exclude from search.
            I will be updating this as necessary.</li>
</ol>

<h2>REQUIREMENTS</h2>

<ul>
    <li><a href="https://pypi.org/project/wikipedia/">Wikipedia</a></li>
    <li><a href="https://pypi.org/project/syllables/">Syllables</a></li>
    <li><a href="http://docs.tweepy.org/en/latest/index.html">tweePy</a></li>
<ul>