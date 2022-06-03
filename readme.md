<h1 align="center">Analytical Core Smart Public Transport</h1>
<h3 align="center"><img src='./static/img/logo.png'></h3>


## Prototype analytical core
---
###### title: "Prototype analytical core"
###### author: Osintsev Artem
###### date: 19.05.2022
---
The analytical core processes incoming requests for data processing using predictive analysis methods. The result of the work is a JSON package with the results of the analysis. A packet with the result is sent to the client from which the data came.


<h1>Demo</h1>
<img src='./static/img/demo.gif' width='100%'>


<h1>Installation</h1>
<ol>
<li> Clone repo. </li>
<li> In workdir: <code> pip install -r requirements.txt </code></li>
<li> in console (in workdir) run: <code>uvicorn main:app --reload</code> </li>
</ol>

<ul>
<li> Username: demo </li>
<li> Password: demo-123 </li>
</ul>

&nbsp;&nbsp;The project also contains Docker files so you can build your image in container.

<h1>License</h1>
This project is licensed under the GPL-3.0 License.
