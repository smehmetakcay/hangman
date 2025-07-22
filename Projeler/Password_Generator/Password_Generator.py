<html>
<head>
<title>task.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #bcbec4;}
.s1 { color: #bcbec4;}
.s2 { color: #6aab73;}
.s3 { color: #cf8e6d;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
task.py</font>
</center></td></tr></table>
<pre><span class="s0">letters </span><span class="s1">= [</span><span class="s2">'a'</span><span class="s1">, </span><span class="s2">'b'</span><span class="s1">, </span><span class="s2">'c'</span><span class="s1">, </span><span class="s2">'d'</span><span class="s1">, </span><span class="s2">'e'</span><span class="s1">, </span><span class="s2">'f'</span><span class="s1">, </span><span class="s2">'g'</span><span class="s1">, </span><span class="s2">'h'</span><span class="s1">, </span><span class="s2">'i'</span><span class="s1">, </span><span class="s2">'j'</span><span class="s1">, </span><span class="s2">'k'</span><span class="s1">, </span><span class="s2">'l'</span><span class="s1">, </span><span class="s2">'m'</span><span class="s1">, </span><span class="s2">'n'</span><span class="s1">, </span><span class="s2">'o'</span><span class="s1">, </span><span class="s2">'p'</span><span class="s1">, </span><span class="s2">'q'</span><span class="s1">, </span><span class="s2">'r'</span><span class="s1">, </span><span class="s2">'s'</span><span class="s1">, </span><span class="s2">'t'</span><span class="s1">, </span><span class="s2">'u'</span><span class="s1">, </span><span class="s2">'v'</span><span class="s1">, </span><span class="s2">'w'</span><span class="s1">, </span><span class="s2">'x'</span><span class="s1">, </span><span class="s2">'y'</span><span class="s1">, </span><span class="s2">'z'</span><span class="s1">, </span><span class="s2">'A'</span><span class="s1">, </span><span class="s2">'B'</span><span class="s1">, </span><span class="s2">'C'</span><span class="s1">, </span><span class="s2">'D'</span><span class="s1">, </span><span class="s2">'E'</span><span class="s1">, </span><span class="s2">'F'</span><span class="s1">, </span><span class="s2">'G'</span><span class="s1">, </span><span class="s2">'H'</span><span class="s1">, </span><span class="s2">'I'</span><span class="s1">, </span><span class="s2">'J'</span><span class="s1">, </span><span class="s2">'K'</span><span class="s1">, </span><span class="s2">'L'</span><span class="s1">, </span><span class="s2">'M'</span><span class="s1">, </span><span class="s2">'N'</span><span class="s1">, </span><span class="s2">'O'</span><span class="s1">, </span><span class="s2">'P'</span><span class="s1">, </span><span class="s2">'Q'</span><span class="s1">, </span><span class="s2">'R'</span><span class="s1">, </span><span class="s2">'S'</span><span class="s1">, </span><span class="s2">'T'</span><span class="s1">, </span><span class="s2">'U'</span><span class="s1">, </span><span class="s2">'V'</span><span class="s1">, </span><span class="s2">'W'</span><span class="s1">, </span><span class="s2">'X'</span><span class="s1">, </span><span class="s2">'Y'</span><span class="s1">, </span><span class="s2">'Z'</span><span class="s1">]</span>
<span class="s0">numbers </span><span class="s1">= [</span><span class="s2">'0'</span><span class="s1">, </span><span class="s2">'1'</span><span class="s1">, </span><span class="s2">'2'</span><span class="s1">, </span><span class="s2">'3'</span><span class="s1">, </span><span class="s2">'4'</span><span class="s1">, </span><span class="s2">'5'</span><span class="s1">, </span><span class="s2">'6'</span><span class="s1">, </span><span class="s2">'7'</span><span class="s1">, </span><span class="s2">'8'</span><span class="s1">, </span><span class="s2">'9'</span><span class="s1">]</span>
<span class="s0">symbols </span><span class="s1">= [</span><span class="s2">'!'</span><span class="s1">, </span><span class="s2">'#'</span><span class="s1">, </span><span class="s2">'$'</span><span class="s1">, </span><span class="s2">'%'</span><span class="s1">, </span><span class="s2">'&amp;'</span><span class="s1">, </span><span class="s2">'('</span><span class="s1">, </span><span class="s2">')'</span><span class="s1">, </span><span class="s2">'*'</span><span class="s1">, </span><span class="s2">'+'</span><span class="s1">]</span>

<span class="s0">print</span><span class="s1">(</span><span class="s2">&quot;Welcome to the PyPassword Generator!&quot;</span><span class="s1">)</span>
<span class="s0">nr_letters </span><span class="s1">= </span><span class="s0">int</span><span class="s1">(</span><span class="s0">input</span><span class="s1">(</span><span class="s2">&quot;How many letters would you like in your password?</span><span class="s3">\n</span><span class="s2">&quot;</span><span class="s1">))</span>
<span class="s0">nr_symbols </span><span class="s1">= </span><span class="s0">int</span><span class="s1">(</span><span class="s0">input</span><span class="s1">(</span><span class="s2">f&quot;How many symbols would you like?</span><span class="s3">\n</span><span class="s2">&quot;</span><span class="s1">))</span>
<span class="s0">nr_numbers </span><span class="s1">= </span><span class="s0">int</span><span class="s1">(</span><span class="s0">input</span><span class="s1">(</span><span class="s2">f&quot;How many numbers would you like?</span><span class="s3">\n</span><span class="s2">&quot;</span><span class="s1">))</span>

<span class="s0">password_list </span><span class="s1">= []</span>

<span class="s3">import </span><span class="s0">random</span>

<span class="s3">for </span><span class="s0">item </span><span class="s3">in </span><span class="s0">range</span><span class="s1">(</span><span class="s0">nr_letters</span><span class="s1">):</span>
    <span class="s0">password_list</span><span class="s1">.</span><span class="s0">append</span><span class="s1">(</span><span class="s0">random</span><span class="s1">.</span><span class="s0">choice</span><span class="s1">(</span><span class="s0">letters</span><span class="s1">))</span>
<span class="s3">for </span><span class="s0">item </span><span class="s3">in </span><span class="s0">range</span><span class="s1">(</span><span class="s0">nr_symbols</span><span class="s1">):</span>
    <span class="s0">password_list</span><span class="s1">.</span><span class="s0">append</span><span class="s1">(</span><span class="s0">random</span><span class="s1">.</span><span class="s0">choice</span><span class="s1">(</span><span class="s0">symbols</span><span class="s1">))</span>
<span class="s3">for </span><span class="s0">item </span><span class="s3">in </span><span class="s0">range</span><span class="s1">(</span><span class="s0">nr_numbers</span><span class="s1">):</span>
    <span class="s0">password_list</span><span class="s1">.</span><span class="s0">append</span><span class="s1">(</span><span class="s0">random</span><span class="s1">.</span><span class="s0">choice</span><span class="s1">(</span><span class="s0">numbers</span><span class="s1">))</span>

<span class="s0">print</span><span class="s1">(</span><span class="s0">password_list</span><span class="s1">)</span>

<span class="s0">random</span><span class="s1">.</span><span class="s0">shuffle</span><span class="s1">(</span><span class="s0">password_list</span><span class="s1">)</span>
<span class="s0">password </span><span class="s1">= </span><span class="s2">' '</span><span class="s1">.</span><span class="s0">join</span><span class="s1">(</span><span class="s0">password_list</span><span class="s1">)</span>

<span class="s0">print</span><span class="s1">(</span><span class="s2">f&quot;Your password is: </span><span class="s3">{</span><span class="s0">password</span><span class="s3">}</span><span class="s2">&quot;</span><span class="s1">)</span>
</pre>
</body>
</html>