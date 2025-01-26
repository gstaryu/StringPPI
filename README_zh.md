# StringPPI

该仓库用于处理STRING网站的PPI数据。

### 解决STRING网站的2000个输入蛋白质的限制
由于STRING网站（<https://string-db.org/>）一次最多输入2000个蛋白质，`string_input_limiter.py`将STRING网站中的和PPI相关的数据（<https://string-db.org/cgi/download>）做了处理，可以输入任意数量的蛋白质。

注意：只处理数据，没有绘制PPI图的功能，请使用Cytoscape等其它工具绘图。

### 使用STRING API获取PPI
`string_API.py`调用了STRING的API，适合批量处理。
