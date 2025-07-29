<html>
<head>
<title>hanghangman.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #bcbec4;}
.s1 { color: #bcbec4;}
.s2 { color: #6aab73;}
.s3 { color: #cf8e6d;}
.s4 { color: #2aacb8;}
.s5 { color: #7a7e85;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
hanghangman.py</font>
</center></td></tr></table>
<pre><span class="s0">stages </span><span class="s1">= [</span><span class="s2">r''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      | 
========= 
'''</span><span class="s1">, </span><span class="s2">r''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      | 
========= 
'''</span><span class="s1">, </span><span class="s2">r''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      | 
========= 
'''</span><span class="s1">, </span><span class="s2">''' 
  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      | 
========='''</span><span class="s1">, </span><span class="s2">''' 
  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      | 
========= 
'''</span><span class="s1">, </span><span class="s2">''' 
  +---+ 
  |   | 
  O   | 
      | 
      | 
      | 
========= 
'''</span><span class="s1">, </span><span class="s2">''' 
  +---+ 
  |   | 
      | 
      | 
      | 
      | 
========= 
'''</span><span class="s1">]</span>

<span class="s0">logo </span><span class="s1">= </span><span class="s2">r'''  
 _                                              
| |                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
| | | | (_| | | | | (_| | | | | | | (_| | | | | 
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    __/ |                       
                   |___/    '''</span>

<span class="s0">word_list </span><span class="s1">= [</span><span class="s2">&quot;misir&quot;</span><span class="s1">, </span><span class="s2">&quot;cips&quot;</span><span class="s1">, </span><span class="s2">&quot;cikolata&quot;</span><span class="s1">, </span><span class="s2">&quot;cerez&quot;</span><span class="s1">, </span><span class="s2">&quot;cekirdek&quot;</span><span class="s1">, </span><span class="s2">&quot;biskuvi&quot;</span><span class="s1">, </span><span class="s2">&quot;kurabiye&quot;</span><span class="s1">, </span><span class="s2">&quot;pasta&quot;</span><span class="s1">]</span>

<span class="s3">import </span><span class="s0">random</span>

<span class="s0">lives </span><span class="s1">= </span><span class="s4">6</span>

<span class="s0">print</span><span class="s1">(</span><span class="s0">logo</span><span class="s1">)</span>
<span class="s0">print</span><span class="s1">(</span><span class="s2">&quot;WELCOME TO THE AKCAY'S SNACKTIME HANGMAN. LETS SEE IF SELINTO MAKES CORRECT GUESSES&quot;</span><span class="s1">)</span>
<span class="s0">chosen_word </span><span class="s1">= </span><span class="s0">random</span><span class="s1">.</span><span class="s0">choice</span><span class="s1">(</span><span class="s0">word_list</span><span class="s1">)</span>
<span class="s5"># print(chosen_word)</span>

<span class="s0">placeholder </span><span class="s1">= </span><span class="s2">&quot;&quot;</span>
<span class="s0">word_length </span><span class="s1">= </span><span class="s0">len</span><span class="s1">(</span><span class="s0">chosen_word</span><span class="s1">)</span>
<span class="s3">for </span><span class="s0">position </span><span class="s3">in </span><span class="s0">range</span><span class="s1">(</span><span class="s0">word_length</span><span class="s1">):</span>
    <span class="s0">placeholder </span><span class="s1">+= </span><span class="s2">&quot;_&quot;</span>
<span class="s0">print</span><span class="s1">(</span><span class="s2">&quot;Word to guess: &quot; </span><span class="s1">+ </span><span class="s0">placeholder</span><span class="s1">)</span>

<span class="s0">game_over </span><span class="s1">= </span><span class="s3">False</span>
<span class="s0">correct_letters </span><span class="s1">= []</span>

<span class="s3">while not </span><span class="s0">game_over</span><span class="s1">:</span>

    <span class="s0">print</span><span class="s1">(</span><span class="s2">f&quot;****************************&lt;</span><span class="s3">{</span><span class="s0">lives</span><span class="s3">}</span><span class="s2">&gt;/6 LIVES LEFT****************************&quot;</span><span class="s1">)</span>
    <span class="s0">guess </span><span class="s1">= </span><span class="s0">input</span><span class="s1">(</span><span class="s2">&quot;Guess a letter: &quot;</span><span class="s1">).</span><span class="s0">lower</span><span class="s1">()</span>

    <span class="s3">if </span><span class="s0">guess </span><span class="s3">in </span><span class="s0">correct_letters</span><span class="s1">:</span>
        <span class="s0">print</span><span class="s1">(</span><span class="s2">f&quot;You have already guessed </span><span class="s3">{</span><span class="s0">guess</span><span class="s3">}</span><span class="s2">&quot;</span><span class="s1">)</span>

    <span class="s0">display </span><span class="s1">= </span><span class="s2">&quot;&quot;</span>

    <span class="s3">for </span><span class="s0">letter </span><span class="s3">in </span><span class="s0">chosen_word</span><span class="s1">:</span>
        <span class="s3">if </span><span class="s0">letter </span><span class="s1">== </span><span class="s0">guess</span><span class="s1">:</span>
            <span class="s0">display </span><span class="s1">+= </span><span class="s0">letter</span>
            <span class="s0">correct_letters</span><span class="s1">.</span><span class="s0">append</span><span class="s1">(</span><span class="s0">guess</span><span class="s1">)</span>
        <span class="s3">elif </span><span class="s0">letter </span><span class="s3">in </span><span class="s0">correct_letters</span><span class="s1">:</span>
            <span class="s0">display </span><span class="s1">+= </span><span class="s0">letter</span>
        <span class="s3">else</span><span class="s1">:</span>
            <span class="s0">display </span><span class="s1">+= </span><span class="s2">&quot;_&quot;</span>

    <span class="s0">print</span><span class="s1">(</span><span class="s2">&quot;Word to guess: &quot; </span><span class="s1">+ </span><span class="s0">display</span><span class="s1">)</span>

    <span class="s3">if </span><span class="s0">guess </span><span class="s3">not in </span><span class="s0">chosen_word</span><span class="s1">:</span>
        <span class="s0">lives </span><span class="s1">-= </span><span class="s4">1</span>
        <span class="s0">print</span><span class="s1">(</span><span class="s2">f&quot;You guessed </span><span class="s3">{</span><span class="s0">guess</span><span class="s3">}</span><span class="s2">, BUT THAT'S NOT IN THE WORD. You LOSE a life.&quot;</span><span class="s1">)</span>
        <span class="s3">if </span><span class="s0">lives </span><span class="s1">== </span><span class="s4">0</span><span class="s1">:</span>
            <span class="s0">game_over </span><span class="s1">= </span><span class="s3">True</span>

            <span class="s0">print</span><span class="s1">(</span><span class="s2">f&quot;***********************IT WAS </span><span class="s3">{</span><span class="s0">chosen_word</span><span class="s3">} </span><span class="s2">YOU LOSE**********************&quot;</span><span class="s1">)</span>

    <span class="s3">if </span><span class="s2">&quot;_&quot; </span><span class="s3">not in </span><span class="s0">display</span><span class="s1">:</span>
        <span class="s0">game_over </span><span class="s1">= </span><span class="s3">True</span>
        <span class="s0">print</span><span class="s1">(</span><span class="s2">&quot;****************************YOU WIN****************************&quot;</span><span class="s1">)</span>

    <span class="s0">print</span><span class="s1">(</span><span class="s0">stages</span><span class="s1">[</span><span class="s0">lives</span><span class="s1">])</span>
</pre>
</body>
</html>